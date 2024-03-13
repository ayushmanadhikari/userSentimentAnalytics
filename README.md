###Project to do usersentiment analysis on different subreddits for crypto market. 

What this project does is gets Users' posts from various subreddits and performs analysis on that data to get result like polarity score and the particular crypto it is talking about in those posts' title, body and comment section. On the basis of that score it predicts if the cryptos price will go up or down. 

Another module of this project then collects the market data from a Coincap api. It performs necessary transformation and cleaning on that data before storing that data in a Kafka topic. It then uses Spark to perform further processing. And then sends the data into Elasticsearch for proper storage and time-series analysis. Finally, it visualizes the end result using Kibana. 