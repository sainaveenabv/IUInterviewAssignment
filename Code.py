import pandas as pd
from datetime import datetime

FILE_NAME = "api.csv"
def convert_log_to_csv(path):
    file = pd.read_csv(path, sep=' ', header=None)
    file = file.dropna(axis=1)
    file.columns = ['Date', 'Time', 'Logger', 'Alert', 'Code', 'Log_Message']
    file['Combineddatetime'] = file['Date']+ ' '+ file['Time']
    file= file.groupby(['Code']).agg(
        {'Log_Message': lambda x: '-'.join(x), 'Combineddatetime': lambda x: '/'.join(x)})
    file[['Start_Time', 'End_Time']] = file['Combineddatetime'].str.split('/', 1, expand=True)
    file['S'] = pd.to_datetime(file['Start_Time'])
    file['E'] = pd.to_datetime(file['End_Time'])
    file['Time_diff']= file['E']-file['S']
    file['Time_diff']= file.Time_diff.dt.total_seconds()
    file.drop(['Combineddatetime','S','E'],axis=1,inplace=True)
    file.to_csv(FILE_NAME,index = False)

if __name__ == "__main__":
    convert_log_to_csv("api.log")
