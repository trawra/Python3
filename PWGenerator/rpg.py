#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random
import time


def random_password_genertor():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*'
    size = 8
    return ''.join(random.choice(chars) for x in range(size, 16))
     # size,16 means 8 characters increase or decrease as needed

def random_password_genertor_ico():
	random_password_genertor_ico = """
	#-----------------------------------------------------------#
	#        PYTHON - Random Password Generator (RPG)           #
	#-----------------------------------------------------------# 
	#                         CONTACT:                          #
	#-----------------------------------------------------------#
	#                     DEV: TR_Unknown                       #
	#                                                           #
	#-----------------------------------------------------------#
	"""
	print(random_password_genertor_ico)

random_password_genertor_ico()

# Prints password on screen.
print("Password : " + random_password_genertor())

# Telling the user program will pause for 25 seconds.
print("Program Paused for 25 seconds...")
time.sleep(25) #this will pause for 25 seconds