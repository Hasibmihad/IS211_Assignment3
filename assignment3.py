import csv
import io 
import urllib.request
import re

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



 

