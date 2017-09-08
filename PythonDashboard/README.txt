Add SQLite directory to the root of C:\ (or append csvToSQL.py to change the directory to here)
Add the SQLite directory to the PATH environment variable

Install Python 2.7.x on the computer

Open a cmd window and cd to this directory
Use python largeFileSplitter.py access.log to split any file into smaller chunks (this is good for extremely large parameter files)
Use python logFileAnalyser.py access.log to split access.log into chunks based on the MMM/YY, this is somewhat slow at the moment - am looking to make more performant
Use python csvToSQLite.py access_MMMYY.log to add CSV into an SQLite database
