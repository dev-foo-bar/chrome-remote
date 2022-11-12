#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import os, subprocess, threaing
import sys
import json
import requests
from websocket import create_connection

CHROME_REMOTE_DEBUG_PORT="12345"

def print_help():
    print("Usage: "+sys.argv[0]+" [ -h ] | [ -p <chrome-remote-port>] <url_to_open> | refresh ")
    print("")
    print(" This programm requires chrome/chromium browser. Start this with the following argument: ")
    print(" chromium -remote-debugging-port=12345")
    print("") 
    print(" -p remote debugging port (default is 12345)")
    print(" ")
    print(" <url_to_open> e.g. https://www.heise.de")
    print(" OR")
    print(" refresh")
    print("")

# {"id": 1, "method": "Page.navigate", "params": { "url": "https://www.heise.de"} }
def create_request( my_url ):
    url_request = json.loads("{}")
    url_request['url'] = my_url
    
    final = json.loads("{}")
    final['id'] = 1
    final['method'] = "Page.navigate"
    final['params'] = url_request

    return json.dumps(final, indent=4)


# {"id": 1, "method": "Page.reload", "params": {"ignoreCache": true} }
def create_refresh():
    url_request = json.loads("{}")
    url_request['ignoreCache'] = True
    
    final = json.loads("{}")
    final['id'] = 1
    final['method'] = "Page.reload"
    final['params'] = url_request

    return json.dumps(final, indent=4)
 
def open_url( ws_json_request, chrome_port ):
    debug_json_url = "http://localhost:"+str(chrome_port)+"/json"
    try:
        response = requests.get(debug_json_url)
    except:
        print("Browser not reachable on port "+str(chrome_port))
        raise SystemExit()

    for page in response.json():
            if  page['type'] == 'page':
                # print(page['url'])
                # print(page['webSocketDebuggerUrl'])    
                ws = create_connection(page['webSocketDebuggerUrl'])
                # url_json = create_request( my_url )
                # print(url_json)
                ws.send(ws_json_request)
                ws.close()               


if len(sys.argv) < 2:
    print_help()
    exit(1)
else:
    chromeport = CHROME_REMOTE_DEBUG_PORT
    i = 1
    while i<len(sys.argv):
        if sys.argv[i] == "-h":
            print_help()
            exit(1)
        elif (sys.argv[i] == "-p"):
            try:
                chromeport = int(sys.argv[i+1])                
                i = i+1
            except:
                print_help()
                raise SystemExit()
        elif (sys.argv[i] == "refresh"):
            ws_request = create_refresh()
        elif (sys.argv[i].startswith("http://") | sys.argv[i].startswith("https://")):
            ws_request = create_request(sys.argv[i])
        else:
            print_help()
            exit(1)        
      
        i = i+1

# print(ws_request)
# print(chromeport)

if ws_request:
    open_url(ws_request, chromeport)