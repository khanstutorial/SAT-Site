#! python3

def writeTo(fileName,fileContent):
    with open(fileName,"w+") as outfile:
        outfile.write(fileContent)
    return

def readFrom(fileName):
    return

# input ex. : "Astoria", "Floral-Park"
# output: index.html with replaced titleString
def makeFile(nbrhood):
    titleString = "<title>SAT - Khan's Tutorial</title>"
    bannerString = "<a href=\"index.html\" class=\"logo\">SAT <span>Khan's Tutorial</span></a>"
    endContent = None
    with open("../SAT-Site/index.html","r",encoding='ascii',errors='surrogateescape') as reference:
        refContent = reference.read()
        newTString = titleString.replace("SAT",nbrhood+" SAT")
        newBString = bannerString.replace("SAT",nbrhood+" SAT")
        tIndex = refContent.find(titleString)
        bIndex = refContent.find(bannerString)
        endContent = refContent[:tIndex]+newTString+refContent[tIndex+len(titleString):bIndex]+newBString+refContent[bIndex+len(bannerString):]
    return endContent

def generate(nbrhood):
    fileName = nbrhood+".html"
    name = nbrhood.replace('-',' ')
    writeTo(fileName,makeFile(name))
    return

# generates html pages for all neighborhoods on file
def cityGeneration():
    neighborhoods = ["Astoria","Auburndale","Bay-Terrace","Bayside","Beechhurst","Bellaire",
                     "Bellerose","Blissville","Borough-Park","Briarwood","Bronxdale","Cambria-Heights",
                     "Castle-Hill","Clearview","College-Point","Corona","Ditmas-Park","Douglaston-Little-Neck",
                     "East-Elmhurst","Elmhurst","Fairmont-Claremont-Village","Flatbush","Floral-Park",
                     "Flushing","Forest-Hills-Gardens","Forest-Hills","Glen-Oaks","Glendale","Greenwood",
                     "Hillcrest","Hollis","Jackson-Heights","Jamaica-Estates","Jamaica-Hils","Jamaica",
                     "Kew-Garden-Hills","Kew-Gardens","Laurel-Hill","Laurelton","LeFrak-City","Lindenwood",
                     "Locust-Manor","Long-Island-City","Malba","Mapleton","Maspeth","Middle-Village",
                     "Morris-Park","Murray-Hill","Oakland-Gardens","Ozone-Park","Park-Slope","Parkchester",
                     "Pelham-Bay","Pomonok","Prospect-Lefferts-Gardens","Prospect-Park-South","Queens-Village",
                     "Rego-Park","Richmond-Hill","Rochdale","Saint-Albans","Soundview","South-Jamaica",
                     "South-Ozone-Park","South-Richmond-Hill","Springfield-Gardens","Sunnyside-Gardens","Sunnyside",
                     "Sunset-Park","Unionport","Upper-East-Side","Utopia","Van-Nest","West-Farms","Westchester-Square",
                     "Whitestone","Windsor-Terrace","Woodhaven","Woodside"]
    for x in neighborhoods:
        generate(x)
    return

cityGeneration()
