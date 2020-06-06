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
                             techno,\
                             crawler,\
                             reverseip,\
                             revdns,\
                             zone)

#from plugins.modules import respondir

def help():
        parser = argparse.ArgumentParser()
        parser.add_argument('-b',
                            metavar='Banner',
                            help='Banner grabing of target ip address')
        parser.add_argument('-S',
                            metavar='subnetlookup',
                            help='subnetlookup of target')
        parser.add_argument('-c', 
                            metavar='',
                            help='Cms detect with headers')
        parser.add_argument('--cert',
                            metavar='Certificate',
                            help=('Certificate Transparency log monitor'))
        parser.add_argument('-d',
                            metavar='Dns',
                            help='Dnslookup of target domain')
        parser.add_argument('-e',
                            metavar='Extract',
                            help='Extract links from target url(https/http)')
        parser.add_argument('-ip',
                            metavar='GeoIP',
                            help='GeoIP lookup of target ip address')
        parser.add_argument('-H',
                            metavar='Httpheaders',
                            help='Httpheaders of target url')
        parser.add_argument('-N',
                            metavar='nmap',
                            help='Nmapscan of target domain')
       # parser.add_argument('-R',
       #                    metavar=''
       #                    help='Check Dir Response')
        parser.add_argument('--sub',
                            metavar='subdomain',
                            help='Subdomain lookup of target domain')
        parser.add_argument('-T',
                            metavar='traceroute',    
                            help='Traceroute')
        parser.add_argument('--url',
                            metavar='Url',
                            help='URL and website scanner for potentially malicious websites')
        parser.add_argument('--username', 
                            metavar='Username',
                            help='Github username of target')  
        parser.add_argument('--whois',
                            metavar='Whois',
                            help='Whois of target domain')
        parser.add_argument('--crawl', 
                            metavar='crawl',
                            help='crawler target url')   
        parser.add_argument('--reverse',
                            metavar='reverse',
                            help='reverse ip lookup')
        parser.add_argument('--revdns',
                            metavar='revdns',
                            help='reverse DNS')
        parser.add_argument('--zone',
                            metavar='zone',
                            help='zonetransfer, Retrieve DNS Zone')
        args = parser.parse_args()
        if args.revdns:
            print("[+] Reverse DNS from target ip address\n")
            os.system('tput setaf 10')
            revdns(args.revdns)
            exit()
        if args.zone:
            print("[+] Retrieve DNS Zone from target ip address\n")
            os.system('tput setaf 10')
            zone(args.zone)
            exit()
        if args.reverse:
            print("[+] Reverse IP Lookup from target ip address\n")
            os.system('tput setaf 10')
            reverseip(args.reverse)
            exit()
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
        if args.crawl:
            print("[+] crawler target url")
            os.system("tput setaf 7")
            crawler(args.crawl)
            exit()

        

        

        

        

        

        

        
        

        
