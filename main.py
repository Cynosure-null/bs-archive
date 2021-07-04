#!usr/bin/env
# FOSSil is a program that automaticly archives websites in the background. Good for data hoarders like me.
import os

import toml

import mods

import time


#Fuck TOML. It does not go into dictionaries well.
#Loads the config file as a dictionary
filepath = os.path.expanduser("~/.config/fossil/config.toml")
cfg_file = toml.load(filepath)
#print(cfg_file) #debugging feature because I don't know how to use breakpoints
websites = cfg_file['links']
#print(sites)
act = cfg_file['action']
#print(act)
loop = cfg_file['time']
#print(loop)


#Removes that one fucking comma
websites = websites.replace("," , " ")
#spageitti code to split into strings
websites = str(websites)
websites = websites.strip()

websites = list(websites.split())

ct = -2 + len(websites)
websites = str(websites)
websites = websites.replace("," , " ")

while ct < 10:
    websites = websites + " localhost"
    ct = ct+1


s1,s2,s3,s4,s5,s6,s6,s7,s8,s8,s9,s10 = str.split(websites)

# I hate this.

s1 = s1.replace("[", "")
s1 = s1.replace("'", "")
s1 = s1.replace("]", "")

s2 = s2.replace("[", "")
s2 = s2.replace("'", "")
s2 = s2.replace("]", "")

s3 = s3.replace("[", "")
s3 = s3.replace("'", "")
s3 = s3.replace("]", "")

#---

s4 = s4.replace("[", "")
s4 = s4.replace("'", "")
s4 = s4.replace("]", "")

s5 = s5.replace("[", "")
s5 = s5.replace("'", "")
s5 = s5.replace("]", "")

s6 = s6.replace("[", "")
s6 = s6.replace("'", "")
s6 = s6.replace("]", "")

#--

s7 = s7.replace("[", "")
s7 = s7.replace("'", "")
s7 = s7.replace("]", "")

s8 = s8.replace("[", "")
s8 = s8.replace("'", "")
s8 = s8.replace("]", "")

s9 = s9.replace("[", "")
s9 = s9.replace("'", "")
s9 = s9.replace("]", "")

#---

s10 = s10.replace("[", "")
s10 = s10.replace("'", "")
s10 = s10.replace("]", "")

print(s1)
print("here")
loop = int(loop)
cycle = 0
while True:
    print("this will take a minute")
    cycle = cycle + 1
    mods.archive(s1)
    mods.archive(s2)
    mods.archive(s3)
    mods.archive(s4)
    mods.archive(s5)
    mods.archive(s6)
    mods.archive(s7)
    mods.archive(s8)
    mods.archive(s9)
    mods.archive(s10)
    cycle_num = "cycle {} completed."
    cycle_num = cycle_num.format(cycle)
    print(cycle_num)
    mods.cleanup()
    time.sleep(loop)
