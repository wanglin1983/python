#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logger
import sys

print "sys.argv[0] : ", sys.argv[0]
for i in range(1, len(sys.argv)):
  print "Arg", i, sys.argv[i]

def main():
    print "Hello, world!"
    tokens = "I am fiser from Nanjing...".split()
    print len(tokens)
    print tokens
    str1 = "%d %f %s" % (1, 1.1, "fisher")
    print str1
    logger.info(str1)

if __name__ == '__main__':
    main()
