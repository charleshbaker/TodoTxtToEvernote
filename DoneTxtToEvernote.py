#!/usr/bin/env python
'''
Parse a done.txt file in the format of Gina Trapani's todo.txt application for
items done $TODAY. Concatenate those items in a string and use Geeknote to
create a note in Evernote with those items as the body.
'''


# Import python libs
from optparse import OptionParser
import subprocess
import time

def debug(mystring):
    print mystring
    
debugOn = True

usage = 'usage: %prog [options]'
    
parser = OptionParser()

parser.set_defaults(done='/Users/chbaker/Dropbox/todo/done.txt')
parser.set_defaults(geeknote='/usr/local/bin/geeknote')
parser.set_defaults(notebook='DONE')

parser.add_option('-f',
                '--file',
                help='Path to done.txt',
                action='store',
                type='string',
                dest='done',
                metavar='DONE'
                    )
                    
parser.add_option('-g',
                '--geeknote',
                help='Path to geeknote',
                action='store',
                type='string',
                dest='geeknote',
                metavar='GEEKNOTE'
                    )
                    
parser.add_option('-n',
                '--notebook',
                help='Destination notebook',
                action='store',
                type='string',
                dest='notebook',
                metavar='NOTEBOOK'
                    )
                    
(options, args) = parser.parse_args()

if (debugOn):
    debug(options.done)
    debug(options.geeknote)
    debug(options.notebook)    

# Constant
PREFIX = 'x '

today = time.strftime('%Y-%m-%d')
searchString = PREFIX + today
count = 0
body = ''

with open(options.done, 'r') as doneFile:
    for line in doneFile:
        if line.startswith(searchString):
            body += line[13:]
            count += 1

geeknoteArgs = ' create --title "' + str(count) + ' tasks completed ' + today + \
  '" --content "' + body + '" --notebook "' + options.notebook + '"'

if (debugOn):
    debug(geeknoteArgs)

if (!debugOn):    
    subprocess.call(GEEKNOTE + ARGS, shell = True)
