#performs sentiment analysis on the extracted reddit data
#gives polarity scoring for each extracted comments, post and subreddit as a whole

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk



#defined constants
CSVFILENAME = "data/cryptodataTest.csv"



#this function gets the reddit data from the csv file and returns a pandas dataframe containing the data
#null --> dataframe
def getRedditData():
    df = pd.read_csv(CSVFILENAME)
    if not df.empty:
        print("Data imported successfully.... \n")
    return df




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





def namedEntityRecognizer(sentence):
    tokens = nltk.word_tokenize(sentence)
    taggedTokens = nltk.pos_tag(tokens)
    entities = nltk.ne_chunk(taggedTokens)
    pass



#recieves the dataframe containing title, body, comments and returns the polarity score for each (dataframe)
def getPolarityScores(dataframe):

    dictWithpolarityValuestoAppend = {'Title Score':[], 'Body Score': [], 'Comments Score': []}

    #get scores for title
    print("extracting scores for title....")
    for sentence in dataframe['Title']:
        sentimentScoreDict = sentimentAnalyzer(sentence)
        dictWithpolarityValuestoAppend['Title Score'].append(sentimentScoreDict['compound'])
        #print(sentimentScoreDict['compound'])

    #get scores for body
    print("extracting scores for body....")
    for sentence in dataframe['Body']:

        sentimentScoreDict = sentimentAnalyzer(str(sentence))
        dictWithpolarityValuestoAppend['Body Score'].append(sentimentScoreDict['compound'])
        #print(sentimentScoreDict['compound'])

    
    #get scores for comments by averaging the total number of comments
    print("extracting scores for comments....")
    #postCount = 0                  #gives the count of nth post it is currently working for
    for commentsList in dataframe['Comments']:
        totalCommentScore = 0
        avgCommentScore = 0
        count = 0
        for sentence in commentsList:
            score = sentimentAnalyzer(sentence)
            totalCommentScore = totalCommentScore + score['compound']
            if score['compound'] != 0:
                count = count + 1           
        avgCommentScore = totalCommentScore/count
        #postCount = postCount + 1   
        #print(postCount)
        print(avgCommentScore)
        dictWithpolarityValuestoAppend['Comments Score'].append(avgCommentScore)



    dataframe['Title Score'] = dictWithpolarityValuestoAppend['Title Score']
    dataframe['Body Score'] = dictWithpolarityValuestoAppend['Body Score']
    dataframe['Comments Score'] = dictWithpolarityValuestoAppend['Comments Score']


    return dataframe



#main function
if __name__=="__main__": 
    redditDF = getRedditData()
    dfWithPolarityScores = getPolarityScores(redditDF)
    print(dfWithPolarityScores.columns)
    print(dfWithPolarityScores[['Title Score', 'Body Score', 'Comments Score']].head())


    #totalList = []
    # scoreDict = {'Title Compound Score':[], 'Title Compound Keyword':[] }

    # dfPolarityScores = getPolarityScores(redditDF)

    # #pass every 'title' row(sentence) to sentimentAnalyzer to get polarity compound score
    # for sentence in redditDF['Title']:
    #     sentimentScoreDict = sentimentAnalyzer(sentence)
    #     sentimentKeyword = sentimentKeywordOutput(sentimentScoreDict)
    #     scoreDict['Title Compound Score'].append(sentimentScoreDict['compound'])
    #     #scoreDict['Title Compound Keyword'].append(sentimentKeyword)

    
    # print(scoreDict)

    # redditDF['Title Compound Score'] = scoreDict['Title Compound Score']
    # #redditDF['Title Compound Keyword'] = scoreDict['Title Compound Keyword']
    # print(redditDF.head(5))


    






#fields we are gonna add to the original data to perform further analysis
# title polarity score
# body polarity score
# comments polairty score
# polarity keyword
# named entity 