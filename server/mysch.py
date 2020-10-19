# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
import time
import json
import urllib.request
from utils import *
from tcp_latency import measure_latency
from datetime import datetime 
import docker

def mypost(body):
	try:
		# body = {"who":"2.247","cpu":6,"memory":3,"disk":5} 
		myurl = "http://127.0.0.1:5000/update"

		req = urllib.request.Request(myurl)
		req.add_header('Content-Type', 'application/json; charset=utf-8')
		jsondata = json.dumps(body)
		jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
		req.add_header('Content-Length', len(jsondataasbytes))
		response = urllib.request.urlopen(req, jsondataasbytes)
		return response.status
	except:
		return 404

def test_ping(who, stype, host):
	delay = 1000
	my_post_body={'who':who, 'type':stype, 'latency':delay}
	while True:
		# ping server
		delay = do_one_ping(host)

		# write latency to post data
		my_post_body['latency'] = delay

		# post to rest API
		ret = mypost(my_post_body)
		if (ret) != 200:
			print('rest service error [%d]'%ret, file=sys.stderr)
		if stype == 'ping' and delay == 1000:
			continue
		time.sleep(0.9)

def test_tcp(who, stype, host, port):
	delay = 1000
	my_post_body={'who':who, 'type':stype, 'latency':delay}
	while True:
		# ping server
		try:
			delay_ar = measure_latency(host=host, port=port, wait=0)
			delay = round(delay_ar[0],3)
		except:
			delay = 1000
		# write latency to post data
		my_post_body['latency'] = delay

		# post to rest API
		ret = mypost(my_post_body)
		if (ret) != 200:
			print('rest service error [%d]'%ret, file=sys.stderr)
		if stype == 'ping' and delay == 1000:
			continue
		time.sleep(0.9)

def test_service(who, stype, host, keykey):
	delay = 1000
	my_post_body={'who':who, 'type':stype, 'latency':delay}
	while True:
		# ping server
		try:
			a=datetime.now()
			resp = urllib.request.urlopen(host).read()
			b=datetime.now()
			delay = round(((b-a).microseconds)/1000, 3)
			json_resp = json.loads(resp)
			# print(type(json_resp))
			# print(json_resp,file=sys.stderr)
			test_key = eval(keykey%json_resp)
			# print (test_key)
			if not test_key:
				delay = 1000
		except:
			delay = 1000
		# write latency to post data
		my_post_body['latency'] = delay

		# post to rest API
		ret = mypost(my_post_body)
		if (ret) != 200:
			print('rest service error [%d]'%ret, file=sys.stderr)
		if stype == 'ping' and delay == 1000:
			continue
		time.sleep(0.9)

	
	

# a = measure_latency(host='172.16.0.221', port=8081, wait=0)
def backup_server_p():
	'''
	172.16.0.220, BareMetal
	ping
	'''
	print('running')
	stype = 'ping'
	who = '0.220'
	host = '172.16.0.220'
	test_ping(who, stype, host)


def nexus_server_p():
	'''
	172.16.0.221, BareMetal
	ping
	'''
	stype = 'ping'
	who = '0.221'
	host = '172.16.0.221'
	test_ping(who, stype, host)

def nexus_services_port_p():
	'''
	172.16.0.221, nexus, Service
	tcp_ping
	'''
	stype = 'tcp_ping'
	who = 'nexus'
	host = '172.16.0.221'
	test_tcp(who, stype, host, 8081)

def nas_backup_p():
	'''
	172.16.0.57, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.57'
	host = '172.16.0.57'
	test_ping(who, stype, host)


def dev_env_p():
	'''
	172.16.75.223, BareMetal
	ping
	'''
	stype = 'ping'
	who = '75.223'
	host = '172.16.75.223'
	test_ping(who, stype, host)

def test_env_p():
	'''
	172.16.75.249, BareMetal
	ping
	'''
	stype = 'ping'
	who = '75.249'
	host = '172.16.75.249'
	test_ping(who, stype, host)

def it0_env_p():
	'''
	192.168.2.247, BareMetal
	ping
	'''
	stype = 'ping'
	who = '2.247'
	host = '192.168.2.247'
	test_ping(who, stype, host)

def yapi_p():
	'''
	172.16.0.58, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.58'
	host = '172.16.0.58'
	test_ping(who, stype, host)

