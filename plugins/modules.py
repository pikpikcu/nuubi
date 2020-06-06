#!/usr/bin/python

import sys
import os
import json
import webtech
import re
import requests
import requests as res
from requests import get
from os import system
import shutil
from json import dumps

# Nuubi Modules
url = 'api.hackertarget.com'
#HACKERTARGET
def aslookup(target):
	print("[+] Start Check an Autonomous System Number (ASN)")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/aslookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def findshareddns(target):
	print("[+] Start Find hosts sharing DNS servers ")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/findshareddns/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def nping(target):
	print("[+] Start test Ping Response ")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/nping/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def zone(target):
	print("[+] Retrieve DNS Zone")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/zonetransfer/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def nmap(target):
	print("[+] Port scanning of target domain")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/nmap/",
							 params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def banner(target):
	print("[+] Start Banner Grabing ")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"bannerlookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def traceroute(target):
	print("[+] Start Traceroute")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/mtr/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def revdns(target):
	print("[+] Reverse DNS from target ip address")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/reversedns/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
def reverseip(target):
	print("[+] Reverse IP Lookup ")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/reverseiplookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
def whois(target):
	print("[+] Whois lookup of target domain")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/whois/",
							headers=headers, params=params)
	results = results.text.split('\n')
def geo(target):
	print("[+] Geoip lookup of target Ip address")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/geoip/",
							headers=headers, params=params)
	results = results.text.split('\n')
def dnslookup(target):
	print("[+] DNS lookup of target domain")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/dnslookup/",
							headers=headers, params=params)
	results = results.text.split('\n')
def subnetlookup(target):
	print("[+] Start subnetlookup")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/subnetcalc/",
							headers=headers, params=params)
	results = results.text.split('\n')
def sub(target):
	print("[+] Subdomain lookup from target domain")
	print("[+] Target: "+target)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/hostsearch/",
							headers=headers, params=params)
	results = results.text.split('\n')
	print(*results, sep = "\n")
	
def extract(target):
	print("[+] Extracting all hidden and visiable links")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/pagelinks/",
							headers=headers, params=params)
	results = results.text.split('\n')
def httpheader(target):
	print("[+] Extracing http headers of target url")
	print("[+] Target: "+target)
	
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
	params = (('q', target),)

	results = requests.get("https://"+url+"/httpheaders/",
							headers=headers, params=params)
	results = results.text.split('\n')
####
def certspotter(url):
	print("[+]  Certificate Transparency log monitor")
	print("[+] Target: "+url)
	target = res.get('https://api.certspotter.com/v1/issuances?domain='+url+'&expand=dns_names&expand=issuer&expand=cert | jq ".[].dns_names[]" | sed "s/\"//g" | sed "s/\*\.//g" | sort -u | grep '+url).text
	data = json.loads(target)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)
def urlscan(url):
	print("[+] Target: "+url)
	response = res.get('https://urlscan.io/api/v1/search/?q=domain:'+url).text
	data = json.loads(response)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)
def gitusers(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print("[+] Dumping Sensitive information from github")
	os.system('tput setaf 9')
	print("[+] Name : ", str(data['name']))
	print("[+] Location : ", str(data['location']))
	print("[+] ID : ", str(data['id']))
	print("[+] Website : ", str(data['blog']))
	print("[+] Number of public github Repository : " ,str(data['public_repos']))
	print("[+] Number of public gist Repository : ",str(data['public_gists']))
def gitemails(username):
	try:
		response = res.get("https://api.github.com/users/%s/events/public" %(username))
		jsn = response.json()
		data = jsn[0]
		dump = data["payload"]["commits"][0]["author"]["email"]
		print("[+] Email data : ", dump)	
	except KeyError:
		os.system('tput setaf 12')
		print("[+] Aww Snap Unable to find out the email address!")


#def respondir(target):
#    os.system("tput setaf 6")
#    os.system("echo "+target+ "| hakrawler -plain | hakcheckurl | grep -v 404")

def crawler(url):
    content = get(url).text
    regex_title = re.compile(r"<title>(.*?)<\/title>")
    title = re.findall(regex_title, content)

    regex_links = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    link = re.findall(regex_links, content)

    robots = get(url + "/robots.txt").text
	
    print("Title: "+ ''.join(title) + "\n")
    print("extract links: \n" + '\n'.join(link) + "\n")
    print("robots.txt: \n" + robots)
def techno(url):
	print("[+] Detecting CMS with Identified Technologies and Custom Headers from target url\n")
	print("[+] Target: "+url)
	obj = webtech.WebTech()
	results = obj.start_from_url(url, timeout=1)
	system('tput setaf 9')
	sys.stdout.write(results)

