#!usr/bin/env
# FOSSil is a program that automaticly archives websites in the backround. Good for data hoarders like me.
import os
import time

import requests
import gzip
import datetime


def dl(url):
    http_url = "https://"+url
    r = requests.get(http_url, allow_redirects=True)
    r = r.content
    r = str(r)
    FileName = url
    open(FileName, 'w').write(r)

#dl("github.com")

def archive(url):
    http_url = "http://"+url
    r = requests.get(http_url, allow_redirects=True)
    r = r.content
    FileName = url
    FileName = str(FileName)
    FileName = FileName.replace('/', '-')
    _time = time.time()
    _time = str(_time)
    ArcName = _time + "_" + FileName+".html.bz"
    print(ArcName)
    f = gzip.open(ArcName, 'wb')
    f.write(r)
    move_it = "mv {} ~/FOSSil"
    move_it = move_it.format(ArcName)
    os.system(move_it)


def cleanup():
    os.system("rm ~/FOSSil/*_localhost.html.bz")

def init():
    os.system("mkdir ~/FOSSil")
    #FOSSil.arc is the directory for all fossil archived programs. .config/fossil is for congiguration
    os.system("mkdir ~/.config/fossil")
    os.system("echo title = '\"fossil config file\"' > ~/.config/fossil/config.toml")
    print("done")

