import requests
import untangle


def readNycOutages(url):
    doc = untangle.parse(url)
    return doc.NYCOutages.outage

def calculateRepairFraction(outages):
    noOfElements = len(outages)
    
    i=0
    noRepair = 0
    noTotal = 0
    while i < noOfElements:
        noTotal+=1
        if outages[i].reason.cdata == "REPAIR":
            noRepair+=1   
        i+=1
    return float(float(noRepair)/float(noTotal))
