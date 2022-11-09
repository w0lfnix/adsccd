import requests
import struct
import os


def my_recv(conn, format):
    s = conn.recv(1024)
    bs =b''
    bs += s
    while s:
        s.recv(1024)
        bs+=s

    struct.unpack(bs, format)

   

def my_curl(adresse):
    os.system(f"curl {adresse}")

def my_post(adresse, payload):
    #payload string : '{"key":"value}'
    os.system(f"curl {adresse} -H 'Content-Type:application/json' -d '{payload}'")
