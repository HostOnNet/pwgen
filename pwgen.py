#!/usr/bin/python

"""pwgen: Generate secure password."""

__author__      = "HostOnNet.com"
__email__       = "admin@hostonnet.com"
__copyright__   = "Copyright 2016, HostOnNet.com"


import random

PASSWORD_LENGTH = 14
password_chars = "abcdefghjkmnpqrstuvwxyz"

def update_password(password, char):
    replace_index = random.randrange(len(password))
    if (replace_index == 0):
        replace_index = 1;
    return password[0:replace_index] + str(char) + password[replace_index+1:]

my_password = ""

for i in range(PASSWORD_LENGTH):
    next_index = random.randrange(len(password_chars))
    if (random.randrange(10) > 5):
        my_password = my_password + password_chars[next_index].upper()
    else:
        my_password = my_password + password_chars[next_index]

my_password = update_password(my_password, "@")
my_password = update_password(my_password, random.randrange(0,9))

print (my_password)
