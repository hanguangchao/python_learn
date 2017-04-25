# -*- coding: utf-8 -*- 

import time
import socket
import socks
import requests
from stem import Signal
from stem.control import Controller

controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 , "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket
    print("connectTor")

def renew_tor():
    controller.authenticate(password='rootroot')
    controller.signal(Signal.NEWNYM)
    print("renew_tor")

def showmyip():
    r = requests.get('http://icanhazip.com/')
    ip_address = r.text.strip()
    print("showmyip")
    print(ip_address)

if __name__ == '__main__':

    for i in range(3):
        renew_tor()
        connectTor()
        showmyip()
        time.sleep(10)
