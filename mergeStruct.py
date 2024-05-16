import pandas as pd
from typing import List
from GeneralHelperFunctions import secondstoHtz

class MergeObject:
    def __init__(self, unixStartTime: int, unixEndTime: int, filePath: str, headers:List[str], dataframeobj):
        self.unixStartTime = unixStartTime
        self.unixEndTime = unixEndTime
        self.filepath = filePath 
        self.headers = headers
        self.dataframeobj = dataframeobj

    def getHtz(self):
        numEntries:int = len(self.dataframeobj)
        self.htz = numEntries/(self.unixEndTime - self.unixStartTime)
        return self.htz

    




class MacroMerge:
    def __init__(self):
        self.maxHz = 0
        self.fileCount = 0
        self.MergeObjects: List[MergeObject] = []

    def append(self, item:MergeObject):
        self.MergeObjects.append(item)
        if(self.maxHz < item.getHtz()):
            self.maxHz = item.getHtz
        self.fileCount+=1

    

    



        


