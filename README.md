# About
This project is a Python implementation of the TP-Link HS100 Protocol.

It is based on the bash script found here: 
  https://github.com/ggeorgovassilis/linuxscripts/blob/master/tp-link-hs100-smartplug/hs100.sh
  and this blog post:
  https://georgovassilis.blogspot.com/
  
I can't take any credit for the hard part, I'm just writing it in Python. My end game is to be able to easily query
the devicees periodically and graph the results onto a simple webpage.

# Usage

```
Usage: hs100.py {on|off|query|meter} [options]

<b>on</b> turns on the device
<b>off</b> turns off the device
<b>query</b> queries the device for general information
<b>meter</b> queries the device for power usage information 

Options:
  -h, --help   show this help message and exit
  --ip=IPADDR  IP address to query
  --port=PORT  PORT to query on the IP (default 9999)
```
