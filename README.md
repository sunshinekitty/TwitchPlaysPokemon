<h1>Twitch Plays Pokemon IRC Bot</h1>
<h2>Written in Python 3.3.4</h2>
<p>This will be updated, but not much.  I will create a quick and easy way for people to connect Twitch to Visual Boy Advance and have an interactive chat, however beyond that not much is to be promised.  I will continue the development of my own personal project where I work from this script as a base to build what fits my needs.</p>

<h2>Pre requisists</h2>
<p>This is written in Python 3.3.4 and meant to run on Windows, it has only been tested on Windows 7 because I hate Windows 8.  That being said, you need to install this:

<a href="http://www.python.org/ftp/python/3.3.4/python-3.3.4.amd64.msi">64 bit</a>

<a href="http://www.python.org/ftp/python/3.3.4/python-3.3.4.msi">Everyone else</a>

After that install this:

<a href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win-amd64-py3.3.exe/download">64 bit</a>

<a href="http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py3.3.exe/download">Everyone Else</a>

<i>If you experience a dll error uninstall this and use the other link</i>

You'll want to download <a href="http://coolrom.com/emulators/gba/14/Visual_Boy_Advance.php">Visual Boy Advance</a> and set .gbc files to open with it by default before running this bot

Now you're good, download <a href="https://github.com/sunshinekitty5/TwitchPlaysPokemon/archive/master/twitchplayspokemon.zip">this</a> and extract it anywhere, don't re-arrange or re-name the contents without changing the scripts, you will also need to update ircbot.py to connect to your account, or else it will NOT work.

<h2>How-to run</h2>

Open Visual Boy Advance and change your arrow key settings to use num-pad 8, 4, 6, 2 respectively with num-lock enabled, Z and X are A and B, Enter and Backspace are Start and Select.

Drop your .gbc file (ONLY ONE .GBC FILE) into the folder named "game"

Open CMD prompt and type in chcp 65001

Navigate to the Python script Launch.py and type in the name of it, it should open in python

<h2>In other news</h2>
Now I will shamelessly plug my channel <a href="http://www.twitch.tv/nutz1"><b>HERE</b></a>

However once I move it to a server it will be shown <a href="http://www.twitch.tv/twitchplaysgameboyadvance"><B>HERE</B></a>

So if you must follow a channel, follow the latter.

<h3>Side:</h3>
If you get this working on a Ubuntu 12.04 server running xvnc please tell me what you're using to stream by sending me a message on Twitch, I'd appreciate it so I can port this to Linux.

My code is not beautiful and could be better.
