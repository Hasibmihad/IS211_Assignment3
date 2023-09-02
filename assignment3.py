import csv
import io 
import urllib.request

def downloadData(url):

    with urllib.request.urlopen(url) as response:
      downloaded_data = response.read().decode('utf-8')
      return downloaded_data
    


url_data = downloadData("http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")
csv_data = csv.reader(io.StringIO(url_data))
for row in csv_data:
        # Extract values for each column
        path_to_file = row[0]
        datetime_accessed = row[1]
        browser = row[2]
        status_of_request = row[3]
        request_size_bytes = row[4]
        
        # Perform any processing or analysis on the data here
        # For example, you can print the values for each row
        print(f"Path: {path_to_file}, Datetime: {datetime_accessed}, Browser: {browser}, Status: {status_of_request}, Size: {request_size_bytes}")