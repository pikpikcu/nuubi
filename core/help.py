#!/usr/bin/python

import sys,os,argparse
from plugins.modules import (traceroute,\
                             certspotter,\
                             urlscan,\
                             nmap,\
                             gitusers,\
                             gitemails,\
                             extract,\
                             banner,\
                             sub,\
                             geo,\
                             whois,\
                             dnslookup,\
                             subnetlookup,\
                             httpheader,\
                             techno)
#from plugins.modules import respondir

def help():
        parser = argparse.ArgumentParser()
        parser.add_argument('-b',help='Banner grabing of target ip address')
        parser.add_argument('-S',help='subnetlookup of target')
        parser.add_argument('-c', help='Cms detect with headers')
        parser.add_argument('--cert',help=('Certificate Transparency log monitor'))
        parser.add_argument('-d',help='Dnslookup of target domain')
        parser.add_argument('-e',help='Extract links from target url(https/http)')
        parser.add_argument('-ip',help='GeoIP lookup of target ip address')
        parser.add_argument('-H',help='Httpheaders of target url')
        parser.add_argument('-N',help='Nmapscan of target domain')
       # parser.add_argument('-R',help='Check Dir Response')
        parser.add_argument('--sub',help='Subdomain lookup of target domain')
        parser.add_argument('-T',help='Traceroute')
        parser.add_argument('--url',help='URL and website scanner for potentially malicious websites')
        parser.add_argument('--username', help='Github username of target')  
        parser.add_argument('--whois',help='Whois of target domain')   
        args = parser.parse_args()
       # Banner garbing
        if args.b:
            print("[+] Banner Grabing from target ip address\n")
            os.system('tput setaf 10')
            banner(args.b)
            exit()
       # Cdir
        if args.S:
            os.system('tput setaf 10')
            subnetlookup(args.S)
            exit()
       # CMS
        if args.c:
            print("[+] Detecting CMS with Identified Technologies and Custom Headers from target url\n")
            os.system('tput setaf 10')
            techno(args.c)
            exit()
       # Certificate
        if args.cert:
            print("[+]  Certificate Transparency log monitor\n")
            os.system('tput setaf 5')
            certspotter(args.cert)
            exit()
       # DNS
        if args.d:
            print("[+] DNS lookup of target domain\n")
            os.system('tput setaf 10')
            dnslookup(args.d)
            exit()
       # Extrack links
        if args.e:
            print("[+] Extracting all hidden and visiable links from target url\n")
            os.system('tput setaf 10')
            extract(args.e)
            exit()
       # GeoIp
        if args.ip:
            print("[+] Geoip lookup of target Ip address\n")
            os.system('tput setaf 10')
            geo(args.ip)
            exit() 
       # Http header
        if args.H:
            print("[+] Extracing http headers of target url\n")
            os.system('tput setaf 10')
            httpheader(args.H)
            exit()
       # NMAP
        if args.N:
            print("[+] Port scanning of target domain\n")
            os.system('tput setaf 10')
            nmap(args.N)
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
       # subdomains
        if args.sub:
            print("[+] Subdomain lookup from target domain\n")
            os.system('tput setaf 7')
            sub(args.sub)
            exit()
       # scan web
        if args.url:
            print("[+] Check url\n")
            os.system('tput setaf 6')
            urlscan(args.url)
            exit()
       # Traceroute
        if args.T:
            print("[+] Traceroute\n")
            os.system('tput setaf 6')
            traceroute(args.T)
            exit()
       # github username
        if args.username:
            gitusers(args.username)
            gitemails(args.username)
            exit()
       # whois
        if args.whois:
            print("[+] Whois lookup of target domain\n")
            os.system('tput setaf 7')
            whois(args.whois)
            exit()

        

        

        

        

        

        

        
        

        
