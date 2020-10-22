#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
import random
import sys
from myconfig import *

import urllib.request
import json
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
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
DEBUG = False
g_update_ts_flag = False
g_executor = ThreadPoolExecutor(1)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def send_warnning(server, wtype):
    if wtype:
        ot = '可能挂了'
    else:
        ot = '恢复了'
    global DEBUG

    print(server+" "+ot,file=sys.stderr)
    if DEBUG:
        return
    body= {
        "msgtype": "text",
        "text": {
            "content": "服务器<{}>{}".format(server, ot),
            "mentioned_list": ["@all"]
        },
    }

    # try:
    myurl = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=71c5a100-115f-4388-b168-e50a3aa93e5c"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondataasbytes = json.dumps(body)
    jsondataasbytes = jsondataasbytes.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
    return response.status
    # except:
    #     return 404

def udpate_ts():
    ts_val = datetime.now()
    for d in servers:
        old_ts_val = servers[d]['ts']
        tdiff = (ts_val - old_ts_val).seconds
        servers[d]['tdiff'] = tdiff

def prt(strs):
    print (strs, file=sys.stderr)

# 有post请求
def update_para(who, post_data):
    
    if(post_data.get('latency') == 1000):
        # print("offline: %d"%servers[who]['offline'], file=sys.stderr)
        # 当前post提交的延时为1000
        if servers[who]['_rowVariant']!='danger' and servers[who]['offline'] == 0: 
            servers[who]['offline'] = 1
            srv = '{}({})'.format(servers[who]['host'], who)
            send_warnning(srv, True)
        servers[who]['_rowVariant']='danger'
        servers[who]['latency']=1000
        servers[who]['offline'] = servers[who]['tdiff'] 
        return 'error'
    else:
        servers[who]['_rowVariant']=''
        if servers[who]['latency'] == 1000 and servers[who]['offline'] > 10:
            srv = '{}({})'.format(servers[who]['host'], who)
            send_warnning(srv, False)

    # print(post_data, file=sys.stderr)
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    ts_val = datetime.now()
    # old_ts_val = servers[who]['ts']
    try:
        servers[who]['latency']=post_data.get('latency')
        servers[who]['ts']=ts_val
        servers[who]['offline'] = 0

        return 'success'
    except:
        return 'error'

def update_datas_routine():
    print ("Task <update_ts> started!", file=sys.stderr)
    # print("Task <update_ts> started!")
    while True:
        udpate_ts()
        time.sleep(2)

@app.route('/updatets', methods=['GET'])
def run_jobs():
    global g_update_ts_flag
    global g_executor
    response_object = {'status': 'success'}
    if g_update_ts_flag:
        print ("Task <update_ts> already started!", file=sys.stderr)
        return jsonify(response_object)
    g_update_ts_flag = True
    g_executor.submit(update_datas_routine)
    return jsonify(response_object)

@app.route('/update', methods=['POST'])
def udpate_datas():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    # print(post_data, file=sys.stderr)
    
    who = post_data.get('who')
    if who in servers:
        ret = update_para(who, post_data);
        response_object['status'] = ret
    # print (post_data, file=sys.stderr)
    return jsonify(response_object)

def get_bar_color(v):
    if v < 5:
        return 'success'
    else :
        if v <10:
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