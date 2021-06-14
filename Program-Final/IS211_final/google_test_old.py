import os
import requests
from flask import Flask, render_template, request, redirect, session, g, url_for, flash
import sqlite3
from contextlib import closing

DATABASE = 'books.db'
SECRET_KEY = 'secret_key'
USERNAME = 'admin'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def get_db():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect('/library')
    return render_template('login.html', error=error)

@app.route('/library', methods = ['GET'])
def library():
    if session['logged_in'] == False:
        return redirect('/login')
    else:
        cur = g.db.execute('SELECT title, author, pages, rating FROM books')# order by title')
        books = [dict(title=row[0], author=row[1], pages=row[2], rating=row[3]) for row in cur.fetchall()]
        return render_template('library.html', books = books)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    if session['logged_in'] == False:
        return redirect('/login')
    else:
        if request.method == 'POST':
            print ('Searching')
            find = (request.form['booksearch'])
            gbooks().booksearch(find)


        if request.method == 'GET':
            print('Getting')

        return render_template('search.html')


class gbooks():
    def __init___(self, value):
                self.title = title

    def booksearch(self, value):
        parms = {"q":value}
        print parms
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print (r.url)
        rj = r.json()
        for i in (rj['items']):
            try:
                title = (i['volumeInfo']['title'])
            except Exception as e:
                print (e)
            try:
                subtitle = (i['volumeInfo']['subtitle'])
            except Exception as e:
                subtitle = None
            try:
                author = (i['volumeInfo']['authors'])
            except Exception as e:
                print (e)
            try:
                pageCount = (i['volumeInfo']['pageCount'])
            except Exception as e:
                print (e)
            try:
                rating = (i['volumeInfo']['averageRating'])
            except Exception as e:
                print (e)
            try:
                thumbnail = i['volumeInfo']['imageLinks']['thumbnail']
            except Exception as e:
                print (e)
            print (title,  author, '\n')
            return render_template('search.html', title=title)

if __name__ == "__main__":
    app.run(debug = True)
    connect_db()
