#!/usr/bin/env python

import sys
import os
import requests
from ConfigParser import ConfigParser

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        sys.exit("Please install the simplejson library or upgrade to Python 2.6+")

def find_config():
    config = ConfigParser()
    files = config.read(['.pushover',os.path.expanduser('~/.pushover')])
    if not files:
        sys.exit("No Configuration ( .pushover ) found")
    conf = { 'app_key': config.get('pushover','app_key'),
             'user_key': config.get('pushover','user_key')}
    return conf

def send_message(conf,message):
    # mild sanity check on the message
    if len(message) > 512:
        sys.exit("message too big")
    payload = {
            'token': conf['app_key'],
            'user' : conf['user_key'],
            'message': message,
    }
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload )
    if not r.status_code == requests.codes.ok:
        print r.headers
    
                      
if __name__=='__main__':
    c = find_config()
    send_message(c,"This is a test message")
    
