# IUInterviewAssignment
I have converted the given log file to CSV using Python3 Pandas. Python will read data from log file and will create a dataframe with rows equal to number of lines
present in the log file and columns equal to the number of fields present in a single line.

The first column in dataframe is indexing which is by default when a log file is read.

Based on the requirements the log message, start time,end time and the time difference are calculated.

Once the dataframe is created, it will be stored into a csv file format using Dataframe.to_csv()method
