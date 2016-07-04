#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket
import time
import base64
import sys
import struct
import json
from optparse import OptionParser

usage = """This is a simple tool to manipulate TP-Link HS100 devices

%prog <on|off|query|meter> [options]

on:    turns on the device
off:   turns off the device
query: queries the device for general information
meter: queries the device for power usage information"""

parser = OptionParser(usage=usage)
parser.add_option("--ip", dest="ip",
                  help="IP address to query", metavar="IPADDR")

parser.add_option("--port", dest="port", default=9999, type="int",
                  help="PORT to query on the IP (default %default)", metavar="PORT")

(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("Incorrect number of arguments")
if not options.ip:
    parser.error("IP address was not given")

# base64 encoded data to send to the plug to switch it on
payload_on="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="

# base64 encoded data to send to the plug to switch it off
payload_off="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="

# base64 encoded data to send to the plug to query it
payload_query="AAAAI9Dw0qHYq9+61/XPtJS20bTAn+yV5o/hh+jK8J7rh+vLtpbr"

# base64 encoded data to query emeter - hs100 doesn't seem to support this in hardware, but the API seems to be there...
payload_emeter="AAAAJNDw0rfav8uu3P7Ev5+92r/LlOaD4o76k/6buYPtmPSYuMXlmA=="

def recv_size(the_socket):
    #data length is packed into 4 bytes
    total_len=0;total_data=[];size=sys.maxint
    size_data=sock_data='';recv_size=8192
    while total_len<size:
        sock_data=the_socket.recv(recv_size)
        if not total_data:
            if len(sock_data)>4:
                size_data+=sock_data
                size=struct.unpack('>i', size_data[:4])[0]
                recv_size=size
                if recv_size>524288:recv_size=524288
                total_data.append(size_data[4:])
            else:
                size_data+=sock_data
        else:
            total_data.append(sock_data)
        total_len=sum([len(i) for i in total_data ])
    return ''.join(total_data)

def send(payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((options.ip, options.port))

    #input_num=`sendtoplug $ip $port "$payload"
    s.send(base64.b64decode(payload))
    data = recv_size(s)
    s.close()

    mapped = map(ord, data)

    code = 171
    response = ''
    for byte in mapped:
        output = byte ^ code
        response += chr(output)
        code=byte

    return json.loads(response)

def request(command):
    functions = {
            'on':    lambda: send(payload_on),
            'off':   lambda: send(payload_off),
            'query': lambda: send(payload_query),
            'meter': lambda: send(payload_emeter)
    }

    function = functions.get(command)

    if function:
        return function()
    else:
        print "Function must be one of {0}".format(functions.keys())
        exit()


print request(args[0])
