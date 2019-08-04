#! python3
import re

def writeTo(fileName,fileContent):
    with open(fileName,"w+") as outfile:
        outfile.write(fileContent)
    return

def makeFile(branch):
    #schedTarget = "<div id=\"sched\"></div>"
    #schedule = schedDict[branch]

    with open("./index.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        #startIndex = [m.start() for m in re.finditer(schedTarget, refContent)]
        #lookLen = len(schedTarget)
        #endContent = refContent[:startIndex[0]]+schedule+refContent[(startIndex[0]+lookLen):]
        #return endContent
        return refContent
    return endContent

def generateBranch(branch):
    fileName = "index"+branch+".html"
    writeTo(fileName,makeFile(branch))
    return

def branchGeneration():
    branches = ["AST","BK","FP","JA","JH","OP","PCCH","RH","SS","SUT"]

    for x in branches:
        generateBranch(x)
    return

def test():
    generateBranch("PCCH")
    return

#test()
branchGeneration()
