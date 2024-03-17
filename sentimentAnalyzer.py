#performs sentiment analysis on the extracted reddit data
#gives polarity scoring for each extracted comments, post and subreddit as a whole

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
import ast



#defined constants
CSVFILENAME = "data/cryptodata.csv"

#cryptocurrencies with their symbols list
cryptocurrencies = ["BTC", "Bitcoin", "ETH", "Ethereum", "USDT", "Tether", "BNB", "Binance Coin", "SOL", "Solana", "XRP", "Ripple", "USDC", "USD Coin",
"ADA", "Cardano", "AVAX", "Avalanche", "DOGE", "Dogecoin", "LINK", "Chainlink", "TRX", "TRON", "DOT", "Polkadot", "MATIC", "Polygon", "TON", "TON Crystal",
"ICP", "Internet Computer", "SHIB", "Shiba Inu", "DAI", "Dai", "LTC", "Litecoin", "BCH", "Bitcoin Cash", "UNI", "Uniswap", "LEO", "UNUS SED LEO", "ATOM", "Cosmos"]



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




#analyzes a sentence to get which crypto it has mentioned
#input is sentence... output is list containing crypto name/s
def cryptoRecognizer(sentence):
    tokens = nltk.word_tokenize(sentence)
    # Identify tokens that are in the list of cryptocurrencies
    mentioned_cryptos = []
    for coin in cryptocurrencies:
        for token in tokens:
            if token.lower() == coin.lower():
                mentioned_cryptos.append(token.lower())

    return mentioned_cryptos
    



#recieves the dataframe containing title, body, comments and returns the polarity score for each (dataframe)
def getPolarityScoresnCrypto(dataframe):

    dictWithpolarityValuesnCrypto = {'Title Score':[], 'Body Score': [], 'Comments Score': [],
                                      'Title Crypto': [], 'Body Crypto': [], 'Comments Crypto': []}

    #get scores for title
    print("extracting scores for title....")
    for sentence in dataframe['Title']:
        sentimentScoreDict = sentimentAnalyzer(sentence)
        cryptosMentioned = cryptoRecognizer(str(sentence))
        dictWithpolarityValuesnCrypto['Title Score'].append(sentimentScoreDict['compound'])
        dictWithpolarityValuesnCrypto['Title Crypto'].append(cryptosMentioned)
        #print(sentimentScoreDict['compound'])


    #get scores for body
    print("extracting scores for body....")
    for sentence in dataframe['Body']:
        sentimentScoreDict = sentimentAnalyzer(str(sentence))
        cryptosMentioned = cryptoRecognizer(str(sentence))
        dictWithpolarityValuesnCrypto['Body Score'].append(sentimentScoreDict['compound'])
        dictWithpolarityValuesnCrypto['Body Crypto'].append(cryptosMentioned)
        #print(sentimentScoreDict['compound'])

    
    #get scores for comments by averaging the total number of comments
    print("extracting scores for comments....")
    #postCount = 0                  #gives the count of nth post it is currently working for
    for commentsList in dataframe['Comments']:
        totalCommentScore = 0
        avgCommentScore = 0
        count = 0
        cryptosMentionedTotal = []
        commentsList = ast.literal_eval(commentsList)
        for sentence in commentsList:
            score = sentimentAnalyzer(sentence)
            cryptosMentioned = cryptoRecognizer(str(sentence))
            cryptosMentioned = listToString(list(set(cryptosMentioned)))
            print(f"cryptosmentioned:  ",cryptosMentioned)
            totalCommentScore = totalCommentScore + score['compound']
            if score['compound'] != 0:
                count = count + 1  
            #cryptosMentioned = listToString(cryptosMentioned)
            cryptosMentionedTotal.append(cryptosMentioned)    
        avgCommentScore = totalCommentScore/count
        #splits list into sublist and again to list
        cryptosMentionedTotal = [word for item in cryptosMentionedTotal if item for word in item.split()]
        cryptosMentionedTotal = list(set(cryptosMentionedTotal))
        print(f"crypstosmentionedTotal:  ", cryptosMentionedTotal) 
        dictWithpolarityValuesnCrypto['Comments Score'].append(avgCommentScore)
        dictWithpolarityValuesnCrypto['Comments Crypto'].append((cryptosMentionedTotal))



    dataframe['Title Score'] = dictWithpolarityValuesnCrypto['Title Score']
    dataframe['Body Score'] = dictWithpolarityValuesnCrypto['Body Score']
    dataframe['Comments Score'] = dictWithpolarityValuesnCrypto['Comments Score']
    dataframe['Title Crypto'] = dictWithpolarityValuesnCrypto['Title Crypto']
    dataframe['Body Crypto'] = dictWithpolarityValuesnCrypto['Body Crypto']
    dataframe['Comments Crypto'] = dictWithpolarityValuesnCrypto['Comments Crypto']
    

    return dataframe



def listToString(someList):
    mystring = ""
    for item in someList:
        if mystring != "":
            mystring = mystring+" "+item
        else: 
            mystring = mystring + item
    return mystring



def getMentionedCryptos(dataframe):
    dictWithCryptosMentioned = {'Title Crypto': [], 'Body Crypto': [], 'Comments Crypto': []}

    for sentence in dataframe['Title']:
        cryptosMentioned = cryptoRecognizer(sentence)
        dictWithCryptosMentioned['Title Crypto'].append(cryptosMentioned)
    
    
def save2scv(dataframe):
    dataframe.to_csv('data/analyzed.csv')
    print("\n File successfully saved!")


  

#main function
if __name__=="__main__": 
    redditDF = getRedditData()
    dfWithPolarityScoresnCrypto = getPolarityScoresnCrypto(redditDF)
    save2scv(dfWithPolarityScoresnCrypto)

    #print(dfWithPolarityScores.columns)
    #print(dfWithPolarityScores[['Title Score', 'Body Score', 'Comments Score']].head())

    # sentence = "i love dailogue solitude in bitcoinish sol"
    # cryptos = cryptoRecognizer(sentence)
    # print(cryptos)




    #totalList = []
    # scoreDict = {'Title Compound Score':[], 'Title Compound Keyword':[] }

    # dfPolarityScores = getPolarityScores(redditDF)

   

    






