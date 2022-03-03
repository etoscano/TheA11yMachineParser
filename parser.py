
### Parser for theA11yMachine
## Author: Eleonora Toscano, 2022

# Adds URL to each A11y Issue
# Removes all logging info

from operator import contains
import os
import Database

def getWCAGType(guidelineNum):
    return "2.2" if guidelineNum in Database.WCAG2_2 else "2.1"

def getWCAGLevel(guidelineNum):

    if guidelineNum in Database.A:
        return "A"
    elif guidelineNum in Database.AA:
        return "AA"
    elif guidelineNum in Database.AAA:
        return "AAA"
    else:
        return "No WCAG Level found"    


inputFolder = os.getcwd() + "/in/input.csv"
outputFolder = os.getcwd() + "/out/output.csv"

f = open(inputFolder, "r")
fOut = open(os.getcwd() + "/out/output.csv", "w")

countLines = 0
countURLs = 0
countIssues = 0
countHeaderLines = 0
countLogInfo = 0
currentURL = ""
runDivider = " Run: "
typeStr = '"type",'

for line in f:
    countLines += 1

    # AllyMachine Log info
    if not line.startswith('"'):

        if runDivider in line:
            # Get URL from "102/1000  Run: https://www.website/page1/."
            currentURL = line.split(runDivider,1)[1][:-2] 
            countURLs += 1
        else:
            countLogInfo += 1

    # A11y Issue or Headers ("type","code","message","context","selector")
    else:
        # A11y Issue
        if not typeStr in line:
            countIssues += 1
            # Remove first and last character
            line = line[1:-2]

            # Split Ally Issue by headers
            splittedLine = line.split('","')
 
            # type = splittedLine[0]
            code = splittedLine[1]
            message = splittedLine[2]
            context = splittedLine[3]
            # selector = splittedLine[4]

            # Get WCAG guideline
            guidelineNum = code.split(".")[3].replace("_",".")

            if guidelineNum in Database.guidelines:
                g = Database.guidelines.get(guidelineNum)
                title = g[0]
                link = g[1]

            macroareaNum = guidelineNum[:-1] 
            if macroareaNum in Database.macroareas:
                macroarea = Database.macroareas.get(macroareaNum)

            formattedLine = ('"' +
            currentURL + '","' +
            guidelineNum + ' ' + title +'","' +
            '=HYPERLINK(""'+link + '"";""' + '"LINK")' +',"' +
            macroarea + '","' +
            getWCAGLevel(guidelineNum) + '","' +
            getWCAGType(guidelineNum) + '","' +
            'TO DO' + '","' +
            message + '","' +
            context +
            '"\n')

            fOut.write(formattedLine)

        else:
            countHeaderLines += 1

# Print last formatted line to check stuff
# print(formattedLine)

print("\nSuccess! Parsing complete.")
print("The output file can be found here: "+ outputFolder + " \n")

print("------  Lines in Input file: "+ str(countLines) + "  ------")
print("---  Number of URLs: "+ str(countURLs))
print("---  Accessibility Issues: "+ str(countIssues))
print("- Header Lines: "+ str(countHeaderLines) +" | Log Info Lines: "+ str(countLogInfo) + "")

f.close()


fOut = open(outputFolder, "r")
# print(fOut.read())

fOut.close()

