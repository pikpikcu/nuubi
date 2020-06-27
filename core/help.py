#!/usr/bin/python

import sys,os,argparse
import requests, os, argparse, re
from plugins.modules import *
from core.banner import *

def help():
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-h","--help",dest="help",action="store_true")
        parser.add_argument("-b","--banner",dest="banner")
        parser.add_argument("-s","--subnet",dest="subnet")
        parser.add_argument("-c","--cms", dest="cms")
        parser.add_argument("-d","--dns", dest="dns")
        parser.add_argument("-e","--extract", dest="extract")
        parser.add_argument("-H","--http", dest="http")
        parser.add_argument("-n","--nmap", dest="nmap")
        parser.add_argument("-S","--subdo",dest="subdo")   
        parser.add_argument("-f","--find",dest="find")
        parser.add_argument("-u","--username", dest="username")
        parser.add_argument("-C","--crawl", dest="crawl")
        parser.add_argument("-w","--whois",dest="whois")
        parser.add_argument("-z","--zone",dest="zone")
        parser.add_argument("-r","--reverse", dest="reverse")

        parser.add_argument("--asn",dest="asn")
        parser.add_argument("--nping",dest="nping")   
        parser.add_argument("--cookie",dest="cookie")
        parser.add_argument("--revdns",dest="revdns")
        parser.add_argument("--cert",dest="cert")
        parser.add_argument("--url",dest="url")
        parser.add_argument("--response",dest="response")
        parser.add_argument("--exj",dest="exj")

        parser.add_argument("-T",dest="T")
        parser.add_argument("-ip",dest="ip")
        
        args = parser.parse_args()
        # help
        if args.help:
            banner()
            exit
        # Banner garbing
        if args.banner:
            banner(args.banner)
            exit()
        # Subnet
        if args.subnet:
            subnetlookup(args.subnet)
            exit()
        # CMS
        if args.cms:
            techno(args.cms)
            exit()
        # DNS
        if args.dns:
            dnslookup(args.dns)
            exit()
        # Extrack links
        if args.extract:
            extract(args.extract)
            exit()
        # Http header
        if args.http:
            httpheader(args.http)
            exit()
        # NMAP
        if args.nmap:
            nmap(args.nmap)
            exit()
        # subdomains
        if args.subdo:
            sub(args.subdo)
            exit()
        # finddns
        if args.find:
            findshareddns(args.find)
            exit()
        # github username
        if args.username:
            gitusers(args.username)
            gitemails(args.username)
            exit()
        # crawl
        if args.crawl:
            crawler(args.crawl)
            exit()
        # whois
        if args.whois:
            whois(args.whois)
            exit()
        # zonetransfer
        if args.zone:
            zone(args.zone)
            exit()
        # reversedns
        if args.reverse:
            reverseip(args.reverse)
            exit()

        if args.response:
            print("[+] Check code status response\n") 
            hosts(args.response)
            exit()

        if args.asn:
            aslookup(args.asn)
            exit()

        if args.cookie:
            cookie(args.cookie)
            exit()

        if args.exj:
            dirs(args.exj)
            exit()

        if args.nping:
            nping(args.nping)
            exit()

    
        if args.revdns:
            revdns(args.revdns)
            exit()
       
       # Certificate
        if args.cert:
            certspotter(args.cert)
            exit()
       
       
       # GeoIp
        if args.ip:
            geo(args.ip)
            exit() 
       
       
       # Check status dir 
 #       if args.R:
 #          print("[+] Check Dir Response")
 #          print("=======================")
 #          os.system('tput setaf 7')
 #          print("Status  |    site    ")
 #          os.system('tput setaf 9')
 #          respondir(args.R)
 #          exit()
       
       # scan web
        if args.url:
            urlscan(args.url)
            exit()
       # Traceroute
        if args.T:
            traceroute(args.T)
            exit()
       
       
        
