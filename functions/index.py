# -*- coding:utf8 -*-

###########################################
# index.py
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
import parser
from ENV import *

def createIndex():
	pass

def existsIndex(game):
	return os.path.exists(os.path.append(INDEX_PATH,game))
