#!/usr/bin/python

import time

DONE = '/Users/chbaker/Dropbox/todo/done.txt'
GEEKNOTE = '/usr/local/bin/geeknote'
PREFIX = 'x '

today = time.strftime("%Y-%m-%d")

search_string = PREFIX + today

count = 0

body = ""

with open(DONE, 'r') as done_file:
    for line in done_file:
        if line.startswith(search_string):
            body += line[2:].strip()
            count += 1

# Debug
#print "{} tasks completed {}".format(count, today)
title = "{} tasks completed {}".format(count, today)
