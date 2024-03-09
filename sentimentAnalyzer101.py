from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiment_scores(sentence):
    sid = SentimentIntensityAnalyzer()

    #polarity_scores method implementing... it gives sentiment dictionary as a result
    # which contains pos,neg,neu and compound scores

    sentiment_dict = sid.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)

    # Perform VADER analysis on the sentence
    sentiment_scores = sid.polarity_scores(sentence)

    # Print the sentiment scores
    print("Sentiment Scores:")
    for key, value in sentiment_scores.items():
        print(f"{key}: {value}")


    return 0




if __name__=="__main__": 
    sent = "This is a test sentence which i strongly good about."
    sentiment_scores(sent)
