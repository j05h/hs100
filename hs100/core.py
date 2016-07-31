#!/usr/bin/python
#-*- coding: utf-8 -*-

import time
import base64
import sys
import struct
import json
import helpers
from netaddr import *
import Queue
import threading

class Core:
    # base64 encoded data to send to the plug to switch it on
    payload_on="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="

    # base64 encoded data to send to the plug to switch it off
    payload_off="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="

    # base64 encoded data to send to the plug to query it
    payload_query="AAAAI9Dw0qHYq9+61/XPtJS20bTAn+yV5o/hh+jK8J7rh+vLtpbr"

    # base64 encoded data to query emeter - hs100 doesn't seem to support this in hardware, but the API seems to be there...
    payload_emeter="AAAAJNDw0rfav8uu3P7Ev5+92r/LlOaD4o76k/6buYPtmPSYuMXlmA=="

    ip    = None
    port  = 9999
    debug = False

    def __init__(self, ip, port, debug):
        self.ip    = ip
        self.port  = port
        self.debug = debug

    def send(self, payload, ip, port):
        data = helpers.send(ip, port, payload)

        if self.debug:
            debug_file = open(args[0]+".debug", "w")
            debug_file.write(data)
            debug_file.close()

        mapped = map(ord, data)

        code = 171
        response = ''
        for byte in mapped:
            output = byte ^ code
            response += chr(output)
            code=byte

        return json.loads(response)

    def request(self, command):
        functions = {
                'on':    self.payload_on,
                'off':   self.payload_off,
                'query': self.payload_query,
                'meter': self.payload_emeter,
        }

        if command == 'discover':
            print self.discover()

        payload = functions.get(command)

        if payload:
            if self.ip == 'all':
                ips = self.discover()
            else:
                ips = [self.ip]

            for ip in ips:
                print ip
                print self.send(payload, ip, self.port)
        else:
            print "Function must be one of {0}".format(functions.keys())
            exit()

    def find(self, q, ip):
        result = helpers.check_port(ip, self.port)

        if result:
            q.put(result)

    def discover(self):
        ipset = IPSet([helpers.my_ip() + '/24'])

        print("Discovering devices on {0}".format(ipset))

        q = Queue.Queue()

        threads = []
        for ip in list(ipset):
            t = threading.Thread(target=self.find, args=(q, str(ip)))
            t.daemon = True
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        ips = []
        while not q.empty():
            ips.append(q.get())

        return ips
