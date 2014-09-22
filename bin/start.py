#! /usr/bin/env python

import sys

print "path=" + sys.path[0] + "/../lib"

sys.path.append(sys.path[0] + "/../lib")

print "sys.path[0]:   %s" % sys.path[0]
print "sys.path[0]:   ", sys.path[0]

#import testtttt
import Name.name

#name_obj = Name("my new name")

## Function definition
####################################################################################################
def print_values(var="abc", var2="variable2 default value"):
    print "in print_values. var=%s" % var
    print "var2=%s" % var2

## Main program
####################################################################################################
print "python\n";

variable = "aaaaa"
print "generated %s." % variable

print_values()
print_values("passed variable", "outside variable 2")


