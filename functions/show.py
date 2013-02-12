# -*- coding:utf8 -*-

###########################################
# show.py
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

def showList(dico):
	for fld,val in dico.iteritems():
		print "    {}".format(fld)
		for v in val:
			print "      > {}: {}".format(v[0],v[1])

def showPerso(perso):
	for section in perso.sections():
		print "[{}]".format(section)
		for item,val in perso.items(section):
			print "    {}: {}".format(item,val)
