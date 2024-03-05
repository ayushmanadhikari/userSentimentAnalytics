import praw
import requests


CLIENT_ID = "S-V6chA1resmTNB2N7mfkw"
CLIENT_SECRET = "JHU-fb5mY_vnzuOQ7-hgHBD7yiGQ6w"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
session = requests.Session()


reddit = praw.Reddit(
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    user_agent = USER_AGENT
)


print(reddit.read_only)


for submission in reddit.subreddit("test").hot(limit=10):
    print(submission.title)