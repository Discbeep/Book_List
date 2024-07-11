from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://openlibrary.org/search.json?q=the+lord+of+the+rings')
    books = response.json()['docs'][:10]  # Get the first 10 books

    return render_template('index.html', books=books)

@app.route('/book/<book_id>')
def book_details(book_id):
    response = requests.get(f'http://openlibrary.org/books/{book_id}.json')
    book = response.json()

    return render_template('details.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)