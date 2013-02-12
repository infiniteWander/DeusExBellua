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


sD10=parser.parsedObjectList("./characters/systemD10/")
#print sD10.files
prs=search.filterFunction("str>8&str=4")
#prs.show()
show.showList( sD10.filter(prs))
#Commands:
# view <char>
# set <system>
# find RECO [INTER/UNION RECO]
# RECO=<section>.<field> OP VAL

#for mm in xrange(nb*fdp):
	#p= parser.read("./characters/systemD10/Dragon.cfg")
	#for i in parser.sections(p):
		#[j for j in parser.items(p,i) if bint(j[1])>1]

#print (time.clock()-t1)/nb

