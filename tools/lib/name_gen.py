#!/usr/bin/env python
## -*- python -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from os.path import abspath, join, dirname
import random

full_path = lambda filename: abspath(join(dirname(__file__), filename))

def get_name(filename):
	with open(filename) as afile:
	    line = next(afile)
	    for num, aline in enumerate(afile):
	      if random.randrange(num + 2): continue
	      line = aline
	    return line
    # selected = random.random() * 90
    # with open(filename) as name_file:
    #     for line in name_file:
    #         name, _, cummulative, _ = line.split()
    #         if float(cummulative) > selected:
    #             return name
    # return ""  # Return empty string if file is empty


def get_adjective():
    return get_name(full_path('adjectives')).strip()

def get_noun():
    return get_name(full_path('nouns')).strip()

def get_rand():
	return random.randint(100, 999)

def get_full_name():
    return "{0}-{1}-{2}".format(get_adjective(), get_noun(), get_rand())

if __name__ == "__main__":
    print get_full_name()