import csv
import io 
import urllib.request
import re
from datetime import datetime
import sys
import argparse

def downloadData(url):

    with urllib.request.urlopen(url) as response:
      downloaded_data = response.read().decode('utf-8')
      return downloaded_data
    


#url_data = downloadData("http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")
def processData(url_data):
    csv_data = csv.reader(io.StringIO(url_data))
    dataDict={}
    row_id=0
    for row in csv_data:
       

        path = row[0]
        datetime_accessed = row[1]
        browser = row[2]
        #need only time 
        time_accessed= datetime_accessed.split(' ')
        time=time_accessed[1]

        dataDict[int(row_id)]= (path,time,browser)
        row_id=row_id+1



def imageHit(dataDict):
    image_pattern = re.compile(r'\.(jpg|gif|png|jpeg|tiff|svg|bmp|)$', re.IGNORECASE)
    image_hits = 0
    for x in dataDict:
        file_name=dataDict[x][0]
        if re.search(image_pattern, file_name):
                image_hits += 1
    print(f"Image requests account for "+ str(image_hits/len(dataDict)* 100)+ " of all requests")

def browserHit(dataDict):

    firefox_pattern = r'Firefox'
    chrome_pattern = r'Chrome'
    ie_pattern = r'MSIE'
    safari_pattern = r'Safari'

    firefox_count = 0
    chrome_count = 0
    ie_count = 0
    safari_count = 0

    for x in dataDict:
        browser_name=dataDict[x][2]
        if re.search(firefox_pattern, browser_name):
                firefox_count += 1
        elif re.search(chrome_pattern, browser_name):
                chrome_count += 1
        elif re.search(ie_pattern, browser_name):
                ie_count += 1
        elif re.search(safari_pattern, browser_name):
                safari_count += 1

    print (f"Firefox Hits:{firefox_count}   Safari Hits:{safari_count}     MSIE Hits:{ie_count}      Chrome Hits:{chrome_count}")
    print("Chrome is the popular !!!!")



''' -------------------------------- Extra Credit -------------------------------------- '''


def timeHit(dataDict):

    newHitCount={"00":0,"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,
                "08":0,"09":0,"10":0,"10":0,"12":0,"13":0,"14":0,"15":0,
                "16":0,"17":0,"18":0,"19":0,"20":0,"21":0,"22":0,"23":0,
                }


    for x in dataDict:
            time = dataDict[x][1]
            
            hit_time = datetime.strptime(time, '%H:%M:%S')
            hour = str(hit_time.hour).zfill(2)
            

            newHitCount[hour] += 1

    sorted_count = sorted(newHitCount.items(), key=lambda x:x[1],reverse=True)
    #print(sorted_count)
    for x in sorted_count:
        print (f"Hour {x[0]} has {x[1]} Hits ")




def main(url) :

    downloadedData = downloadData(url)

    personData=processData(downloadedData)

    
    while True:
        print ("Please enter an ID to look up:")
        input_id=int(input())
        if input_id <= 0:
            print("Exiting the program.")
            sys.exit()
        else:
            displayPerson(input_id, personData)
    






if __name__ == "__main__":
     # url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="URL parameter without any double quotation")
    args = parser.parse_args()
    if args.url:
           main(args.url)
    else:
        print("URL Invalid. Exiting the program.")
        sys.exit()


'''


