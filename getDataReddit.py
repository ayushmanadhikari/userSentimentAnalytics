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







# # we could get a bunch of information about this submission/subreddit post
# dataESub = reddit.subreddit('dataengineering')
# dataE = dataESub.hot(limit=5)
# for submission in dataE:
#     if not submission.stickied:
#         print(submission.title, "\n", submission.ups, "\n", submission.downs, "\n", submission.visited)

# for submission in reddit.subreddit("test").hot(limit=10):
#     print(submission.title)


#---------------------------crypto work------------------------------#



cryptoSubReddits = ['ethtrader', 'cryptocurrency', 'Bitcoin', 'altcoin', 'cryptocurrencies', 'cryptocurrencies', 'cryptocurrencytrading', 
                    "CryptoMarkets", "Crypto_General", "Web3"]

cryptoSubRedditsTest = ['ethtrader', 'ryptocurrency']

data_list = []

def get_content():
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
        hotSubreddit = subreddit.top(limit=10)

        for subs in hotSubreddit:
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
                        "Comments": subs.num_comments,
                        "Vote Count": subs.score,
                        "Comments": comments_placehoolder
                }
                print(data)
                #appending the global data_list with this iteratiosns data
                data_list.append(data)
                
                time.sleep(2)
                



def save2csv():
    csv_headers = ['Title', 'Author', 'Subreddit', 'URL', 'Created Time', 'Number of Comments', 'Vote Count', 'Comments']
    with open('cryptodata', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)



if __name__ == "__main__":
    data_list = get_content()
    

    



    
