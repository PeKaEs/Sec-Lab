#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = requests.utils.default_headers()

headers.update({'User-Agent': 'pwrobot'})

with open('SendMe.py','rb') as fScript:
    sScriptContent = fScript.read()

rResponse = requests.post('https://pmlabs.net/pwr/0xfeedface/0x02/.post/', data = {'name':'Paweł Kryska','script':sScriptContent})
print rResponse.content
