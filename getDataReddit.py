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


    for cryptoSub in cryptoSubReddits:
        print("Requested Subreddit   ---->   "+cryptoSub)
        subreddit = reddit.subreddit(cryptoSub)
        topSubreddit = subreddit.top(limit=20)

        for submissionPost in topSubreddit:
            if not submissionPost.stickied:

                # Create a list to store comments and set necessary conditions
                comments_placeholder = []
                submissionPost.comments.replace_more(limit=10)  # Set the comment limit to 5
                submissionPost.comment_sort = 'top'
                
                # Retrieve and store comments in comments_placeholder
                for comment in submissionPost.comments.list()[:10]:          #adjust this number to set the number of comments being stored
                    comments_placeholder.append(comment.body)


                # data dict to store the extracted data
                data = {'Title': submissionPost.title,
                        'Body': submissionPost.selftext,
                        "Author": submissionPost.author,      
                        "Subreddit": submissionPost.subreddit,
                        "URL": submissionPost.url,
                        "Created Time": submissionPost.created_utc,
                        "Vote Count": submissionPost.score,
                        "Number of Comments": submissionPost.num_comments,
                        "Number of comments Extracted": len(comments_placeholder),
                        "Comments": comments_placeholder
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
    csv_headers = ['Title','Body', 'Author', 'Subreddit', 'URL', 'Created Time', 'Number of Comments', 'Vote Count', 'Number of comments Extracted', 'Comments']
    with open('cryptodata.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)


#main function
if __name__ == "__main__":
    data_list = []
    data_list = get_content()
    save2csv(data_list)
    

    



    
