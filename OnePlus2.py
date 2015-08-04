#!/usr/bin/python

import urllib, urllib2, cookielib, os
import time
import requests
import re
import csv


class OnePlus2:
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)       
    opener = urllib2.build_opener(cookie)
    myMsgs = []
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "PyFBept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "PyFBept-Language" : "en-us,en;q=0.5",
        "PyFBept-Charset" : "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "oneplus.net"
    }

    def hit(self, mail):
    	referral_code = '6GECS'
    	url = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&koid=" + referral_code + "&_=1438707525213&email="
    	url += mail
    	print url
    	dump = requests.get(url)
    	print dump
    	return   

def main():
	One2 = OnePlus2()
	mails = []
	i = 0
	# data.csv has emails in comma separated
	with open('data.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			mails = row
			print (row)
			break
	
	for mail in mails:
		i+=1
		print str(i) + " of " + str(len(mails)) + ": ",
		One2.hit(mail)
		time.sleep(7)

if __name__ == "__main__":
	main()