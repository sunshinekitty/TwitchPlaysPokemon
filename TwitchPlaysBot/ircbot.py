#!/usr/bin/env python3

# ircbot.py
# Copyright (C) 2014 : Alex Edwards
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#

import sys
import socket
import string
import os
import time

HOST = "irc.twitch.tv"
PORT = 6667
AUTH = "YOUR AUTH CODE" #Obtained at http://www.twitchapps.com/tmi 

NICK = "YOUR USERNAME HERE"
IDENT = "YOUR USERNAME HERE"
REALNAME = "YOUR USERNAME HERE"
MASTER = "YOUR USERNAME HERE"
CHAT_CHANNEL = "YOUR CHAT CHANNEL" #Typically username of the streamer

readbuffer = ""
out = ""
x = 0

os.system("chcp 65001")

s=socket.socket( )
s.connect((HOST, PORT))

s.send(bytes("PASS %s\r\n" % AUTH, "UTF-8"))
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("JOIN #%s\r\n" % CHAT_CHANNEL, "UTF-8"));
s.send(bytes("PRIVMSG #%s :Connected\r\n" % CHAT_CHANNEL, "UTF-8"))

while 1:
    readbuffer = readbuffer+s.recv(1024).decode("UTF-8", errors="ignore")
    temp = str.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        x = 0
        out = ""
        line = str.rstrip(line)
        line = str.split(line)

        for index, i in enumerate(line):
            # I don't know which it is, and I don't care in the slightest
            if(line[index] == "ING: " or line[index] == "ING:" or line[index] == "ING" or line[index] == "PING:" or line[index] == "PING: " or line[index] == "PING"):
                s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
            if x == 0:
                user = line[index]
                user = user[1:].split('!')[0] + ": "
            if x == 3:
                out += line[index]
                out = out[1:]
            if x >= 4:
                out += " " + line[index]
            x = x + 1
        print(user + out)
        if out.lower() == 'up':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'up')
        if out.lower() == 'right':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'right')
        if out.lower() == 'down':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'down')
        if out.lower() == 'left':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'left')
        if out.lower() == 'a':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'a')
        if out.lower() == 'b':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'b')
        if out.lower() == 'start':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'start')
        if out.lower() == 'select':
            with open("commands.txt", "a") as f:
                f.write('\n' + user + 'select')