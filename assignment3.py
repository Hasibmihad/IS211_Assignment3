import csv
import io 
import urllib.request
import re
from datetime import datetime


def downloadData(url):

    with urllib.request.urlopen(url) as response:
      downloaded_data = response.read().decode('utf-8')
      return downloaded_data
    


url_data = downloadData("http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")
csv_data = csv.reader(io.StringIO(url_data))
dataDict={}
row_id=0
for row in csv_data:
        # Extract values for each column

        path = row[0]
        datetime_accessed = row[1]
        browser = row[2]
        #need only time 
        time_accessed= datetime_accessed.split(' ')
        time=time_accessed[1]

        dataDict[int(row_id)]= (path,time,browser)
        row_id=row_id+1

#print(dataDict)
image_pattern = re.compile(r'\.(jpg|gif|png|jpeg|tiff|svg|bmp|)$', re.IGNORECASE)
total_hits = 0
image_hits = 0
for x in dataDict:
     #total_hits += 1
     file_name=dataDict[x][0]
     if re.search(image_pattern, file_name):
            image_hits += 1


print(f"Image requests account for "+ str(image_hits/len(dataDict)* 100)+ " of all requests")



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
newHitCount={}
for x in dataDict:
        time = dataDict[x][1]
        
       
        hit_time = datetime.strptime(time, '%H:%M:%S')
        hour = hit_time.hour
        
        # Update the hit count for the corresponding hour
        hourly_hits[hour] += 1







'''






def main(url) :

    logger=loggerSetup()

    downloadedData = downloadData(url,logger)

    personData=processData(downloadedData,logger)

    
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


