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
                             zone,\
                             nping,\
                             findshareddns,\
                             aslookup,\
                             cookie,\
                             hosts
                             )

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
        parser.add_argument('-f',
                            metavar='findshareddns',
                            help='Find hosts sharing DNS servers')
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
        parser.add_argument('--nping',
                            metavar='nping',
                            help='nping, test Ping Response')
        parser.add_argument('--AS',
                            metavar='aslookup',
                            help='Check an Autonomous System Number (ASN)')
        parser.add_argument('--cookie',
                            metavar='cookie',
                            help='Cloudflare cookie scraper')
        parser.add_argument('-v',
                            metavar='',
                            help='Check code status response')
       
        args = parser.parse_args()
        if args.v:
            hosts(args.v)
            exit()
        if args.cookie:
            cookie(args.cookie)
            exit()
        if args.AS:
            aslookup(args.AS)
            exit()
        if args.nping:
            nping(args.nping)
            exit()
        if args.f:
            findshareddns(args.f)
            exit()
        if args.revdns:
            revdns(args.revdns)
            exit()
        if args.zone:
            zone(args.zone)
            exit()
        if args.reverse:
            reverseip(args.reverse)
            exit()
       # Banner garbing
        if args.b:
            banner(args.b)
            exit()
       # Cdir
        if args.S:
            subnetlookup(args.S)
            exit()
       # CMS
        if args.c:
            techno(args.c)
            exit()
       # Certificate
        if args.cert:
            certspotter(args.cert)
            exit()
       # DNS
        if args.d:
            dnslookup(args.d)
            exit()
       # Extrack links
        if args.e:
            extract(args.e)
            exit()
       # GeoIp
        if args.ip:
            geo(args.ip)
            exit() 
       # Http header
        if args.H:
            httpheader(args.H)
            exit()
       # NMAP
        if args.N:
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
            sub(args.sub)
            exit()
       # scan web
        if args.url:
            urlscan(args.url)
            exit()
       # Traceroute
        if args.T:
            traceroute(args.T)
            exit()
       # github username
        if args.username:
            gitusers(args.username)
            gitemails(args.username)
            exit()
       # whois
        if args.whois:
            whois(args.whois)
            exit()
        if args.crawl:
            crawler(args.crawl)
            exit()
