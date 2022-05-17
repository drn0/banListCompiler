import os.path
import sys
if not os.path.exists("data/thisWeek.txt"):
    sys.exit('read the instructions bro')
if not os.path.exists("fullDB.txt"):
    f = open("fullDB.txt", 'x')
if not os.path.exists("data/nonwithStanding.txt"):
    o = open("data/nonwithStanding.txt", 'x')
with open("data/thisWeek.txt",'r') as data_file:
    for line in data_file:
        data = line.split()
    data = data
with open("fullDB.txt", 'w') as data_base:
     for x in data:
        data_base.write("%s\n" % x)
with open("data/nonwithStanding.txt", 'r') as sexy:
    sexydata = []
    for line in sexy:
        sexydata.append(line.replace('\n', ''))
with open("fullDB.txt", 'a') as data_base2:
     for y in sexydata:
        data_base2.write("%s\n" % y)