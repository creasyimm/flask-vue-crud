#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
import random
import sys
from myconfig import *

from flask import Flask, jsonify, request
from flask_cors import CORS
import time

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

def udpate_ts():
    ts_val = datetime.now()
    for d in servers:
        old_ts_val = servers[d]['ts']
        tdiff = (ts_val - old_ts_val).seconds
        servers[d]['tdiff'] = tdiff

def prt(strs):
    print (strs, file=sys.stderr)

def update_para(who, post_data):
    servers[who]['_rowVariant']=''
    if(post_data.get('latency') == 1000):
        servers[who]['_rowVariant']='danger'
        servers[who]['latency']=1000
        return 'error'
    print(post_data, file=sys.stderr)
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    ts_val = datetime.now()
    # old_ts_val = servers[who]['ts']
    try:

        # servers[who]['cpu'] = float(post_data.get('cpu'))
        # servers[who]['memory'] = float(post_data.get('memory'))
        # servers[who]['disk'] = float(post_data.get('disk'))
        # print (post_data)
        servers[who]['latency']=post_data.get('latency')
        servers[who]['ts']=ts_val
        return 'success'
    except:
        return 'error'

@app.route('/update', methods=['POST'])
def udpate_datas():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print(post_data, file=sys.stderr)
    
    who = post_data.get('who')
    if who in servers:
        ret = update_para(who, post_data);
        response_object['status'] = ret
    # print (post_data, file=sys.stderr)
    return jsonify(response_object)

def get_bar_color(v):
    if v < 2:
        return 'success'
    else :
        if v <5:
            return 'warning'
        else:
            return 'danger'

@app.route('/datas', methods=['GET', 'POST'])
def all_datas():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        response_object['message'] = 'wtf!'
    else:
        # for dt in datas:
        #     rvalue = random.randint(0,100)
        #     dt['service']['value'] = rvalue
        #     dt['service']['variant'] = get_bar_color(rvalue)
        udpate_ts()
        datas = []
        for k in servers:
            rvalue = servers[k]['tdiff']
            servers[k]['service']['variant'] = get_bar_color(rvalue)
            servers[k]['service']['value'] = (servers[k]['latency']/30)*100
            datas.append(servers[k])
        response_object['datas'] = datas
    return jsonify(response_object)


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
    app.run(host = '0.0.0.0')