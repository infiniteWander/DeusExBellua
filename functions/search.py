# -*- coding:utf8 -*-

###########################################
# search.py
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

def Inf(a,b):
	return a>b
def Sup(a,b):
	return a<b
def Eq(a,b):
	return a==b
def Not(a,b):
	return a!=b
def In(a,b):
	return a in b
def And(a,b):
	return a and b
def Or(a,b):
	return a or b

op=[">","<"]
textop=["=","!","?"]
allop=op+textop
logicop=["&","|"]
translateop={">":Inf,"<":Sup,"=":Eq,'!':Not,'?':In,'&':And,'|':Or}


#class Request():
	#def __init__(self,section,function):
		#"""The form of a the "section" field is either:
			#+ section.* (all fields)
			#+ section (analyse the section itself)
			#+ * (All sections)
			#+ section.field (analyse a specific field)
		#If at least one field match the function,
		#the analysis return true, false otherwise"""
		#self.function=function
		#self.section=self.parse(section)
		

class filterFunction():
	def __init__(self,text):
		self.field,self.op,self.val="","",""
		self.following=None
		self.followingOp=None
		self.parse(text)
		
	def parse(self,text):
		i,j,mx=0,0,len(text)
		virgin=True
	
		for i in xrange(mx):
			if text[i] in allop:
				if text[i] in op:
					self.val="i"
				self.field=text[0:i].strip()
				self.op=text[i].strip()
				virgin=False
				break
		
		for j in xrange(i,mx):
			if text[j] in logicop:
				self.following=filterFunction(text[j+1:mx])
				self.followingOp=text[j]
				j-=1
				break
		
		if self.val=="i":
			self.val=int(text[i+1:j+1])
		else:
			self.val=text[i+1:j+1].strip()
	def process(self,parser):
		val=False
		for data in match(self.field,parser):
			if translateop[self.op](data,self.val):
				val=True
				break
		if self.following:
			translateop[self.followingOp](self.following.process(parser),val)
		return val
	
	def show(self):
		print (self.field,self.op,self.val)
		if self.following:
			print self.followingOp
			self.following.show()

def match(field,parser):
	ret=[]
	for section in parser.sections():
		for item,val in parser.items(section):
			if field in item:
				ret.append(val)
	return ret
