#!/usr/bin/env python

from time import sleep

"""
    print function with flush parametr
    Created by: Artjoms Jablonskis

    URL: https:// www.includehelp.com/python/flush-parametr-in-python-with-print-function.aspx
"""
# output is flushed here
print("hello, world!,", end=' ', flush='true')
sleep(5)
print("bye!!!")

input("Press <Enter> to continue..")
