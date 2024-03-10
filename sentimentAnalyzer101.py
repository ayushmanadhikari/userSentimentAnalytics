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
    
    polarity = format_output(sentiment_scores)
    print(f"The sentence is {polarity}!")

    return 0

#helper function to return positive negative or neutral instead of numeric values
def format_output(output_dict):
  polarity = "neutral"
  if(output_dict['compound']>= 0.05):
    polarity = "positive"
  elif(output_dict['compound']<= -0.05):
    polarity = "negative"

  return polarity



if __name__=="__main__": 
    sent = "This is a test sentence which i strongly feel good about!!!"
    sentiment_scores(sent)
