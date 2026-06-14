import pandas as pd
import os
import kaggle


url = 'https://drive.google.com/file/d/1eR3NZtwIC6ECN3vhtrynqmx8okG0twA7/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
url2 = "https://drive.google.com/file/d/1wCSAkGagMzWiToedLC3ZGo_lGf_laF-k/view?usp=sharing"
url2='https://drive.google.com/uc?id=' + url2.split('/')[-2]
kaggle.api.authenticate ()
kaggle.api.dataset_download_files(
    'shivamb/netflix-shows',
    path='data/raw/', unzip=True)
TEMP_ANNUAL = pd.read_csv('https://raw.githubusercontent.com/datasets/global-temp/main/data/annual.csv')
TEMP_ANNUAL.to_csv("data/raw/temp_annualy.csv", index=False)
TEMP_MONTHLY = pd.read_csv("https://raw.githubusercontent.com/datasets/global-temp/main/data/monthly.csv")
TEMP_MONTHLY.to_csv("data/raw/temp_monthly.csv", index=False)

def load_data(url: str, local_path: str) -> pd.DataFrame:
    if os.path.exists(local_path):
        print(f'Loading from cache: {local_path}')
        return pd.read_csv(local_path)

    print(f'Downloading from {url} ...')
    df = pd.read_csv(url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    df.to_csv(local_path, index=False)
    print(f'Saved to {local_path}')
    return df

df = load_data(url2, 'data/raw/chess_players.csv')
df = load_data(url, 'data/raw/chess_games.csv')


dfg = pd.read_csv("data/raw/chess_games.csv", encoding='latin1')
dfp = pd.read_csv("data/raw/chess_players.csv", encoding='latin1')


def clean_function_games(dfg,local_path):
    dfg[['time_base', 'time_inc']] = dfg['time_increment'].str.split('+', expand=True).astype(int)
    dfg['rating_diff'] = dfg['white_rating'] - dfg['black_rating']
    dfg['opening_family'] = dfg['opening_fullname'].str.split(':').str[0].str.strip()
    dfg = dfg.drop(columns=['opening_response'])
    dfg['is_suspicios'] = dfg['turns'] < 5
    assert dfg['rating_diff'].notna().all()
    assert dfg.duplicated().sum() == 0
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    dfg.to_csv(local_path, index=False)
    print(f'Saved to {local_path}')
    return  dfg
clean_function_games(dfg,"data/raw/chess_games.csv")