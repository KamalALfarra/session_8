# Session 8

This is the coursework for session number 8. Running the `main.py` 
file will generate the figures in the designated folder (`data/plot`).
If there is no data available, it can be generated through the 
`fetch_and_clean.py` file, which downloads and cleans the data 
into its designated folder (`data/raw`).

## Findings:

The first finding I noticed in the Netflix dataset, from the figure 
`Q4-3_Netflix_Staked_bar.png`, is that there was a drop in the 
number of TV shows and movies added in late 2020 and 2021. This could be related to 
the impact of the Coronavirus pandemic, which caused production 
delays for many shows and movies.

The second finding is from the temperature dataset in the figure 
`Q3_temp_year.png`, which shows an obvious increase in average temperature 
throughout the decades. This clearly indicates that global temperatures are warming a
nd that climate change is still a problem and a challenge facing humanity.

The third finding in the chess dataset is from the first figure 
`Q1_Average_turns`. I noticed that the average number of turns for 
mate endings and resignations are extremely close, somewhere between 60 and 80. 
This suggests that many chess games in the dataset tend to end around this range, 
while games that continue longer may have a higher chance of 
ending in a draw, as seen in the out-of-time status.

One last note about the random player rating figure: it generates a random player each time 
the code runs and adjusts the figure to match their minimum and maximum rating 
for better visualization.
