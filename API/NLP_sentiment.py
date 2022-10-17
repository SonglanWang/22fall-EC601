import requests
import twitter_streamer

url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

for tweet in twitter_streamer.tweets.data:
    querystring = {"text": tweet.text}

    # print(querystring["text"])
    headers = {
	"X-RapidAPI-Key": "7d7b82d6b7mshb2fe85d719709bcp1ec96bjsnd2db82dde21f",
	"X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)