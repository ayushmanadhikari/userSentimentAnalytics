import praw
import requests


#creds constant
CLIENT_ID = "S-V6chA1resmTNB2N7mfkw"
CLIENT_SECRET = "JHU-fb5mY_vnzuOQ7-hgHBD7yiGQ6w"
USER_AGENT = "crypto data bot 101"
USERNAME = "unixparadox"
PASSWORD = "numbers4799"


session = requests.Session()

reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT,
    password = PASSWORD,
    username = USERNAME
)

#using requests library.. not working condition
# url = "https://www.reddit.com/api/subreddits_by_topic"
# headers = {
#     'client_id' : CLIENT_ID,
#     'client_secret' : CLIENT_SECRET,
#     'user_agent' : USER_AGENT
# }
# response = requests.request("GET", url=url, headers=headers)
# print(response.text)

print(reddit.user.me())


for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)


