# twitter-consummer 

Docker image with a simple twitter consumer that listens for a list of keywords and sends tweets to a Apachee Kafka topic. 

## Uso

You have to specify a configuration file with the parameters for the consumer (JSON):

```
  {
    "kafka_server": "kafka:9092",
    "consumer_token": "CONSUMER_TOKEN",
    "consumer_secret":  "CONSUMER_SECRET",
    "access_token": "ACCESS_TOKEN"
    "access_token_secret" : "ACCESS_TOKEN_SECRET",
    "keywords": ["keyword1", "keyword2",...]
    "languages": ["en", "es", ...],
    "kafka_topic": "test"
} 
```

Then you just have to run it:

	docker run --rm -it -v $(pwd)/:/work/ enriquegrodrigo/twitter-consumer config.json 

