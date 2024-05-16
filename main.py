from mergeStruct import MergeObject, MacroMerge
from ACQHelperFunctions import acqGetCount, acqGetChannels, acqDataFiller, acqTimepass
from typing import List
from pandas import DataFrame


print("Welcome to the lab Data Syncing Symposium")
print("You can add mergeStruct Objects in order to sync multiple files together, declare merge struct objects and given certain parameters, this should happen seamlessly")

# This will ultimately contain all the MergeObjects that you want to merge

m = MacroMerge()

## example, instantiating a MergeObject that contains an acknowledge file ##

## let's say that in the future that you don't have a Acqknowleddge file, this means that you can just get rid of the Acq file in the future ##

############################################################################



# headings are what seed the pandas dataframe for this information when we need it// we are seeding the heading with time
ACQheadings:List[str] = []
ACQheadings.append("time")
ACQchannels = []
ACQchannels.append(("time", "seconds"))

# Creating the fileptr to the Acqknowledge data file
filename = input("what is the name of your Acqknowledge file? (include extensions): ")
acq = open(filename)
print("Original File Name: " + acq.readline())

# seedings headings and channels (channels are headings but with the unit added)
acq.readline()
graph_start = acq.readline()[13:].strip()
acq.readline()
count = acqGetCount(acq)
acqGetChannels(ACQchannels, count, acq, ACQheadings)

# fills the dataframe up with data
acqDF:DataFrame = acqDataFiller(count, ACQheadings, filename)

#creates the correct timeshift according to the starting unix time

acqTimepass(acqDF, graph_start)

## This final object right here is the goal, we know have an object that can begin the sync proccess along with other objects that we might add to this in the future

acqOBJ:MergeObject = MergeObject(acqDF.loc[0, "time"], acqDF.loc[len(acqDF)-1, "time"], filename, ACQheadings, acqDF)

acqOBJ.acqDF.to_csv("test.csv", sep = ',', index = False, encoding = 'utf-8')


## append the object the the MacroMerge datastructure and then continue on with your journey
m.append(acqOBJ)



## next example, instatiating a merge object file that contains Hexoskin data, not that each hexoskin file is it's own file with it's own heading, so this will create multiple merge objects##

########################################################################################################

exit(0)


Hexoskinheadings:List[str] = []
Hexoskinchannels:List[str] = []












