#!/usr/bin/env python3

# Launch.py
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

import configparser
import os
import sys
import string
import time
import socket
from threading import Thread
import win32com.client, win32api, win32con

settings = []
commands = []
readbuffer = ""
GAME = os.listdir('game')[0]

VK_CODE = {'backspace':0x08,
                    'tab':0x09,
                    'clear':0x0C,
                    'enter':0x0D,
                    'shift':0x10,
                    'ctrl':0x11,
                    'alt':0x12,
                    'pause':0x13,
                    'caps_lock':0x14,
                    'esc':0x1B,
                    'spacebar':0x20,
                    'page_up':0x21,
                    'page_down':0x22,
                    'end':0x23,
                    'home':0x24,
                    'left_arrow':0x25,
                    'up_arrow':0x26,
                    'right_arrow':0x27,
                    'down_arrow':0x28,
                    'select':0x29,
                    'print':0x2A,
                    'execute':0x2B,
                    'print_screen':0x2C,
                    'ins':0x2D,
                    'del':0x2E,
                    'help':0x2F,
                    '0':0x30,
                    '1':0x31,
                    '2':0x32,
                    '3':0x33,
                    '4':0x34,
                    '5':0x35,
                    '6':0x36,
                    '7':0x37,
                    '8':0x38,
                    '9':0x39,
                    'a':0x41,
                    'b':0x42,
                    'c':0x43,
                    'd':0x44,
                    'e':0x45,
                    'f':0x46,
                    'g':0x47,
                    'h':0x48,
                    'i':0x49,
                    'j':0x4A,
                    'k':0x4B,
                    'l':0x4C,
                    'm':0x4D,
                    'n':0x4E,
                    'o':0x4F,
                    'p':0x50,
                    'q':0x51,
                    'r':0x52,
                    's':0x53,
                    't':0x54,
                    'u':0x55,
                    'v':0x56,
                    'w':0x57,
                    'x':0x58,
                    'y':0x59,
                    'z':0x5A,
                    'numpad_0':0x60,
                    'numpad_1':0x61,
                    'numpad_2':0x62,
                    'numpad_3':0x63,
                    'numpad_4':0x64,
                    'numpad_5':0x65,
                    'numpad_6':0x66,
                    'numpad_7':0x67,
                    'numpad_8':0x68,
                    'numpad_9':0x69,
                    'multiply_key':0x6A,
                    'add_key':0x6B,
                    'separator_key':0x6C,
                    'subtract_key':0x6D,
                    'decimal_key':0x6E,
                    'divide_key':0x6F,
                    'F1':0x70,
                    'F2':0x71,
                    'F3':0x72,
                    'F4':0x73,
                    'F5':0x74,
                    'F6':0x75,
                    'F7':0x76,
                    'F8':0x77,
                    'F9':0x78,
                    'F10':0x79,
                    'F11':0x7A,
                    'F12':0x7B,
                    'F13':0x7C,
                    'F14':0x7D,
                    'F15':0x7E,
                    'F16':0x7F,
                    'F17':0x80,
                    'F18':0x81,
                    'F19':0x82,
                    'F20':0x83,
                    'F21':0x84,
                    'F22':0x85,
                    'F23':0x86,
                    'F24':0x87,
                    'num_lock':0x90,
                    'scroll_lock':0x91,
                    'left_shift':0xA0,
                    'right_shift ':0xA1,
                    'left_control':0xA2,
                    'right_control':0xA3,
                    'left_menu':0xA4,
                    'right_menu':0xA5,
                    'browser_back':0xA6,
                    'browser_forward':0xA7,
                    'browser_refresh':0xA8,
                    'browser_stop':0xA9,
                    'browser_search':0xAA,
                    'browser_favorites':0xAB,
                    'browser_start_and_home':0xAC,
                    'volume_mute':0xAD,
                    'volume_Down':0xAE,
                    'volume_up':0xAF,
                    'next_track':0xB0,
                    'previous_track':0xB1,
                    'stop_media':0xB2,
                    'play/pause_media':0xB3,
                    'start_mail':0xB4,
                    'select_media':0xB5,
                    'start_application_1':0xB6,
                    'start_application_2':0xB7,
                    'attn_key':0xF6,
                    'crsel_key':0xF7,
                    'exsel_key':0xF8,
                    'play_key':0xFA,
                    'zoom_key':0xFB,
                    'clear_key':0xFE,
                    '+':0xBB,
                    ',':0xBC,
                    '-':0xBD,
                    '.':0xBE,
                    '/':0xBF,
                    '`':0xC0,
                    ';':0xBA,
                    '[':0xDB,
                    '\\':0xDC,
                    ']':0xDD,
                    "'":0xDE,
                    '`':0xC0}

