#file for headlines project

import feedparser
from flask import Flask
from flask import render_template


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
        return render_template("home.html", articles=feed['entries'])

    except:
        return "no news is good news"

if __name__ == '__main__':
    app.run(port=5000, debug = True)
