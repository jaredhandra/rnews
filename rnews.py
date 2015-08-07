from flask import Flask, render_template
import praw

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = praw.Reddit(user_agent='news_reader')
    submissions = r.get_subreddit('news').get_hot(limit=30)
    count = 0
    posts = []
    title = "Yay Title"
    for sub in submissions:
        count += 1
        new_post = {"title":sub.title, "ups":sub.ups, "url":sub.url, "count":count}
        posts.append(new_post)
    return render_template("index.html", posts=posts, title=title)

if __name__ == '__main__':
    app.run()
