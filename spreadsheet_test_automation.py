# encoding: utf-8
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
import csv
import requests
import json
from jinja2 import Template
from progress.bar import ChargingBar
import webbrowser
import os

htmlFile = sys.argv[2]
fileCsv = open(sys.argv[1], "rb")
out = open(htmlFile, "w")
domain = sys.argv[3]
cantOfCases = int(sys.argv[4])

template = open('template.txt', 'r')
data = ""
with template as tem:
    data = Template(tem.read().replace('\n', ''))

def formatHeaders(headers):
    listHeaders = headers.split(',')
    for headerIndex in range(0,len(listHeaders)):
        keyValue = listHeaders[headerIndex].split(':')
        for keyValueIndex in range(0, len(keyValue)):
             keyValue[keyValueIndex] = '"' + keyValue[keyValueIndex] + '"'
        listHeaders[headerIndex] = ':'.join(keyValue)
    return "{" + ','.join(listHeaders) + "}"
    

# Line -> [caso, objetivo, que se espera, metodo, url prod, headers, body]
with  fileCsv as f:
    reader = csv.reader(f, delimiter="\t") 
    bar = ChargingBar('Processing', max=cantOfCases)
    for i, line in enumerate(reader):
        if i != 0:
            bar.next()
            method = line[3]
            url = domain + line[4].split("[URL]")[1]
            headers = json.loads(formatHeaders(line[5]))
            body = line[6]

            if method == "GET":
                r = requests.get(url)
            elif method == "POST":
                r = requests.post(url, body, headers)
            elif method == "PUT":
                r = requests.put(url, body)
           
            out.write(data.render(expected=line[2], response=r.text))
    bar.finish()
    webbrowser.open('file://' + os.path.realpath(htmlFile));