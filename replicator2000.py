#! python3
import re

def writeTo(fileName,fileContent):
    with open(fileName,"w+") as outfile:
        outfile.write(fileContent)
    return

def findAll(lookup,refContent,tag):
    startIndices = [m.start() for m in re.finditer(lookup, refContent)]
    indexPairs = []
    lookLength = len(lookup)
    for elem in startIndices:
        indexPairs.append((elem,elem+lookLength,tag))
    return indexPairs

def orderIndices(arr,arrLen):
    key = None
    for i in range(1,arrLen):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# input ex. : "Astoria", "Floral-Park"
# output: index.html with replaced titleString
def makeFile(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    bannerString = "\" class=\"logo\">SAT <span>"
    indexLink = "index.html"
    hallLink = "templates/halloffame.html"
    mentorLink = "templates/mentorship.html"
    progLink = "templates/programs.html"
    faqLink = "templates/satfaqs.html"
    newBString = bannerString.replace("SAT",nbrhood.replace('-',' ')+" SAT")
    newIString = "./"+nbrhood+".html"
    newHString = "./nbrhoodHoF/halloffame_"+nbrhood+".html"
    newMString = "./nbrhoodMtrshp/mentorship_"+nbrhood+".html"
    newPString = "./nbrhoodProgs/programs_"+nbrhood+".html"
    newFString = "./nbrhoodFaqs/satfaqs_"+nbrhood+".html"

    insertDict = {
        'b' : newBString,
        'i' : newIString,
        'h' : newHString,
        'm' : newMString,
        'p' : newPString,
        'f' : newFString
    }
    with open("./index.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        bIndices = findAll(bannerString,refContent,'b')
        iIndices = findAll(indexLink,refContent,'i')
        hIndices = findAll(hallLink,refContent,'h')
        mIndices = findAll(mentorLink,refContent,'m')
        pIndices = findAll(progLink,refContent,'p')
        fIndices = findAll(faqLink,refContent,'f')
        allIndices = bIndices+iIndices+hIndices+mIndices+pIndices+fIndices
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
        return endContent
    return endContent

# Subpage generators : can compress into one function, then pass a dictionary/array of corresponding strings

def makeHallofFame(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    bannerString = "\" class=\"logo\">SAT <span>"
    indexLink = "../index.html"
    hallLink = "halloffame.html"
    mentorLink = "mentorship.html"
    progLink = "programs.html"
    faqLink = "satfaqs.html"
    newBString = bannerString.replace("SAT",nbrhood.replace('-',' ')+" SAT")
    newIString = "../"+nbrhood+".html"
    newHString = "./halloffame_"+nbrhood+".html"
    newMString = "../nbrhoodMtrshp/mentorship_"+nbrhood+".html"
    newPString = "../nbrhoodProgs/programs_"+nbrhood+".html"
    newFString = "../nbrhoodFaqs/satfaqs_"+nbrhood+".html"

    insertDict = {
        'b' : newBString,
        'i' : newIString,
        'h' : newHString,
        'm' : newMString,
        'p' : newPString,
        'f' : newFString
    }
    with open("./templates/halloffame.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        bIndices = findAll(bannerString,refContent,'b')
        iIndices = findAll(indexLink,refContent,'i')
        hIndices = findAll(hallLink,refContent,'h')
        mIndices = findAll(mentorLink,refContent,'m')
        pIndices = findAll(progLink,refContent,'p')
        fIndices = findAll(faqLink,refContent,'f')
        allIndices = bIndices+iIndices+hIndices+mIndices+pIndices+fIndices
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
        return endContent

def makeMentorship(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    bannerString = "\" class=\"logo\">SAT <span>"
    indexLink = "../index.html"
    hallLink = "halloffame.html"
    mentorLink = "mentorship.html"
    progLink = "programs.html"
    faqLink = "satfaqs.html"
    newBString = bannerString.replace("SAT",nbrhood.replace('-',' ')+" SAT")
    newIString = "../"+nbrhood+".html"
    newHString = "../nbrhoodHoF/halloffame_"+nbrhood+".html"
    newMString = "./mentorship_"+nbrhood+".html"
    newPString = "../nbrhoodProgs/programs_"+nbrhood+".html"
    newFString = "../nbrhoodFaqs/satfaqs_"+nbrhood+".html"

    insertDict = {
        'b' : newBString,
        'i' : newIString,
        'h' : newHString,
        'm' : newMString,
        'p' : newPString,
        'f' : newFString
    }
    with open("./templates/mentorship.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        bIndices = findAll(bannerString,refContent,'b')
        iIndices = findAll(indexLink,refContent,'i')
        hIndices = findAll(hallLink,refContent,'h')
        mIndices = findAll(mentorLink,refContent,'m')
        pIndices = findAll(progLink,refContent,'p')
        fIndices = findAll(faqLink,refContent,'f')
        allIndices = bIndices+iIndices+hIndices+mIndices+pIndices+fIndices
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
        return endContent

def makePrograms(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    bannerString = "\" class=\"logo\">SAT <span>"
    indexLink = "../index.html"
    hallLink = "halloffame.html"
    mentorLink = "mentorship.html"
    progLink = "programs.html"
    faqLink = "satfaqs.html"
    newBString = bannerString.replace("SAT",nbrhood.replace('-',' ')+" SAT")
    newIString = "../"+nbrhood+".html"
    newHString = "../nbrhoodHoF/halloffame_"+nbrhood+".html"
    newMString = "../nbrhoodMtrshp/mentorship_"+nbrhood+".html"
    newPString = "./programs_"+nbrhood+".html"
    newFString = "../nbrhoodFaqs/satfaqs_"+nbrhood+".html"

    insertDict = {
        'b' : newBString,
        'i' : newIString,
        'h' : newHString,
        'm' : newMString,
        'p' : newPString,
        'f' : newFString
    }
    with open("./templates/programs.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        bIndices = findAll(bannerString,refContent,'b')
        iIndices = findAll(indexLink,refContent,'i')
        hIndices = findAll(hallLink,refContent,'h')
        mIndices = findAll(mentorLink,refContent,'m')
        pIndices = findAll(progLink,refContent,'p')
        fIndices = findAll(faqLink,refContent,'f')
        allIndices = bIndices+iIndices+hIndices+mIndices+pIndices+fIndices
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
        return endContent

def makeSatFaqs(nbrhood):
    # bannerString and first indexLink are too close so characters in between must be paid special attention
    bannerString = "\" class=\"logo\">SAT <span>"
    indexLink = "../index.html"
    hallLink = "halloffame.html"
    mentorLink = "mentorship.html"
    progLink = "programs.html"
    faqLink = "satfaqs.html"
    newBString = bannerString.replace("SAT",nbrhood.replace('-',' ')+" SAT")
    newIString = "../"+nbrhood+".html"
    newHString = "../nbrhoodHoF/halloffame_"+nbrhood+".html"
    newMString = "../nbrhoodMtrshp/mentorship_"+nbrhood+".html"
    newPString = "../nbrhoodProgs/programs_"+nbrhood+".html"
    newFString = "./satfaqs_"+nbrhood+".html"

    insertDict = {
        'b' : newBString,
        'i' : newIString,
        'h' : newHString,
        'm' : newMString,
        'p' : newPString,
        'f' : newFString
    }
    with open("./templates/satfaqs.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        bIndices = findAll(bannerString,refContent,'b')
        iIndices = findAll(indexLink,refContent,'i')
        hIndices = findAll(hallLink,refContent,'h')
        mIndices = findAll(mentorLink,refContent,'m')
        pIndices = findAll(progLink,refContent,'p')
        fIndices = findAll(faqLink,refContent,'f')
        allIndices = bIndices+iIndices+hIndices+mIndices+pIndices+fIndices
        allLength = len(allIndices)
        orderIndices(allIndices,allLength)
        endContent = ""
        for i in range(allLength):
            insertStr = insertDict[allIndices[i][2]]
            if(i==0):
                endContent += refContent[:allIndices[i][0]]+insertStr
            elif(i==allLength-1):
                endContent += insertStr+refContent[allIndices[i][1]:]
                break
            else:
                endContent += insertStr+refContent[allIndices[i][1]:allIndices[i+1][0]]
        return endContent

def generateIndex(nbrhood):
    fileName = nbrhood+".html"
    writeTo(fileName,makeFile(nbrhood))
    return

def generateHall(nbrhood):
    fileName = "./nbrhoodHoF/halloffame_"+nbrhood+".html"
    writeTo(fileName,makeHallofFame(nbrhood))
    return

def generateMentor(nbrhood):
    fileName = "./nbrhoodMtrshp/mentorship_"+nbrhood+".html"
    writeTo(fileName,makeMentorship(nbrhood))
    return

def generateProgs(nbrhood):
    fileName = "./nbrhoodProgs/programs_"+nbrhood+".html"
    writeTo(fileName,makePrograms(nbrhood))
    return

def generateFaqs(nbrhood):
    fileName = "./nbrhoodFaqs/satfaqs_"+nbrhood+".html"
    writeTo(fileName,makeSatFaqs(nbrhood))
    return

# generates html pages for all neighborhoods on file
def cityGeneration():
    neighborhoods = ["Astoria","Auburndale","Bay-Terrace","Bayside","Beechhurst","Bellaire",
                     "Bellerose","Blissville","Borough-Park","Briarwood","Bronxdale","Cambria-Heights",
                     "Castle-Hill","Clearview","College-Point","Corona","Ditmas-Park","Douglaston-Little-Neck",
                     "East-Elmhurst","Elmhurst","Fairmont-Claremont-Village","Flatbush","Floral-Park",
                     "Flushing","Forest-Hills-Gardens","Forest-Hills","Glen-Oaks","Glendale","Greenwood",
                     "Hillcrest","Hollis","Jackson-Heights","Jamaica-Estates","Jamaica-Hills","Jamaica",
                     "Kew-Garden-Hills","Kew-Gardens","Laurel-Hill","Laurelton","LeFrak-City","Lindenwood",
                     "Locust-Manor","Long-Island-City","Malba","Mapleton","Maspeth","Middle-Village",
                     "Morris-Park","Murray-Hill","Oakland-Gardens","Ozone-Park","Park-Slope","Parkchester",
                     "Pelham-Bay","Pomonok","Prospect-Lefferts-Gardens","Prospect-Park-South","Queens-Village",
                     "Rego-Park","Richmond-Hill","Rochdale","Saint-Albans","Soundview","South-Jamaica",
                     "South-Ozone-Park","South-Richmond-Hill","Springfield-Gardens","Sunnyside-Gardens","Sunnyside",
                     "Sunset-Park","Unionport","Upper-East-Side","Utopia","Van-Nest","West-Farms","Westchester-Square",
                     "Whitestone","Windsor-Terrace","Woodhaven","Woodside"]
    for x in neighborhoods:
        generateIndex(x)
        generateHall(x)
        generateMentor(x)
        generateFaqs(x)
        generateProgs(x)
    return

def test():
    generateIndex("Floral-Park")
    generateHall("Floral-Park")
    generateMentor("Floral-Park")
    generateFaqs("Floral-Park")
    generateProgs("Floral-Park")
    return

cityGeneration()
