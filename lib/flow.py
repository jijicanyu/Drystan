# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from lib.common import initOptions, getIPs, sortNmapXML
from lib.interface import *
import sys
from lib.enums import TARGET_MODE
from config import ENABLE_WEBSOC


def startDomainFlow():
    if 'j1' not in sys.argv:
        whois()
        dig()
        theHarvester()
        DNSzoneTransfer()
        Sublist3r()
        SubDomainBrute()
    getIPs()

    if 'j2' not in sys.argv:
        Nmap()
    sortNmapXML()

    if 'j3' not in sys.argv:
        portScan()
        Hydra()

    if 'jweb' not in sys.argv:
        BBScan()
        if ENABLE_WEBSOC:
            WebSOC()


def startIpFlow():
    BingC()

    Nmap()
    sortNmapXML()
    portScan()

    BBScan()

    Hydra()
    if ENABLE_WEBSOC:
        WebSOC()