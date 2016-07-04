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
This is a simple tool to manipulate TP-Link HS100 devices

Usage: hs100.py <on|off|query|meter> [options]

on:    turns on the device
off:   turns off the device
query: queries the device for general information
meter: queries the device for power usage information

Options:
  -h, --help   show this help message and exit
  --ip=IPADDR  IP address to query
  --port=PORT  PORT to query on the IP (default 9999)
```

# Examples
```
$ ./hs100.py on --ip=10.0.0.8
{u'system': {u'set_relay_state': {u'err_code': 0}}}

$./hs100.py query --ip=10.0.0.8
{u'system': {u'get_sysinfo': {u'oemId': u'FFFFFFFFFFFFFFFFFFFFFFFFFF', u'dev_name': u'Wi-Fi Smart Plug With Energy Monitoring', u'on_time': 171171, u'feature': u'TIM:ENE', u'fwId': u'EEEEEEEEEEEEEEEEEEEEEEEEE', u'icon_hash': u'', u'relay_state': 1, u'latitude': 30.302912, u'hw_ver': u'1.0', u'type': u'IOT.SMARTPLUGSWITCH', u'led_off': 0, u'hwId': u'11111111111111111111111111', u'sw_ver': u'1.0.8 Build 151113 Rel.24658', u'mac': u'22:22:22:22:22:22', u'active_mode': u'schedule', u'deviceId': u'888888888888888888888888888888', u'updating': 0, u'longitude': -88, u'alias': u'hot water', u'rssi': -50, u'model': u'HS110(US)', u'err_code': 0}}}
