#!/usr/bin/env python
from falk.session2 import readNycOutages, calculateRepairFraction

outages = readNycOutages ("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
print "Fraction of the outages with reason REPAIR:",calculateRepairFraction(outages)
