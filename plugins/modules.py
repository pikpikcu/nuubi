#!/usr/bin/python

import urllib.request
import urllib.parse
import sys
import os
import json
import webtech
import re
import requests
import cfscrape
import bs4
import requests as res
from requests import get
from bs4 import BeautifulSoup
from os import system
import shutil
from json import dumps

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class bcolors:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
# Nuubi Modules
url = 'api.hackertarget.com'
#HACKERTARGET
def aslookup(target):
	print(bcolors.green+"[+] Start Check an Autonomous System Number (ASN)")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/aslookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def findshareddns(target):
	print(bcolors.green+"[+] Start Find hosts sharing DNS servers ")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/findshareddns/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def nping(target):
	print(bcolors.green+"[+] Start test Ping Response ")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/nping/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def zone(target):
	print(bcolors.green+"[+] Retrieve DNS Zone")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/zonetransfer/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def nmap(target):
	print(bcolors.green+"[+] Port scanning of target domain")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/nmap/",
							 params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def banner(target):
	print(bcolors.green+"[+] Start Banner Grabing ")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/bannerlookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def traceroute(target):
	print(bcolors.green+"[+] Start Traceroute")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/mtr/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def revdns(target):
	print(bcolors.green+"[+] Reverse DNS from target ip address")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/reversedns/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def reverseip(target):
	print(bcolors.green+"[+] Reverse IP Lookup ")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/reverseiplookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def whois(target):
	print(bcolors.green+"[+] Whois lookup of target domain")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/whois/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def geo(target):
	print(bcolors.green+"[+] Geoip lookup of target Ip address")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/geoip/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def dnslookup(target):
	print(bcolors.green+"[+] DNS lookup of target domain")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/dnslookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def subnetlookup(target):
	print(bcolors.green+"[+] Start subnetlookup")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/subnetcalc/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def sub(target):
	print(bcolors.green+"[+] Subdomain lookup from target domain")
	print("[+] Target: ",bcolors.red, target)
	print(bcolors.green+"[+] Starting Hackertarget...", bcolors.lightcyan)
	domains= set(target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/hostsearch/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
	print("\n[+] Starting Crt.sh...")
	with urllib.request.urlopen('https://crt.sh/?output=json&q=' + urllib.parse.quote('%.' + target)) as f:
         data = json.loads(f.read().decode('utf-8'))
         for crt in data:
                for domain in crt['name_value'].split('\n'):
                    if not domain in domains:
                        domains.add(domain)
                        print(domain)

	
def extract(target):
	print(bcolors.green+"[+] Extracting all hidden and visiable links")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/pagelinks/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def httpheader(target):
	print(bcolors.green+"[+] Extracing http headers of target url")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("http://"+url+"/httpheaders/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
####
def certspotter(target):
	print(bcolors.green+"[+] Certificate Transparency log monitor")
	print("[+] Target: ",bcolors.red, target, bcolors.lightcyan)
	try:
		headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
		results = requests.get('https://api.certspotter.com/v1/issuances?domain='+target+'&expand=dns_names&expand=issuer&expand=cert | jq ".[].dns_names[]" | sed "s/\"//g" | sed "s/\*\.//g" | sort -u | grep '+target,headers=headers)
		results = results.text.split('\n')
		print(*results, sep = "\n")
	except KeyError:
		os.system('tput setaf 12')
		print("[+] Error!")
def urlscan(url):
	print(bcolors.green+"[+] Check url")
	print("[+] Target: ",bcolors.red, url, bcolors.lightcyan)
	response = res.get('https://urlscan.io/api/v1/search/?q=domain:'+url).text
	data = json.loads(response)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)
def gitusers(username):
	print(bcolors.yellow+"[+] Dumping Sensitive information from github")
	print("[+] Target: ",bcolors.red, username, bcolors.lightcyan)
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print(bcolors.green+"[+] Name : ",bcolors.cyan, str(data['name']))
	print(bcolors.green+"[+] Location : ",bcolors.cyan, str(data['location']))
	print(bcolors.green+"[+] ID : ",bcolors.cyan, str(data['id']))
	print(bcolors.green+"[+] Website : ",bcolors.cyan, str(data['blog']))
	print(bcolors.green+"[+] Number of public github Repository : " ,bcolors.cyan, str(data['public_repos']))
	print(bcolors.green+"[+] Number of public gist Repository : ",bcolors.cyan, str(data['public_gists']))
def gitemails(username):
	try:
		response = res.get("https://api.github.com/users/%s/events/public" %(username))
		jsn = response.json()
		data = jsn[0]
		dump = data["payload"]["commits"][0]["author"]["email"]
		print(bcolors.green+"[+] Email data : ",bcolors.cyan, dump)	
	except KeyError:
		os.system('tput setaf 12')
		print("[+] Aww Snap Unable to find out the email address!")

#def respondir(target):
#    os.system("tput setaf 6")
#    os.system("echo "+target+ "| hakrawler -plain | hakcheckurl | grep -v 404")

def crawler(url):
	print(bcolors.green+"[+] Start crawler")
	print("[+] Target: ",bcolors.red, url, bcolors.lightcyan)
	try:
		content = get(url).text
		regex_title = re.compile(r"<title>(.*?)<\/title>")
		title = re.findall(regex_title, content)

		regex_links = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
		link = re.findall(regex_links, content)

		robots = get(url + "/robots.txt").text
		
		print("Title: "+ ''.join(title) + "\n")
		print("extract links: \n" + '\n'.join(link) + "\n")
		print("robots.txt: \n" + robots)
	except KeyError:
		pass
def techno(url):
	print(bcolors.green+"[+] Detecting CMS with Identified Technologies and Custom Headers from target url\n")
	print("[+] Target: ",bcolors.red, url, bcolors.lightcyan)
	obj = webtech.WebTech()
	results = obj.start_from_url(url, timeout=1)
	sys.stdout.write(results)
def cookie(url):
	sess = cfscrape.create_scraper()
	try:
		print(bcolors.green+"[+] Cloudflare cookie scraper ")
		print("[+] Target: ",bcolors.red, url, bcolors.lightcyan)
		request = "GET / HTTP/1.1\r\n"
		cookie_value, user_agent = cfscrape.get_cookie_string(url)
		request += "Cookie: %s\r\nUser_Agent: %s\r\n" % (cookie_value, user_agent)
		data = sess.get(url)
		out = BeautifulSoup(data.content,'html.parser')
		print("[+] Print Cookie\n")
		print(request)
		os.system('tput setaf 10')
		print("\n[+] Scraper ")
		print(out)
	except KeyError:
		pass
def hosts(host):
    host = host.split()[0]    
    try:             
        r = requests.get("http://"+host, verify=False)       
        html=bs4.BeautifulSoup(r.text,features="html.parser")               
        status_code = str(r.status_code)              
        length = str(len(r.text))              
        title = html.title.text               
        print(bcolors.orange+'  Url:',bcolors.cyan ,host,'\n',bcolors.orange,'Status-Code:',bcolors.cyan, status_code,'\n',bcolors.orange,'Respon-Lenght:',bcolors.cyan, length,'\n',bcolors.orange,'Title:',bcolors.cyan, title,'\n')
		      
    except KeyError:                
           pass
def regex(content):
    pattern = "(\"|')(\/[\w\d?\/&=#.!:_-]{1,})(\"|')"
    matches = re.findall(pattern, content)
    response = ""
    i = 0
    for match in matches:
        i += 1
        if i == len(matches):
            response += match[1]
        else:
            response += match[1] + "\n"
    return(response)
def dirs(url):
		print(bcolors.green+"[+] Extract GET parameters from javascript files\n")
		try:
			dirs = "http://" + url
			url = dirs + "/"
			r = requests.get(url, verify=False)
			soup = BeautifulSoup(r.text, 'html5lib')
			scripts = soup.find_all('script')
			linkArr = [dirs]
			dirArr = []
			for script in scripts:
				try:
					if script['src'][0] == "/" and script['src'][1] != "/":
						script = url.split("/")[0:2] + script['src']
						linkArr.append(script)
					else:
						pass
				except:
					pass
			for link in linkArr:
				res = requests.get(link, verify=False)
				out = regex(res.text).split("\n")
				for line in out:
					pathArr = line.strip().split("/")
					path = ""
					for i in range(len(pathArr)):
						if i == len(pathArr) - 1:
							if "." in pathArr[i]:
								pass
							else:
								path += pathArr[i] + "/"
						else:
							path += pathArr[i] + "/"
					if path != "/" and path != "//":
						dirArr.append(path.replace("//", "/").split("#")[0])
					else:
						pass
			for directory in list(set(dirArr)):
					print(directory)
		except:
			pass
