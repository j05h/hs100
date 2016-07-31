import sys
import socket
import struct
import base64

def send(ip, port, payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(base64.b64decode(payload))
    data = recv_size(s)
    s.close()

    return data

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

def check_port(host, port):
    captive_dns_addr = ""
    host_addr = ""
    try:
        captive_dns_addr = socket.gethostbyname("BlahThisDomaynDontExist22.com")
    except:
        pass
    try:
        host_addr = socket.gethostbyname(host)
        if (captive_dns_addr == host_addr):
            return False
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except:
        return False
    return host

def my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com",80))
    myip = (s.getsockname()[0])
    s.close()

    return myip
