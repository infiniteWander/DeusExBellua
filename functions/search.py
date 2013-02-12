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

from errors import *

def Inf(a,b):
	#print int(a),int(b),int(a)>int(b)
	return int(a)>int(b)
def Sup(a,b):
	return int(a)<int(b)
def Eq(a,b):
	return a==b
def Not(a,b):
	return a!=b
def In(a,b):
	return b in a
	
def And(a,b):
	return len(a)>0 and len(b)>0
	
def Or(a,b):
	return len(a)>0 or len(b)>0

allop=[">","<","=","!","?"]
logicop=["&","|"]
translateop={">":Inf,"<":Sup,"=":Eq,'!':Not,'?':In,'&':And,'|':Or}

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
				self.field=text[0:i].strip()
				self.op=text[i]
				virgin=False
				break
		
		for j in xrange(i,mx):
			if text[j] in logicop:
				self.following=filterFunction(text[j+1:mx])
				self.followingOp=text[j]
				j-=1
				break
		
		self.val=text[i+1:j+1].strip()
		if virgin:
			print 'Parsing error: Expression "{}" is incorrect'.format(text)
			raise ParsingError
		
	def process(self,parser):
		found=[]
		for field,val in match(self.field,parser):
			try:
				if translateop[self.op](val,self.val):
					if self.op=="?": # Extract context only
						val=contex(val,self.val)
					found.append((field,val))
					#break #If you wan't only the first result
			except:
				pass
		if self.following:
			nfound=self.following.process(parser)
			if translateop[self.followingOp](nfound,found):
				return found+nfound
			else: return []
		
		return found
	
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
				ret.append((item,val))
	
	return ret

def contex(text,word):
	ind=text.find(word)
	mi,ma=max(0,ind-30),min(len(text),ind+30)
	
	i=text.find(" ",mi,ind)
	j=text.rfind(" ",ind,ma)
	if j<0: j=ma
	return text[max(mi,i):j+1]
