#file for headlines project

import feedparser
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

RSS_Feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
                 'cnn' : 'http://rss.cnn.com/rss/edition.rss',
                 'iol' : 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")



# @app.route("/<publication>") commented out when adding HTTP GET

def get_news(publication = "bbc"):
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_Feeds:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_Feeds[publication])

    try:
        #print (first_article)
        return render_template("home.html", articles=feed['entries'])

    except:
        return "no news is good news"

if __name__ == '__main__':
    app.run(port=5000, debug = True)
