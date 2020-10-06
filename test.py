#!/usr/bin/python

import os
import sys
import yum

yb = yum.YumBase()
yb.setCacheDir()

results = yb.pkgSack.returnNewestByNameArch(patterns=["python", “perl”])

for pkg in results:
    print "%s %s (%s) \n\t%s" % (pkg.name, pkg.version, pkg.arch, pkg.summary)


plist = yb.rpmdb.returnPackages()
l_plist = [p for p in plist if p.size > 1024 * 1024 * 10]
print "Installed packages with size > 10MB:"
for p in l_plist:
    print "%s: %sMB" % (pkg, pkg.size / (1024 * 1024))



