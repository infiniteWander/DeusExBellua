# -*- coding:utf8 -*-

###########################################
# parser.py
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
from ConfigParser import ConfigParser

class parsedObjectList():
	def __init__(self,directory):
		self.files={}
		for f in os.listdir(directory):
			short=f.rsplit(".",1)[0]
			self.files[short]=ConfigParser()
			self.files[short].read(os.path.join(directory,f))
	def get(self,elt):
		if elt in self.files:
			return self.files[elt]
		else:
			return False
	def filter(self,function):
		res={}
		for name,prs in self.files.iteritems():
			tmp=function.process(prs)
			if len(tmp)>0:
				res[name]=tmp
		return res