def jump_p():
	'''
	172.16.0.239, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.239'
	host = '172.16.0.239'
	test_ping(who, stype, host)

def it1_env_p():
	'''
	192.168.2.248, BareMetal
	ping
	'''
	stype = 'ping'
	who = '2.248'
	host = '192.168.2.248'
	test_ping(who, stype, host)

def nas_p():
	'''
	172.16.0.55, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.55'
	host = '172.16.0.55'
	test_ping(who, stype, host)

def git_p():
	'''
	172.16.0.222, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.222'
	host = '172.16.0.222'
	test_ping(who, stype, host)

def pfsense_gw_p():
	'''
	192.168.2.204, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.11'
	host = '192.168.2.204'
	test_ping(who, stype, host)

def pfsense_p():
	'''
	172.16.0.5, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '2.10'
	host = '172.16.0.5'
	test_ping(who, stype, host)

def dockerhome_p():
	'''
	172.16.0.235, VirtualMachine
	ping
	'''
	stype = 'ping'
	who = '0.235'
	host = '172.16.0.235'
	test_ping(who, stype, host)

def docker_services_port_p():
	'''
	172.16.0.235, docker, Service
	tcp_ping
	'''
	stype = 'tcp_ping'
	who = 'dockerhome'
	host = '172.16.0.235'
	test_tcp(who, stype, host, 1219)

def mysql_port_p():
	'''
	172.16.0.235, docker, Service
	tcp_ping
	'''
	stype = 'tcp_ping'
	who = 'mysql'
	host = 'http://172.16.0.235:1219/containers/9a194e59486e/json'
	test_service(who, stype, host, '%s["State"]["Status"]!="exited"')

def pm_services_p():
	'''
	172.16.0.235, pm, Container
	curl
	'''
	stype = 'url_ping'
	who = 'pm'
	host = 'http://pm.csdev.com/projects.json'
	test_service(who, stype, host, '"projects" in %s')

def pm2_services_p():
	'''
	172.16.0.235, pm2, Container
	curl
	'''
	stype = 'url_ping'
	who = 'pm2'
	host = 'http://pm2.csdev.com/projects.json'
	test_service(who, stype, host, '"projects" in %s')

def wiki_services_p():
	'''
	172.16.0.235, wiki, Container
	curl
	'''
	stype = 'url_ping'
	who = 'wiki'
	host = 'http://wiki.csdev.com/status'
	test_service(who, stype, host, '%s["state"] == "RUNNING"')


def run_proc():
	"""子进程要执行的代码"""
	print('子进程运行中，pid=%d...' % os.getpid())  # os.getpid获取当前进程的进程号
	print('子进程将要结束...')


def run_proc1():
	test('192.168.1.1')

all_proc = [
	'backup_server_p',
	'nexus_server_p',
	'nexus_services_port_p',
	'nas_backup_p',
	'dev_env_p',
	'test_env_p',
	'it0_env_p',
	'yapi_p',
	'jump_p',
	'it1_env_p',
	'nas_p',
	'git_p',
	'pfsense_gw_p',
	'pfsense_p',
	'dockerhome_p',
	'docker_services_port_p',
	'mysql_port_p',
	'pm_services_p',
	'pm2_services_p',
	'wiki_services_p',
]

def run_all():
	for p in all_proc:
		pp = eval('Process(target=%s)'%p)
		pp.start()
	while True:
		time.sleep(60)

if __name__ == '__main__':
	# print('父进程pid: %d' % os.getpid())  # os.getpid获取当前进程的进程号
	# p = Process(target=run_proc)
	# p2 = Process(target=run_proc1)
	# p3 = Process(target=run_proc1)
	# p2.start()
	# p.start()
	run_all()
	# wiki_services_p()
