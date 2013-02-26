#!/usr/bin/env python
from falk.session2 import readNycOutages, calculateRepairFraction

@profile
def gettingData():
    outages = readNycOutages ("http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml")
    print "Fraction of the outages with reason REPAIR:",calculateRepairFraction(outages)

if __name__ == '__main__':
    gettingData()
