import os, sys, re

fileName = sys.argv[1]
fullFileName = fileName.replace(".log","")

with open(fileName) as f:

    for i in f:
        #Captures relevant fields of the access log
        ipAdd = re.search( r'(\d+.\d+.\d+.\d+)', i, re.M|re.I)
        dateStamp = re.search( r'(\d\d/\w\w\w/\d\d\d\d)', i, re.M|re.I)
        timeStamp = re.search( r'\d\d\d\d:(\d\d:\d\d:\d\d)', i, re.M|re.I)
        method = re.search( r'\"([A-Z]{3,7}) ', i, re.M|re.I)
        url = re.search( r'\"[A-Z]{3,7} \/(.+) HTTP/1\.[0-1]\"' , i, re.M|re.I)
        retCode = re.search( r'HTTP/1\.[0-1]\" (\d\d\d)', i, re.M|re.I)
        referrer = re.search( r'HTTP/1\.[0-1]\" \d\d\d .+ \"(.+)\" \"', i , re.M|re.I)
        userAgent = re.search( r'HTTP/1\.[0-1]\" \d\d\d .+ \".+\" \"(.+|)\"', i , re.M|re.I)

        #Captures MMM/YY format, creates a file name based on these values
        dateStampName = re.search( r'\d\d/(\w\w\w)/\d\d(\d\d)', i, re.M|re.I)
        newFileName = fullFileName + "_" + dateStampName.group(1) + dateStampName.group(2) + ".log"

        #Opens a new file based on the MMM/YY
        g = open(newFileName,'a')

        #If the file is empty the file will have a header added to it
        if os.path.getsize(newFileName) == 0:
            g.write("IPAddress|Datestamp|Timestamp|Method|URL|HTTPCode|Referrer|UserAgent")
            g.write("\n")

        #Writing to the new updated files
        g.write(ipAdd.group(1)+ "|" + dateStamp.group(1) + "|" + timeStamp.group(1) + "|" + method.group(1) + "|" + url.group(1) + "|" + retCode.group(1) + "|" + referrer.group(1) + "|" + userAgent.group(1))
        g.write("\n")
        g.close()
