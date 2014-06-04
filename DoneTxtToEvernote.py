#!/usr/bin/python

import time
import subprocess

DONE = '/Users/chbaker/Dropbox/todo/done.txt'
GEEKNOTE = '/usr/local/bin/geeknote'
PREFIX = 'x '
NOTEBOOK = 'Done'

today = time.strftime("%Y-%m-%d")

search_string = PREFIX + today

count = 0

body = ""

with open(DONE, 'r') as done_file:
    for line in done_file:
        if line.startswith(search_string):
            body += line[2:].rstrip()
            count += 1

ARGS = ' create --title "' + str(count) + ' tasks completed ' + today +
  '" --content "' + body + '" --notebook ' + NOTEBOOK

subprocess.call(GEEKNOTE + ARGS, shell = True)
