#do imports
import string

file = open("day 3\input.txt").read().split("\n")


def splitString(string):
    part1,part2 = string[:round(len(string)*0.5)], string[round(len(string)*0.5):]
    return [part1,part2]

def splitString3(string):
    part1,part2,part3 = string[:round(len(string)*0.33)], string[round(len(string)*0.33):round(len(string)*0.66)], string[round(len(string)*0.66):]
    return [part1,part2,part3]

def listToGroups(list,groupnumber):
    endList = []
    curString = ""
    curItem = 0
    for item in list:
        curItem += 1
        curString += item
        if curItem == groupnumber:
            endList.append(curString)
            curString = ""
            curItem = 0
    return endList


allLetters = string.ascii_lowercase + string.ascii_uppercase + "None"

def getSimilarCharacter(string,string2):
    for letter in string:
        if letter in string2:
            return letter
        
def getThreeSimilarCharacter(string,string2,string3):
    for letter in string:
        if letter in string3 and letter in string2:
            return letter
    for letter in string2:
        if letter in string and letter in string3:
            return letter
    for letter in string3:
        if letter in string2 and letter in string:
            return letter
def getPriority(letter):
    return allLetters.index(letter) + 1

total = 0

def main():
    global total
    for line in file:
        # split the string into 2.
        items = splitString(line)
        # get the similar character
        similiarChr = getSimilarCharacter(items[0],items[1])
        # get the priority and add it to the total
        total += getPriority(similiarChr)
    print(f"Part 1: {total}")

pt2Total = 0
def mainPt2():
    global pt2Total
    # split the file into strings of groups of three
    groupThreeFile = listToGroups(file,3)
    for item in groupThreeFile:
        # get that item and split it into 3 equal parts.
        itemList = splitString3(item)
        #print(itemList)
        similarChr = getThreeSimilarCharacter(itemList[0],itemList[1],itemList[2])
        #print(similarChr)
        if similarChr == None:
            similarChr = "None"
        
        pt2Total += getPriority(similarChr)
    print(f"Part 2: {pt2Total}")
        

main()
mainPt2()