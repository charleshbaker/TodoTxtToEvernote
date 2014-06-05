#!/usr/bin/env python
'''
Parse a done.txt file in the format of Gina Trapani's todo.txt application for
items done $TODAY. Concatenate those items in a string and use Geeknote to
create a note in Evernote with those items as the body.
'''

# TODO Accept command line arguments but set reasonable defaults
# TODO Create a usage function

# Import python libs
import time
import subprocess

# Constants
DONE = '/Users/chbaker/Dropbox/todo/done.txt'
GEEKNOTE = '/usr/local/bin/geeknote'
PREFIX = 'x '
NOTEBOOK = 'Done'

today = time.strftime('%Y-%m-%d')
search_string = PREFIX + today
count = 0
body = ''

with open(DONE, 'r') as done_file:
    for line in done_file:
        if line.startswith(search_string):
            body += line[13:].rstrip() + '\n'
            count += 1

ARGS = ' create --title "' + str(count) + ' tasks completed ' + today + \
  '" --content "' + body + '" --notebook ' + NOTEBOOK

subprocess.call(GEEKNOTE + ARGS, shell = True)
