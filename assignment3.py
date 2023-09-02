import csv
import io 
import urllib.request

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
        # i need only time 
        time_accessed= datetime_accessed.split(' ')
        time=time_accessed[1]

        dataDict[int(row_id)]= (path,time,browser)
        row_id=row_id+1

print(dataDict)
