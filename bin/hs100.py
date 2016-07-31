#!/usr/bin/python
#-*- coding: utf-8 -*-

import unittest, os, sys
sys.path.append(os.path.abspath(sys.path[0]) + '/../hs100')

from core import Core
from optparse import OptionParser

usage = """This is a simple tool to manipulate TP-Link HS100 devices

%prog <on|off|query|meter> [options]

on:       turns on the device
off:      turns off the device
query:    queries the device for general information
meter:    queries the device for power usage information
discover: discover HS100 devices on the network"""

parser = OptionParser(usage=usage)
parser.add_option("--ip", dest="ip",
                  help="IP address to query. 'all' will auto discover devices.  ", metavar="IPADDR")

parser.add_option("--port", dest="port", default=9999, type="int",
                  help="PORT to query on the IP (default %default)", metavar="PORT")

parser.add_option("--debug", dest="debug", action="store_true",
                  help="Write debug file for responses")

(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("Incorrect number of arguments")
if not options.ip:
    parser.error("IP address was not given")

Core(options.ip, options.port, debug=options.debug).request(args[0])