def press(*args):
    '''
    press, release
    eg press('x', 'y', 'z')
    '''
    for i in args:
        win32api.keybd_event(VK_CODE[i], 0, 0, 0)
        if QUICK_PRESS == False:
            time.sleep(0.2)
        if QUICK_PRESS == True:
            time.sleep(.01)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
        
def addtofile():
    if len(commands) >= command_length:
        del commands[0]
        commands.extend([user[1:] + out.lower()])
        if mode.lower() == "democracy":
            list_commands.extend([out.lower()])
    else:
        commands.extend([user[1:] + out.lower()])
        if mode.lower() == "democracy":
            list_commands.extend([out.lower()])

def democracy():
    global list_commands
    list_commands = []
    last_command = time.time()
    up_counter = 0
    right_counter = 0
    down_counter = 0
    left_counter = 0
    start_counter = 0
    select_counter = 0
    a_counter = 0
    b_counter = 0
    selected_c = "None"
    
    while True:
        if time.time() > last_command + democracy_time:
            last_command = time.time()
            for list_command in list_commands:
                if list_command == "up":
                    up_counter = up_counter + 1
                if list_command == "right":
                    right_counter = right_counter + 1
                if list_command == "down":
                    down_counter = down_counter + 1
                if list_command == "left":
                    left_counter = left_counter + 1
                if list_command == "a":
                    a_counter = a_counter + 1
                if list_command == "b":
                    b_counter = b_counter + 1
                if list_command == "start":
                    start_counter = start_counter + 1
                if list_command == "select":
                    select_counter = select_counter + 1
            alloutputs = {'Up': up_counter, 'Right': right_counter, 'Down': down_counter, 'Left': left_counter, 'Start': start_counter, 'Select': select_counter, 'B': b_counter, 'A': a_counter}
            if(up_counter + right_counter + down_counter + left_counter + start_counter + select_counter + b_counter + a_counter == 0):
                selected_c = "None"
            else:
                selected_c = max(alloutputs, key = alloutputs.get)
            with open("lastsaid.txt", "w") as f:
                f.write("Selected %s\n" % selected_c)
                f.write("Time left: %s" % str(democracy_time)[0:1])
            list_commands = []
            if selected_c.lower() == 'up':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('up_arrow')
            if selected_c.lower() == 'right':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('right_arrow')
            if selected_c.lower() == 'down':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('down_arrow')
            if selected_c.lower() == 'left':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('left_arrow')
            if selected_c.lower() == 'a':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('z')
            if selected_c.lower() == 'b':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('x')
            if selected_c.lower() == 'start':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('enter')
            if selected_c.lower() == 'select':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('backspace')
            up_counter = 0
            right_counter = 0
            down_counter = 0
            left_counter = 0
            start_counter = 0
            select_counter = 0
            a_counter = 0
            b_counter = 0
        else:
            with open("lastsaid.txt", "w") as f:
                f.write("Selected %s\n" % selected_c)
                f.write("Time left: %s" % str(1.0 + last_command + democracy_time - time.time())[0:1])
        time.sleep(1)
        
