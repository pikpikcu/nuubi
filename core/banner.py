#!/usr/bin/python

import sys

def logo():
    print("""

::::    ::: :::    ::: :::    ::: ::::::::: ::::::::::: 
:+:+:   :+: :+:    :+: :+:    :+: :+:    :+:    :+:     
:+:+:+  +:+ +:+    +:+ +:+    +:+ +:+    +:+    +:+     
+#+ +:+ +#+ +#+    +:+ +#+    +:+ +#++:++#+     +#+     
+#+  +#+#+# +#+    +#+ +#+    +#+ +#+    +#+    +#+     
#+#   #+#+# #+#    #+# #+#    #+# #+#    #+#    #+#     
###    ####  ########   ########  ######### ########### 
						[+] V1.0.0 
	
By pikpikcu & Rizsyad

github.com/pikpikcu
github.com/Rizsyad

""")

def banner():
    print("""
Options:    
       -h/--help       |  Show help message and exit

Arguments: 

        -b/--banner    | Banner grabing of target ip address
        -s/--subnet    | Subnetlookup of target       
        -c/--cms       | Cms detect with headers
        -d/--dns       | Dnslookup of target domain
        -e/--extract   | Extract links from target url(https/http)
        -H/--http      | Httpheaders of target url
        -n/--nmap      | Nmapscan of target domain
        -S/--sub       | Subdomain lookup of target domain
        -f/--find      | Find hosts sharing DNS servers
        -u/--username  | Github username of target
        -w/--whois     | Whois of target domain
        -C/--crawl     | Crawler target url
        -r/--reverse   | Reverse ip lookup
        -z/--zone      | zonetransfer, Retrieve DNS Zone
      
        --asn          | Check an Autonomous System Number (ASN)
        --nping        | nping, test Ping Response
        --cookie       | Cloudflare cookie scraper
        --revdns       | Reverse DNS
        --cert         | Certificate Transparency log monitor
        --url          | URL and website scanner for potentially malicious websites
        --response     | Check code status response
        --exj          | Extract GET parameters from javascript files

        -ip            | GeoIP lookup of target ip address 
        -T             | Traceroute
             
    """)