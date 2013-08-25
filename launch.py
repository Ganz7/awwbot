'''
File : Launch.py
Author : Ganz7 (ganzse7en@gmail.com)
Description : A basic irc bot.

Todo: 1) Needs refactoring.
      2) Extend the features.
      3) Cannot stay inhibited for long

'''

import socket
import sys
from random import randint
from botRequest import greetingsReq
from botReply import greetingsRep

server = "irc.freenode.net"
channel = "#madyo"		#Random Channel
botnick = "Awwbot"
hostname = "DeathStar"	#Blow it up
servername = "Mordor"	#Oh no I didn't

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ hostname +" "+ servername +" :McLovin\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #call me sexy
#irc.send("\r\n")    				        #Gotta reg a name
irc.send("JOIN "+ channel +"\n")

while 1:
	text=irc.recv(2040)
   	print text
	if text.find('PING') != -1:
      		irc.send('PONG ' + text.split() [1] + '\r\n') #I'm alive! Godammit!

      	if (text.find('PRIVMSG') != -1 and text.find('.freenode.net') == -1):
      		for word in greetingsReq.words:
      			if (text.lower().find(word)!= -1 ):
		      		t = str(text)
			 	ind = t.index('!')
			    	t = t[:ind]
			  	t = t[1:]
				irc.send('PRIVMSG '+channel+' :'+greetingsRep.words[randint(0,7)]+' '+t+'!\r\n')
