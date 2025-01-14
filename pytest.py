#!/usr/bin/env python3


import os



os.system("head -c 32 /dev/urandom | base64 > ./random.txt")
with open('random.txt', 'r') as file:
    encryption = file.read()
print(encryption)
