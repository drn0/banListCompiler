# how to use this shit
- make sure u have pymongo
## starting w/ a mess of a data file
1. get any txt file with data split by spaces (words work). copy paste into thisWeek.txt. open data folder and open txtFix.py in an editor
2. comment out the last two "with" statement block, make sure all data is being written to fullDB
3. if not uncomment the "with" statment blocks
4. open fixStuff.py in your editor
5. replace data_file string with the data that isn't being added, yes there is a better way to do this no i dont care im sleepy
6. comment out first two with statements
7. run txtFix.py again. congrats ur db is done
## either moving on from that or starting from a data file seperated by lines
1. get a mongoDB server, choose connect via application, copy the string you get
2. open main.py in an editor
3. replace yourstring with the string, replace the password in that string with your password
4. enter dbname and collectionname
5. run