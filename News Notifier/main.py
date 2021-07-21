import slack
import base64
import requests
import time
import config
import base64


class news_notifier:
    def __init__(self):
        self.news_src = "https://newsapi.org/v2/top-headlines?country=in&apiKey="
        self.news_api = base64.b64decode(config.news_key).decode("ascii")
        self.client = slack.WebClient(
            base64.b64decode(config.slack_token).decode("ascii"))

        self.fetch_news()
        time.sleep(5)
        self.filter_news()

    def fetch_news(self):
        self.response = requests.get(self.news_src + self.news_api).json()
        if(self.response['status'] == 'ok'):
            pass
        else:
            print(
                f"Error: {self.response['code']}.\nSee for: {self.response['message']}")

    def post_news(self):
        self.client.chat_postMessage(
            channel="#news-notifications", blocks=[
                {
                    "type": "section",
                    "block_id": "news",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"<{self.news['redirect']}|{self.news['title']}> \nSource: {self.news['src']} \n{self.news['description']}"},
                    "accessory": {
                        "type": "image",
                        "image_url": self.news['image'],
                        "alt_text": "News Image",
                    },
                }]
        )

    def filter_news(self):
        all_news = self.response['articles']
        for data in all_news:
            self.news = {
                'title': data['title'], 'image': data['urlToImage'], 'description': data['description'], 'redirect': data['url'], 'src': data['source']['name']}
            self.post_news()
            time.sleep(30)


if __name__ == "__main__":
    print("SPRINT News Notifier => Shubhayu Majumdar")
    session = news_notifier()