# Generate a config file if one doesn't exist
while True:
    if os.path.isfile("settings.txt"):
        config = configparser.ConfigParser()
        config.read("settings.txt")
        HOST = config.get('Settings', 'HOST')
        PORT = config.getint('Settings', 'PORT')
        AUTH = config.get('Settings', 'AUTH')
        NICK = config.get('Settings', 'USERNAME').lower()
        APP = config.get('Settings', 'APP')
        CHAT_CHANNEL = config.get('Settings', 'CHAT_CHANNEL').lower()
        command_length = config.getint('Settings', 'LENGTH')
        QUICK_PRESS = config.getboolean('Settings', 'QUICK_PRESS')
        break
    else:
        print("Let's make you a config file")
        settings.append("; Settings for Twitch Plays Pokemon bot")
        settings.append("; Thanks to RDJ, MZ, AP, & Oriax\n")
        
        settings.append("[Settings]\n")
        
        settings.append("; Where you're connecting to, if it's Twitch leave it as is")
        print("Where you're connecting to, if it's Twitch use irc.twitch.tv")
        settings_host = input("Hostname: ")
        settings.append("HOST = " + settings_host + "\n")
        
        settings.append("; Port number, probably should use 6667")
        print("Port number, probably should use 6667")
        settings_port = input("Port: ")
        settings.append("PORT = " + settings_port + "\n")
        
        settings.append("; Auth token, grab this from http://www.twitchapps.com/tmi")
        print("Auth token, grab this from http://www.twitchapps.com/tmi")
        settings_auth = input("Auth Token: ")
        settings.append("AUTH = " + settings_auth + "\n")
        
        settings.append("; Your Twitch Bot's Username")
        print("Your Twitch Bot's Username")
        settings_bot = input("Bot's Username: ")
        settings.append("USERNAME = " + settings_bot + "\n")
        
        settings.append("; Name of the application you run the file from, I suggest VBA")
        print("Name of the application you run the file from, if Visual Boy Advance use VisualBoyAdvance")
        settings_app = input("Application name: ")
        settings.append("APP = " + settings_app + "\n")
        
        settings.append("; Username of who's channel you're connecting to")
        print("Username of who's channel you're connecting to")
        settings_chat = input("Username: ")
        settings.append("CHAT_CHANNEL = " + settings_chat + "\n")
        
        settings.append("; The maximum number of lines in commands.txt (Useful for showing commands received in stream)")
        print("The maximum number of lines in commands.txt (Useful for showing commands received in stream)")
        settings_length = input("Length: ")
        settings.append("LENGTH = " + settings_length + "\n")
        
        settings.append("; Oh how to explain this...")
        settings.append("; You get the chat command 'Left'")
        settings.append("; You are currently facing right")
        settings.append("; If QUICK_PRESS is true you turn left")
        settings.append("; If QUICK_PRESS is false you turn left and move one square left")
        print("Oh how to explain this...")
        print("You get the chat command 'Left'")
        print("You are currently facing right")
        print("If QUICK_PRESS is true you turn left")
        print("If QUICK_PRESS is false you turn left and move one square left")
        settings_press = input("QUICK PRESS: ")
        settings.append("QUICK_PRESS = " + settings_press + "\n")
        
        with open("settings.txt", "w") as f:
            for each_setting in settings:
                f.write(each_setting + '\n')
                
while True:
    print("Currently available: Anarchy, Democracy")
    mode = input("Game type: ")
    if mode.lower() == "anarchy":
        break
    if mode.lower() == "democracy":
        print("Takes most said command every X second: ")
        democracy_time = float(input("(must be integer) X="))
        break

