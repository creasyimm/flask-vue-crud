import uuid
import random

from flask import Flask, jsonify, request
from flask_cors import CORS

datas = [
    {'type': 'BareMetal', 'name': 'TestEnv', 'host': '172.16.75.249', 'os': 'Esxi 6.7', 'cpu': 0.6, 
      'memory': 0.3, 'disk': 0.5, 'service': { 'variant': 'success', 'value': 10 }},
    {'type': 'BareMetal', 'name': 'DevEnv', 'host': '172.16.75.223', 'os': 'Esxi 6.7', 'cpu': 0.6, 
      'memory': 0.3, 'disk': 0.5, 'service': { 'variant': 'warning', 'value': 30 }},
    {'type': 'BareMetal', 'name': 'TestEnv', 'host': '172.16.75.249', 'os': 'Esxi 6.7', 'cpu': 0.6, 
      'memory': 0.3, 'disk': 0.5, 'service': { 'variant': 'success', 'value': 10 }},
    {'type': 'BareMetal', 'name': 'DevEnv', 'host': '172.16.75.223', 'os': 'Esxi 6.7', 'cpu': 0.6, 
      'memory': 0.3, 'disk': 0.5, 'service': { 'variant': 'warning', 'value': 30 }}
]

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'price': '1.1',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'price': '1.2',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'price': '1.3',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/datas', methods=['GET', 'POST'])
def all_datas():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        response_object['message'] = 'wtf!'
    else:
        for dt in datas:
            dt['service']['value'] = random.randint(0,100)
        response_object['datas'] = datas
    return jsonify(response_object)

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'price': post_data.get('price'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'price': post_data.get('price'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()