import kaggle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("question one: Pivot + melt + grouped bar")
chess = pd.read_csv("data/raw/chess_games.csv")
pivot = chess.pivot_table(
    values   = 'turns',     # value to aggregate
    index    = 'victory_status',  # rows
    columns  = 'winner',    # columns
    fill_value = 0,         # replace NaN
).round(1)
print(f"the pivoted table: {pivot}")
melt_table = pivot.reset_index().melt(
    id_vars='victory_status',
    var_name='winner',
    value_name='turns'
)
print(f"the melted table: {melt_table}")
fig, ax = plt.subplots(figsize=(9, 5))
ax = sns.barplot(
    data=melt_table, x='victory_status', y='turns',
    hue='winner', palette='Set2', ax=ax
)
# After seaborn → customise with matplotlib:
ax.set_title('Average Turns by Winner',
             fontsize=14, pad=12)
ax.set_xlabel('Winner', fontsize=12)
ax.set_ylabel('Average Turns', fontsize=12)
ax.spines[['top','right']].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
plt.savefig('data/polt/Q1_pivot_table.png', dpi=150,
            bbox_inches='tight')
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f')
plt.close()


###
# END of Q 1 #
###


print("\n\nquestion one: Pivot + melt + grouped bar\n\n")
player_counts = chess['white_id'].value_counts()

eligible_players = player_counts[player_counts > 15].index

random_player = eligible_players.to_series().sample(1).iloc[0]
the_player_ratings = chess[chess['white_id'] == random_player][['white_rating','game_id']]
print(f" the list for a random player is: {the_player_ratings}")

PRating = the_player_ratings
PRating['rolling_5'] = PRating['white_rating'].rolling(5, min_periods=1).mean()
PRating['game_number'] = range(1, len(PRating) + 1)
PRating['expanding_avg'] = PRating['white_rating'].expanding().mean()
fig, ax = plt.subplots(figsize=(12, 5))
# Raw rating values — noisy, light
ax.set_ylim(PRating['white_rating'].min()-50, PRating['white_rating'].max()+50)
ax.set_title('The Rating of a Random Player',fontsize=14, pad=12)
ax.plot(PRating['game_number'], PRating['white_rating'],
        color='BLACK', alpha=0.4, linewidth=0.8, label='raw rating')
# 5 rolling — clear trend
ax.plot(PRating['game_number'], PRating['rolling_5'],
        color='RED', linewidth=2.5, label='5 rolling avg')
# expanding Avg
ax.plot(PRating['game_number'], PRating['expanding_avg'],
        color='BLUE', linewidth=2.5, label='5 rolling avg')
# Zero baseline + shading
ax.axhline(y=0, color='grey', linewidth=0.8, linestyle='--')
ax.legend(frameon=False)
ax.fill_between(PRating['game_number'], 0, PRating['white_rating'],
                where=PRating['white_rating']>0, alpha=0.15, color='BLACK', label='Above baseline')
ax.fill_between(PRating['game_number'], 0, PRating['rolling_5'],
                where=PRating['rolling_5']>0, alpha=0.15, color='YELLOW', label='Below baseline')
ax.fill_between(PRating['game_number'], 0, PRating['expanding_avg'],
                where=PRating['expanding_avg']>0, alpha=0.15, color='BLUE', label='Below baseline')
max_idx = PRating['white_rating'].idxmax()
max_x = PRating.loc[max_idx, 'game_number']
max_y = PRating.loc[max_idx, 'white_rating']

ax.scatter(max_x, max_y, color='orange', s=80, zorder=5)

ax.annotate(
    f"Max: {max_y}",
    xy=(max_x, max_y),
    xytext=(max_x, max_y + 50),
    arrowprops=dict(arrowstyle="->", color='black'),
    fontsize=10
)
fig.tight_layout()
plt.savefig('data/polt/Q2_player_rating.png', dpi=250,
            bbox_inches='tight')
plt.close()


###
# END of Q 2 #
###


TEMP_ANNUAL = pd.read_csv('data/raw/temp_annualy.csv')

gistemp = TEMP_ANNUAL[TEMP_ANNUAL['Source']=='GISTEMP'].copy()
gistemp['rolling_10'] = gistemp['Mean'].rolling(10, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(12, 5))
# Raw annual values — noisy, light
ax.set_title('The temperature throughout the years ',fontsize=14, pad=12)

ax.plot(gistemp['Year'], gistemp['Mean'],
        color='#C9A84C', alpha=0.4, linewidth=0.8, label='Annual')
# 10-year rolling — clear trend
ax.plot(gistemp['Year'], gistemp['rolling_10'],
        color='#C0392B', linewidth=2.5, label='10-year rolling avg')
# Zero baseline + shading
ax.axhline(y=0, color='grey', linewidth=0.8, linestyle='--')
ax.legend(frameon=False)
ax.fill_between(gistemp['Year'], 0, gistemp['Mean'],
                where=gistemp['Mean']>0, alpha=0.15, color='#C0392B', label='Above baseline')