# Anarchy Game Mode
if mode.lower() == "anarchy":
    with open("lastsaid.txt", "w") as f:
        f.write("")
    print("Starting %s" % GAME)
    time.sleep(1)
    if os.path.splitext(os.listdir('game')[0])[1] != ".sav":
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Run("%s\game\%s" % (os.getcwd(), GAME))
        shell.AppActivate("%s" % APP)

    os.system("chcp 65001")

    s=socket.socket( )
    s.connect((HOST, PORT))

    s.send(bytes("PASS %s\r\n" % AUTH, "UTF-8"))
    s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
    s.send(bytes("USER %s %s bla :%s\r\n" % (NICK, HOST, NICK), "UTF-8"))
    s.send(bytes("JOIN #%s\r\n" % CHAT_CHANNEL, "UTF-8"));
    s.send(bytes("PRIVMSG #%s :Connected\r\n" % CHAT_CHANNEL, "UTF-8"))
    print("Sent connected message to channel %s" % CHAT_CHANNEL)

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
                if x == 0:
                    user = line[index]
                    user = user.split('!')[0] + ": "
                if x == 3:
                    out += line[index]
                    out = out[1:]
                if x >= 4:
                    out += " " + line[index]
                x = x + 1
            
            # Respond to ping, squelch useless feedback given by twitch, print output and read to list
            if user == "PING: ":
                s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
            elif user == ":tmi.twitch.tv: ":
                pass
            elif user == ":%s.tmi.twitch.tv: " % NICK:
                pass
            else:
                print(user + out)
                
            # Take in output
            if out.lower() == 'up':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('up_arrow')
                addtofile()
            if out.lower() == 'right':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('right_arrow')
                addtofile()
            if out.lower() == 'down':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('down_arrow')
                addtofile()
            if out.lower() == 'left':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('left_arrow')
                addtofile()
            if out.lower() == 'a':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('z')
                addtofile()
            if out.lower() == 'b':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('x')
                addtofile()
            if out.lower() == 'start':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('enter')
                addtofile()
            if out.lower() == 'select':
                shell.AppActivate("%s" % APP)
                time.sleep(.02)
                press('backspace')
                addtofile()
                
            # Write to file for stream view
            with open("commands.txt", "w") as f:
                for item in commands:
                    f.write(item + '\n')

# Democracy Game Mode
if mode.lower() == "democracy":
   
    if __name__ == "__main__":
        count_job = Thread(target = democracy, args = ())
        count_job.start()
        #count_job.join()
    
    print("Starting %s" % GAME)
    time.sleep(1)
    if os.path.splitext(os.listdir('game')[0])[1] != ".sav":
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Run("%s\game\%s" % (os.getcwd(), GAME))
        shell.AppActivate("%s" % APP)

    os.system("chcp 65001")
    
    s=socket.socket( )
    s.connect((HOST, PORT))
    
    s.send(bytes("PASS %s\r\n" % AUTH, "UTF-8"))
    s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
    s.send(bytes("USER %s %s bla :%s\r\n" % (NICK, HOST, NICK), "UTF-8"))
    s.send(bytes("JOIN #%s\r\n" % CHAT_CHANNEL, "UTF-8"));
    s.send(bytes("PRIVMSG #%s :Connected\r\n" % CHAT_CHANNEL, "UTF-8"))
    print("Sent connected message to channel %s" % CHAT_CHANNEL)

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
                if x == 0:
                    user = line[index]
                    user = user.split('!')[0] + ": "
                if x == 3:
                    out += line[index]
                    out = out[1:]
                if x >= 4:
                    out += " " + line[index]
                x = x + 1
            
            # Respond to ping, squelch useless feedback given by twitch, print output and read to list
            if user == "PING: ":
                s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
            elif user == ":tmi.twitch.tv: ":
                pass
            elif user == ":%s.tmi.twitch.tv: " % NICK:
                pass
            else:
                print(user + out)
                
            # Take in output
            if out.lower() == 'up':
                addtofile()
            if out.lower() == 'right':
                addtofile()
            if out.lower() == 'down':
                addtofile()
            if out.lower() == 'left':
                addtofile()
            if out.lower() == 'a':
                addtofile()
            if out.lower() == 'b':
                addtofile()
            if out.lower() == 'start':
                addtofile()
            if out.lower() == 'select':
                addtofile()
                
            # Write to file for stream view
            with open("commands.txt", "w") as f:
                for item in commands:
                    f.write(item + '\n')















































