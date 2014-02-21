#!/usr/bin/env python3

# controller.py
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
#
# THIS PROGRAM ASSUMES YOU ARE USING WINDOWS AND HAVE
# THE PYTHON FOR WINDOWS EXTENSIONS FOUND
# http://sourceforge.net/projects/pywin32/
# PROGRAM USES DIRECT INPUT TO FEED INTO VISUAL BOY ADVANCE
# TO CONVERT TO LINUX CHANGE "cls" TO "clear" AND FIND AN 
# ALTERNATIVE TO WIN32API ON YOUR FAVORITE DISTRO
# THEN EMAIL ME HOW YOU GOT IT TO WORK, BECAUSE I COULDN'T
#
# Cheers,
# Don't email me for support
#

import time, os, win32com.client, win32api, win32con

gay = False
up_c = 0
right_c = 0
down_c = 0
left_c = 0
a_c = 0
b_c = 0
start_c = 0
select_c = 0

shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("Silver.gbc")

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
        time.sleep(0.2)
        win32api.keybd_event(VK_CODE[i],0 ,win32con.KEYEVENTF_KEYUP ,0)
                    
while True:
    try:
        f = open('commands.txt')
        lines = f.readlines()
        f.close()
        for line in lines:
            if(line == "" or line == "\n"):
                gay = True
            else:
                value_c = (line).split(' ')[1]
                if value_c == "up\n" or value_c == "up":
                    up_c = up_c + 1
                if value_c == "right\n" or value_c == "right":
                    right_c = right_c + 1
                if value_c == "down\n" or value_c == "down":
                    down_c = down_c + 1
                if value_c == "left\n" or value_c == "left":
                    left_c = left_c + 1
                if value_c == "a\n" or value_c == "a":
                    a_c = a_c + 1
                if value_c == "b\n" or value_c == "b":
                    b_c = b_c + 1
                if value_c == "start\n" or value_c == "start":
                    start_c = start_c + 1
                if value_c == "select\n" or value_c == "select":
                    select_c = select_c + 1
        alloutputs = {'Up': up_c, 'Right': right_c, 'Down': down_c, 'Left': left_c, 'Start': start_c, 'Select': select_c, 'B': b_c, 'A': a_c}
        if(up_c + right_c + down_c + left_c + start_c + select_c + b_c + a_c == 0):
            selected_c = "None"
        else:
            selected_c = max(alloutputs, key = alloutputs.get)
        os.system("cls")
        print("Up: " + str(up_c))
        print("Right: " + str(right_c))
        print("Down: " + str(down_c))
        print("Left: " + str(left_c))
        print("A: " + str(a_c))
        print("B: " + str(b_c))
        print("Start: " + str(start_c))
        print("Select: " + str(select_c))
        print("\nSelected: " + selected_c)
        up_c = 0
        right_c = 0
        down_c = 0
        left_c = 0
        a_c = 0
        b_c = 0
        start_c = 0
        select_c = 0
        if selected_c == "Up":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('up_arrow')
        if selected_c == "Right":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('right_arrow')
        if selected_c == "Down":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('down_arrow')
        if selected_c == "Left":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('left_arrow')
        if selected_c == "A":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('z')
        if selected_c == "B":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('x')
        if selected_c == "Start":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('enter')
        if selected_c == "Select":
            shell.AppActivate("VisualBoyAdvance")
            time.sleep(.02)
            press('backspace')
        with open("commands.txt", "w") as f:
            f.write(' Selected ' + selected_c)
        time.sleep(3)
    except FileNotFoundError:
        gay = True
