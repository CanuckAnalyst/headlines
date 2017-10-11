#file for headlines project

import feedparser
from flask import Flask


app = Flask(__name__)

RSS_Feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
                 'cnn' : 'http://rss.cnn.com/rss/edition.rss',
                 'iol' : 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")


@app.route("/<publication>")

def get_news(publication = "bbc"):
    feed = feedparser.parse(RSS_Feeds[publication])

    first_article = feed['entries'][0]

    try:
        #print (first_article)
        return"""<html>
            <body>
                <h1> Headlines </h1>
                <b>{0}</b><br/>
                <i>{1}</i><br/>
                <p>{2}</p><br/>
            </body>
        </html>""".format(first_article.get("title"),
                          first_article.get("published"),
                          first_article.get("summary"))
    except:
        return "no news is good news"

if __name__ == '__main__':
    app.run(port=5000, debug = True)
