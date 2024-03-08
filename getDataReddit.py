import praw
import requests
import time
import csv


#creds constant
CLIENT_ID = "S-V6chA1resmTNB2N7mfkw"
CLIENT_SECRET = "JHU-fb5mY_vnzuOQ7-hgHBD7yiGQ6w"
USER_AGENT = "crypto data bot 101 (by u/unixparadox)"
USERNAME = "unixparadox"
PASSWORD = "numbers4799"


session = requests.Session()

#---------------------------crypto work------------------------------#



cryptoSubReddits = ['ethtrader', 'cryptocurrency', 'Bitcoin', 'altcoin', 'cryptocurrencies', 'cryptocurrencies', 'cryptocurrencytrading', 
                    "CryptoMarkets", "Crypto_General", "Web3"]

cryptoSubRedditsTest = ['ethtrader', 'cryptocurrency']



#gets data from above subreddits
def get_content():
    data_list = []

    #initializing reddit object
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT,
        password = PASSWORD,
        username = USERNAME, ratelimit_seconds=300)

    print("Welcome:  " + str(reddit.user.me()))

    for cryptoSub in cryptoSubRedditsTest:
        print("Requested Subreddit   ---->   "+cryptoSub)
        subreddit = reddit.subreddit(cryptoSub)
        topSubreddit = subreddit.top(limit=5)

        for subs in topSubreddit:
            if not subs.stickied:
                subs.comment_limit = 10
                comments_placehoolder =[]
                #to get top comments from a post
                for comment in subs.comments:
                    if isinstance(comment, praw.models.Comment):
                        comments_placehoolder.append(comment.body)
                
                # data dict to store the extracted data
                data = {'Title': subs.title,
                        "Author": subs.author,      
                        "Subreddit": subs.subreddit,
                        "URL": subs.url,
                        "Created Time": subs.created_utc,
                        "Vote Count": subs.score,
                        "Number of Comments": subs.num_comments,
                        "Number of comments Extracted": len(comments_placehoolder),
                        "Comments": comments_placehoolder
                }
                
                #appending the global data_list with this iteratiosns data
                data_list.append(data)

                # printing everything except comments item from data dictionary
                data = list(data.items())
                print(data[:8])
                
                
                
                time.sleep(2)

    return data_list            



#saves the collected data from subreddits into a csv file
def save2csv(data_list):
    csv_headers = ['Title', 'Author', 'Subreddit', 'URL', 'Created Time', 'Number of Comments', 'Vote Count', 'Number of comments Extracted', 'Comments']
    with open('cryptodata.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)



if __name__ == "__main__":
    data_list = []
    data_list = get_content()
    save2csv(data_list)
    

    



    
