
### Parser for theA11yMachine
## Author: Eleonora Toscano, 2022

# Adds URL to each A11y Issue
# Removes all logging info

from operator import contains
import os

f = open(os.getcwd() + "/in/input.csv", "r")
fOut = open(os.getcwd() + "/out/output.csv", "w")

countRunLines = 0
currentURL = ""
runDivider = " Run: "
typeStr = '"type",'

for line in f:

    # AllyMachine Log info
    if not line.startswith('"'):

        if runDivider in line:
            # print(line)
            # get URL from "102/1000  Run: https://www.website/page1/."
            currentURL = line.split(runDivider,1)[1][:-2] 
            countRunLines += 1

    # A11y Issue and not header
    else:
        if not typeStr in line:
            # print(line)
            # add page to Ally Issue
            line = '"' + currentURL + '",' + line
            # print(line)
            fOut.write(line)


print("countRunLines: "+ str(countRunLines))
print("currentURL: "+ currentURL)

f.close()


fOut = open(os.getcwd() + "/out/output.csv", "r")
print(fOut.read())

fOut.close()