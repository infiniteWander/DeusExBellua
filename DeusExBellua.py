#!/usr/bin/python
# -*- coding:utf8 -*-

###########################################
# DeusExBellua.py
# Nom: DeusExBellua
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of DeusExBellua.
#
# DeusExBellua is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DeusExBellua is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DeusExBellua. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

import os,sys
from functions import *
import time

#------- Functions ----------
def viewP(t):
	p=system.get(t[1])
	if not p:
		print "The character {} doesn't exist".format(t[1])
	else:
		show.showPerso(p)

def setS(t):
	print "Not implemented yet"

def findP(t):
	prs=search.filterFunction(t[1])
	show.showList(system.filter(prs))
	
def helpC(t):
	printCommands()

def quitP(t):
	sys.exit()

def printCommands():
	print "Valid commands are:"
	for c in commands: print "   ",c,helpCommands[c]
	
def invalidCommand(text):
	print "Error: command {} is invalid".format(text[0])
	printCommands()

def parseInput(text):
	if text[0] not in commands:
		invalidCommand(text)
		return
	commands[text[0]](text)	

commands={'show':viewP,'set':setS,'find':findP,'help':helpC,'quit':quitP}
helpCommands={
	'show':"<character> Show the character",
	'set':"<system> Change the current game system (indev)",
	'find':"""<expression> Lookup for a character matching the expression
        <expression> = <field> [=><!?] ([&|] <expression>)""",
	'help':'Display this help',
	'quit':'Quit program'
}
#---------- Load ----------

# Load the game system (Supposed to be a function)
systemPath="./characters/systemD10/"
prompt="{}> ".format(systemPath.split('/')[-2])
system=parser.parsedObjectList(systemPath)

#---------- Main loop ---------
while (1):
	try:
		sys.stdout.write(prompt)
		sys.stdout.flush()
		parseInput(raw_input().split(" ",1))
	except SystemExit:
		break
	except ValueError: #Improvethat
		pass
