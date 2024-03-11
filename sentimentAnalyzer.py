#performs sentiment analysis on the extracted reddit data
#gives polarity scoring for each extracted comments, post and subreddit as a whole

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



#defined constants
CSVFILENAME = "data/cryptodata.csv"




#this function takes a sentence as an input and returns a pandas dataframe with its polarity score
def sentimentAnalyzer(sentence):
    #creating SentimentIntensityAnalyzer object which perform analysis to return polarity score for each sentence 
    sid = SentimentIntensityAnalyzer()
    sentimentScoresDict = sid.polarity_scores(sentence)
    return sentimentScoresDict




#takes the output dictionary from sentimentAnalyzer and returns the sentiment keyword for that dict/sentence
#polarityscore output dict --> polarity keyword
def sentimentKeywordOutput(outputDict):
    polarity = "neutral"
    if(outputDict['compound']>= 0.05):
        polarity = "positive"
    elif(outputDict['compound']<= -0.05):
        polarity = "negative"
    return polarity



#this function gets the reddit data from the csv file and returns a pandas dataframe containing the data
#null --> dataframe
def getRedditData():
    df = pd.read_csv(CSVFILENAME)
    if not df.empty:
        print("Data imported successfully.... \n")
    return df



#main function
if __name__=="__main__": 
    redditDF = getRedditData()
    totalList = []
    scoreDict = {'Title Compound Score':[], 'Title Compound Keyword':[] }
    #pass every 'title' row(sentence) to sentimentAnalyzer to get polarity compound score
    for sentence in redditDF['Title']:
        sentimentScoreDict = sentimentAnalyzer(sentence)
        sentimentKeyword = sentimentKeywordOutput(sentimentScoreDict)
        scoreDict['Title Compound Score'].append(sentimentScoreDict['compound'])
        scoreDict['Title Compound Keyword'].append(sentimentKeyword)

    
    print(scoreDict)

    redditDF['Title Compound Score'] = scoreDict['Title Compound Score']
    redditDF['Title Compound Keyword'] = scoreDict['Title Compound Keyword']
    #newDf = pd.concat([redditDF, pd.DataFrame([scoreDict])], ignore_index=True)
    print(redditDF.head(5))


    






#fields we are gonna add to the original data to perform further analysis
# title polarity score
# body polarity score
# comments polairty score
# polarity keyword