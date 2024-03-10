#performs sentiment analysis on the extracted reddit data
#gives polarity scoring for each extracted comments, post and subreddit as a whole

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



#defined constants
CSVFILENAME = "cryptodata.csv"




#this function takes a sentence as an input and returns a pandas dataframe with its polarity score
def sentimentAnalyzer(sentence):
    #creating SentimentIntensityAnalyzer object which perform analysis to return polarity score for each sentence 
    sid = SentimentIntensityAnalyzer()




#takes the output dictionary from sentimentAnalyzer and returns the sentiment keyword for that dict/sentence
def sentimentKeywordOutput(outputDict):
    polarity = "neutral"
    if(outputDict['compound']>= 0.05):
        polarity = "positive"
    elif(outputDict['compound']<= -0.05):
        polarity = "negative"

    return polarity



#this function gets the reddit data from the csv file and returns a pandas dataframe containing the data
def getRedditData():
    df = pd.read_csv(CSVFILENAME)
    if not df.empty:
        print("Data imported successfully....")
        print("Here's sample data")
        print(df[['Title', 'URL']].head(2))

    return df



if __name__=="__main__": 
    redditDF = getRedditData()
    



#fields we are gonna add to the original data to perform further analysis
# polarity/compount score
#polarity keyword... positive, neutral negative
#