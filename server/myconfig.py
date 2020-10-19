#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime 

servers = {
    '0.220':{
        'desc': '数据备份, PXE服务, Centos repo',
        'type': 'BareMetal', 
        'name': 'Backup', 
        'host': '172.16.0.220', 
        'os': 'CentOS 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.221':{
        'desc': 'repo proxy, docker repo, 数据备份镜像, kvm宿主机',
        'type': 'BareMetal', 
        'name': 'Repos', 
        'host': '172.16.0.221', 
        'os': 'CentOS 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'nexus':{
        'desc': 'nexus 服务',
        'type': '&nbsp;&nbsp;├ Service', 
        'name': 'Nexus', 
        'host': '172.16.0.221', 
        'os': 'CentOS 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.57':{
        'desc': 'nas备份',
        'type': '&nbsp;└ VirtualMachine', 
        'name': 'NasBackup', 
        'host': '172.16.0.57', 
        'os': 'DSM 6.1.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '75.223':{
        'desc': '应用开发宿主机',
        'type': 'BareMetal', 
        'name': 'DevEnv', 
        'host': '172.16.75.223', 
        'os': 'Esxi 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '75.249':{
        'desc': '测试用宿主机',
        'type': 'BareMetal', 
        'name': 'TestEnv', 
        'host': '172.16.75.249', 
        'os': 'Esxi 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '2.247':{
        'desc': 'IT虚拟环境',
        'type': 'BareMetal', 
        'name': 'IT0', 
        'host': '192.168.2.247', 
        'os': 'Esxi 6.5', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.58':{
        'desc': 'yapi',
        'type': '&nbsp;&nbsp;├&nbsp;  VirtualMachine', 
        'name': 'Yapi', 
        'host': '172.16.0.58', 
        'os': 'CentOS 7.4', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.239':{
        'desc': '远程映射跳板机',
        'type': '&nbsp;└ VirtualMachine', 
        'name': 'Jump', 
        'host': '172.16.0.239', 
        'os': 'CentOS 7.4', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '2.248':{
        'desc': 'IT虚拟环境',
        'type': 'BareMetal', 
        'name': 'IT1', 
        'host': '192.168.2.248', 
        'os': 'Esxi 6.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.55':{
        'desc': 'nas, dns, chat',
        'type': '&nbsp;&nbsp;├ VirtualMachine', 
        'name': 'nas', 
        'host': '172.16.0.55', 
        'os': 'DSM 6.1.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.222':{
        'desc': '代码托管',
        'type': '&nbsp;&nbsp;├ VirtualMachine', 
        'name': 'gitlab', 
        'host': '172.16.0.222', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.11':{
        'desc': '局域网对外网关',
        'type': '&nbsp;&nbsp;├ VirtualMachine', 
        'name': 'pfsense_gw', 
        'host': '172.16.0.11', 
        'os': 'FreeBSD', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '2.10':{
        'desc': '办公网到研发网网关',
        'type': '&nbsp;&nbsp;├ VirtualMachine', 
        'name': 'pfsense', 
        'host': '192.168.2.10', 
        'os': 'FreeBSD', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    '0.235':{
        'desc': 'IT 容器',
        'type': '&nbsp;└  VirtualMachine', 
        'name': 'DockerHome', 
        'host': '172.16.0.235', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'dockerhome':{
        'desc': 'docker服务',
        'type': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Service', 
        'name': 'DockerServices', 
        'host': '172.16.0.235', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'mysql':{
        'desc': 'mysql in docker',
        'type': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├ Container', 
        'name': 'mysql', 
        'host': '172.16.0.235', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'pm':{
        'desc': '研发bug库',
        'type': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├ Container', 
        'name': 'pm', 
        'host': 'pm.csdev.com', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'pm2':{
        'desc': '研发项目管理',
        'type': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├ Container', 
        'name': 'pm2', 
        'host': 'pm2.csdev.com', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
    'wiki':{
        'desc': '研发文档库',
        'type': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Container', 
        'name': 'Confluence', 
        'host': 'wiki.csdev.com', 
        'os': 'CentOS 7.7', 
        'latency': 1000,
        'service': { 'variant': 'success', 'value': 10 },
        'ts': datetime.now(),
        'tdiff': 0,
        '_rowVariant': ''
    },
}

datas = []