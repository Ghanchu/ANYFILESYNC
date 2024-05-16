import pandas as pd
from typing import TextIO, List
import pytz
from datetime import datetime

# create the pandas dataframe with all the info that you need

def acqDataFiller(count:int, headers:List[str], filename:str):
    print(headers)
    df = pd.read_csv(filename, header = None, skiprows = 7 + int(count) * 2, names = headers, index_col=False)
    df.set_index("time")
    return df

# turns the graph start time into a unix time value that we can add to every value in the time graph, for the purposes of the merging proccess

def acqTimepass(df, graph_start):
    parts = graph_start.split('-')
    dates = []
    for part in parts:
        dates.append(part)
    year = dates[0]
    month = dates[1]
    parts = dates[2].split(' ')
    dates.pop(2)
    for part in parts:
        dates.append(part)
    day = dates[2]
    parts = dates[3].split(':')
    dates.pop(3)
    for part in parts:
        dates.append(part)
    hour = dates[3]
    minute = dates[4]
    parts = dates[5].split('.')
    dates.pop(5)
    for part in parts:
        dates.append(part)
    second = dates[5]
    millisecond = dates[6]
    print("Please note that the Hexoskin, Research Ring merging proccess assumes that recordings took place in the same timezone as the other devices. To modify the timezones change the line below this print statement to the appropriate timezone")
    resolved_timezone = pytz.timezone('EST')
    resolveddate = resolved_timezone.localize(datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(millisecond) * 1000))
    unixtime = int(resolveddate.timestamp())
    unixtime = unixtime + int(millisecond)/1000
    df["time"] = df["time"] + unixtime

def acqGetChannels(channels, count: int, acq: TextIO, headings: List[str]):
    count = int(count)
    for i in range(count):
        main = acq.readline()
        unit = acq.readline()
        pair = (main, unit)
        channels.append(pair)
        headings.append(main)

# number of channels    
        
def acqGetCount(acq: TextIO):
    count = acq.readline(1)
    acq.readline()
    print("The number of acqknowledge channels is " + count)
    return count

