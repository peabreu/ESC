#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Paulo E. Abreu (c) 2008 Departamento de Química, Universidade de Coimbra, Portugal
# This is free software.  You may redistribute it under the terms
# of the Apache license and the GNU General Public License Version
# 2 or at your option any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#
# Description:
# This program parses a GAMESS-US PUNCH file
# writing localized or canonical orbitals to the standard output
# Usage loc-can-orbs.py file.dat
# Command line arguments
#            -c canonical orbitals output
#            -l localized orbitals output
#            -o output_file.orb (by default writes file.orb)
#            -m merge orbitals into output file (localized+canonical)
#
########################################################################################
########################################################################################
########################################################################################
import os
import sys
import re
import string

localized = 0
canonical = 1 # default 
merged = 0

#2DO replace this with the new facility for parsing arguments
# parse command line arguments
args = sys.argv[1:]
#print args
nargs = len(args)
if nargs < 1:
        print 'No GAMESS-US PUNCH file specified.'
        sys.exit()

if nargs == 1:
    filename = args[0]
    print filename

if nargs == 2:
    if args[1] == "-l" :
        localized=1
        canonical=0
        merged=0
	filename = args[0]
    if args[0] == "-l" :
        localized=1
        canonical=0
        merged=0
	filename = args[1]
    if args[1] == "-c" :
        localized=0
        canonical=1
        merged=0
	filename = args[0]
    if args[0] == "-c" :
        localized=0
        canonical=1
        merged=0
	filename = args[1]
    if args[0] == "-m" :
        localized=0
        canonical=0
        merged=1
	filename = args[1]
    if args[1] == "-m" :
        localized=0
        canonical=0
        merged=1
	filename = args[0]
    #
#

#
# Separate component into filename and path upto the directory 
pathfilename=os.path.split(filename)[0]
filename=os.path.split(filename)[1]

# generate file.orbs name
orbname = string.join(string.split(filename,".dat"), ".orb")
print orbname,localized,canonical

# open GAMESS-US file for reading
gamess_us_dat_file = open (filename,'r')
gamess_orb_file = open (orbname,'w')

myre_vec = re.compile(r' \$VEC')
myre_end = re.compile(r' \$END')
#myre_vecend = re.compile(r' \$VEC* \$END')

#if merged:
#	vecs=0
#	for line in gamess_us_dat_file:
#           orbname_c = string.join(string.split(filename,".dat"), ".orc")
#           orbname_l = string.join(string.split(filename,".dat"), ".orl")
# read and parse dat file into each file
# then merge the two files
# read orl file and write it to the merged file (except from the last $END
# keep up a way to know how much was read/written and then advance that amount
# on the orc file writing the remainer into the merged file
# delete the orc and orl files
# profit !!!

vecs=0
for line in gamess_us_dat_file:
	if myre_vec.search(line):
		vecs=1
		if localized :
			vecs=0
			localized=0
	if vecs : gamess_orb_file.write(line)
	if myre_end.search(line) and vecs == 1 :
		vecs=0
		if canonical == 1 : sys.exit()
	#
#
                    
