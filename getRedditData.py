#getRedditData.py moduling


import praw
import requests
import time
import csv
from datetime import datetime


#creds constant
CLIENT_ID = "S-V6chA1resmTNB2N7mfkw"
CLIENT_SECRET = "JHU-fb5mY_vnzuOQ7-hgHBD7yiGQ6w"
USER_AGENT = "crypto data bot 101 (by u/unixparadox)"
USERNAME = "unixparadox"
PASSWORD = "numbers4799"


TOP_LIMIT = 2
COMMENTS_LIMIT = 2



session = requests.Session()


SubReddits = ['ethtrader', 'cryptocurrency', 'Bitcoin', 'altcoin', 'cryptocurrencies', 'cryptocurrencies', 'cryptocurrencytrading', 
                    "CryptoMarkets", "Crypto_General", "Web3"]

SubRedditsTest = ['ethtrader', 'cryptocurrency']



def getTopSubredditsList():
    subs = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT,
        password = PASSWORD,
        username = USERNAME, ratelimit_seconds=300, limit_type='backoff'
    )

    subredditslist = subs.subreddits.search(query="cryptocurrency", limit=100)

    for subreddit in subredditslist:
        print(subreddit.display_name)



#takes no param but returns reddit object 
def initializeReddit():
    #initializing reddit object
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT,
        password = PASSWORD,
        username = USERNAME, ratelimit_seconds=300, limit_type='backoff')
    print("Welcome:  " + str(reddit.user.me()) + "\n")
    return reddit




def save2csv(data_list):
    csv_headers = ['Title','Body', 'Author', 'Subreddit', 'URL', 'Created Time', 'Number of Comments', 'Vote Count', 'Number of comments Extracted', 'Comments']
    with open('data/cryptodata.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)
        print("\n File successfully saved!")




#takes reddit object as param and returns list containing all the extracted data
def getData(reddit):
    totalDataList = []
    #iterates through the list of subreddits to extract the data
    for sub in SubReddits:
        print("Requested Subreddit   ---->   "+sub)
        subRedditObj = reddit.subreddit(sub)
        topSubredditObj = subRedditObj.top(limit=TOP_LIMIT)

        for submissionObject in topSubredditObj:
            if not submissionObject.stickied:
                comments = getComments(submissionObject)
                currentDataDict = getDataDict(submissionObject, comments)
                totalDataList.append(currentDataDict)
            data = list(currentDataDict.items())
            print(data[:2], "\n")
            time.sleep(2)
    
    return totalDataList


  

#retrieves and stores comments in comments placeholder
def getComments(submissionObj):
    comments_placeholder = []
    submissionObj.comment_sort = 'top'
    submissionObj.comments.replace_more(limit=COMMENTS_LIMIT)  # Set the comment limit
    for comment in submissionObj.comments.list()[:COMMENTS_LIMIT]:
        comments_placeholder.append(comment.body)

    return comments_placeholder





#returns data dictionary containing all the data fields... takes submission object and comment placeholder(list) as input
def getDataDict(submissionObj, comments_placeholder):
    data = {'Title': submissionObj.title,
            'Body': submissionObj.selftext,
            "Author": submissionObj.author,      
            "Subreddit": submissionObj.subreddit,
            "URL": submissionObj.url,
            "Created Time": submissionObj.created_utc,
            "Vote Count": submissionObj.score,
            "Number of Comments": submissionObj.num_comments,
            "Number of comments Extracted": len(comments_placeholder),
            "Comments": comments_placeholder
                }
    return data
    
    
    
    


if __name__ == "__main__":
    dataList = []
    #getTopSubredditsList()
    reddit = initializeReddit()
    dataList = getData(reddit)
    save2csv(dataList)