ax.fill_between(gistemp['Year'], 0, gistemp['Mean'],
                where=gistemp['Mean']<=0, alpha=0.15, color='#3D6B4F', label='Below baseline')
max_idx = gistemp['Mean'].idxmax()
max_x = gistemp.loc[max_idx, 'Year']
max_y = gistemp.loc[max_idx, 'Mean']
ax.annotate(
    f"Max: {max_y}",
    xy=(max_x, max_y),
    xytext=(max_x, max_y + 0.05),
    arrowprops=dict(arrowstyle="->", color='black'),
    fontsize=10
)
fig.tight_layout()
plt.savefig('data/polt/Q3_temp_year.png', dpi=250,
            bbox_inches='tight')
plt.close()

###
# END of Q 3 #
###

netflix = pd.read_csv("data/raw/netflix_titles.csv")
movies = netflix[netflix['type']=='Movie'].copy()
movies['duration'] = movies['duration'].str.replace(' min', '').astype(float)
fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(movies['duration'].dropna(), bins=40,
        color='#C9A84C', edgecolor='white',
        label='Movie duration')
ax.set_title('Number of Netflix movies based on duration',fontsize=14, pad=12)
ax.legend(frameon=False)
ax.set_title('Netflix Movies by duration')
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
plt.savefig('data/polt/Q4-1_Netflix_movies_duration.png', dpi=250,
            bbox_inches='tight')
plt.close()

###
# END of Q 4.1 #
###

countries = (netflix['country'].dropna()
             .str.split(', ', expand=True)
             .stack().reset_index(drop=True)
             .rename('country').to_frame())
top10 = countries['country'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(top10.index[::-1], top10.values[::-1], color='#C0392B')
ax.bar_label(bars, padding=5)
ax.spines[['top','right','left']].set_visible(False)
ax.set_title('The Number of Netflix movies based on countries',fontsize=14, pad=12)
ax.tick_params(left=False)
fig.tight_layout()
plt.savefig('data/polt/Q4-2_Netflix_top_countres.png', dpi=250,
            bbox_inches='tight')
plt.close()


###
# END of Q 4.2 #
###


netflix['year_added'] = pd.to_datetime(
    netflix['date_added'].str.strip(),
    errors='coerce').dt.year
added = (netflix
    [netflix['year_added'].between(2013,2021)]
    .groupby(['year_added','type']).size()
    .reset_index(name='count'))
wide = added.pivot(
    index='year_added', columns='type',
    values='count').fillna(0)
fig, ax = plt.subplots(figsize=(9, 5))
wide.plot(kind='bar', stacked=True, ax=ax,
    color=['#C0392B','#1B4F72'],
    edgecolor='white')
ax.set_xlabel('Year'); ax.set_ylabel('Titles Added')
ax.tick_params(axis='x', rotation=0)
ax.set_title('The number of Netflix movies and TV shows over the years',fontsize=14, pad=12)
ax.legend(title='Type', frameon=False)
ax.spines[['top','right']].set_visible(False)

fig.tight_layout()
plt.savefig('data/polt/Q4-3_Netflix_Staked_bar.png', dpi=250,
            bbox_inches='tight')
plt.close()


###
# END of Q 4.3 #
###
TEMP_MONTHLY = pd.read_csv('data/raw/temp_monthly.csv')

TEMP_MONTHLY['date'] = pd.to_datetime(TEMP_MONTHLY['Year'])
TEMP_MONTHLY['month'] = TEMP_MONTHLY['date'].dt.month
TEMP_MONTHLY['decade'] = (TEMP_MONTHLY['date'].dt.year // 10) * 10
gm    = TEMP_MONTHLY[TEMP_MONTHLY['Source']=='GISTEMP']

pivot_temp = gm.pivot_table(
    values='Mean',
    index='month',
    columns='decade',
    aggfunc='mean'
)
pivot_temp.reset_index(inplace=True)

# pivot_table: rows = months, columns = decades
pivot = gm.pivot_table(index='month', columns='decade', values='Mean', aggfunc='mean')
pivot.index = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fig, ax = plt.subplots(figsize=(14, 5))
sns.heatmap(pivot[[c for c in pivot.columns if c>=1950]],
    annot=True, fmt='.2f', cmap='RdYlBu_r', center=0,
    linewidths=0.3, ax=ax, cbar_kws={'label':'Anomaly (°C)'})
ax.set_title('Temperature Anomaly: Month × Decade', fontsize=13)
ax.set_xlabel('Decade'); ax.set_ylabel('')

fig.tight_layout()
plt.savefig('data/polt/Q5_The tempe_month_decade.png', dpi=250,
            bbox_inches='tight')
plt.close()


###
# END of Q 5 #
###


