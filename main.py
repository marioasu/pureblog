import configparser
import random
import time
import os
from flask import Flask, render_template, request, send_from_directory, abort
from blog import Blog

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('blog.conf')
blog = Blog()

@app.route('/')
def index():
    return page(1)

@app.route('/pages/<page>')
def html(page):
    print('pages/{}.html'.format(page))
    return render_template('pages/{}.html'.format(page))

@app.route('/archives')
def archives():
    posts = blog.get_posts()
    entries = {}
    for post in posts:
        year = time.strftime('%Y', time.strptime(post['date'], '%Y-%m-%d'))
        if not entries.get(year):
            entries[year] = []
        entries[year].append(post)

    entries = sorted(entries.items(), key=lambda item:item[0], reverse=True)
    return render_template('archives.html', entries=entries)

@app.route('/page/<pageno>')
def page(pageno):
    pageno = int(pageno)
    data = {}
    posts = blog.get_posts()
    step = int(config.get('site', 'posts_per_page'))
    offset = (pageno - 1) * step
    data['posts'] = posts[offset:offset+step]

    if pageno>1:
        data['has_previous'] = True
        data['previous_url'] = '/page/{}'.format(pageno-1)
    else:
        data['has_previous'] = False
    if offset+step < len(posts):
        data['has_next'] = True
        data['next_url'] = '/page/{}'.format(pageno+1)
    else:
        data['has_next'] = False

    return render_template('index.html', **data)

@app.route('/post/<article>')
def post(article):
    posts = blog.get_posts()
    # posts = random.sample(posts, 10)
    prev_post, curr_post, next_post = blog.get_post(article)

    return render_template('post.html', posts=posts, curr_post=curr_post)

@app.route('/download/book/<title>')
def download_book(title):
    if request.method == 'GET':
        if os.path.isfile(os.path.join('static/books', title)):
            return send_from_directory('static/books', title, as_attachment=True)
        else:
            abort(404)

if __name__ == '__main__':
    app.run(host='0', port=8002)
