import twint


def fetch_tweets(username):
    client = twint.Config()
    client.Username = username
    client.Store_csv = True
    client.Output = username + ".csv"

    twint.run.Search(client)


if __name__ == "__main__":
    print("Tweet Scraper for Clinify-Open-Sauce by Shubhayu Majumdar")
    harish = "curiousharish"
    shreyans = "Shreyans_23"

    fetch_tweets(harish)
    fetch_tweets(shreyans)
