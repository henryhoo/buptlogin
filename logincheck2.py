import requests
import re
import sys

Target1='http://10.3.8.211'
def check():
    #1 connect & get
    r = requests.get(Target1)
    #find flow
    pattern = re.compile(r'(?<=flow=\')\d+')
    match = re.search(pattern, r.text)
    if match:
        checkcode = match.group()
    #return
    return match.group()
def checkmoney():
    #1 connect & get
    r = requests.get(Target1)
    #find flow
    pattern = re.compile(r'(?<=fee=\')\d+')
    match = re.search(pattern, r.text)
    if match:
        checkcode = match.group()
    #return
    return match.group()

