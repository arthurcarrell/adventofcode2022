file = open("day 2\input.txt")
fileList = file.read().split("\n")

totalScore = 0
part2TotalScore = 0

def checkForLoss(yourplay,enemyplay):
    if yourplay == "X" and enemyplay == "B":
        return "L"
    elif yourplay == "Y" and enemyplay == "C":
        return "L"
    elif yourplay == "Z" and enemyplay == "A":
        return "L"
    elif yourplay == "X" and enemyplay == "A":
        return "D"
    elif yourplay == "Y" and enemyplay == "B":
        return "D"
    elif yourplay == "Z" and enemyplay == "C":
        return "D"
    else:
        return "W"
    

def getScore(play,outcome="W"):
    playDic = {"X":1,"Y":2,"Z":3}
    outcomeDic = {"W":6,"D":3,"L":0}
    print(f"{playDic[play]} + {outcomeDic[outcome]} = {playDic[play] + outcomeDic[outcome]}",end=" ")
    return playDic[play] + outcomeDic[outcome]

def goForTargetOutcome(enemymove,targetoutcome):
    if targetoutcome == "X":
        playDic = {"A":"Z","B":"X","C":"Y"}
        return playDic[enemymove]
    elif targetoutcome == "Y":
        playDic = {"A":"X","B":"Y","C":"Z"}
        return playDic[enemymove]
    elif targetoutcome == "Z":
        playDic = {"A":"Y","B":"Z","C":"X"}
        return playDic[enemymove]

# Get part one answer.
for line in range(sum(1 for line in open("day 2\input.txt"))):
    lineBreakdown = fileList[line].split(" ")
    enemyMove = lineBreakdown[0]
    playerMove = lineBreakdown[1]
    result = checkForLoss(playerMove,enemyMove)
    totalScore += getScore(playerMove,result)

# Get part two answer
for line in range(sum(1 for line in open("day 2\input.txt"))):
    lineBreakdown = fileList[line].split(" ")
    enemyMove = lineBreakdown[0]
    targetOutcome = lineBreakdown[1]
    result = checkForLoss(goForTargetOutcome(enemyMove,targetOutcome),enemyMove)
    part2TotalScore += getScore(goForTargetOutcome(enemyMove,targetOutcome),result)
    print(checkForLoss(goForTargetOutcome(enemyMove,targetOutcome),enemyMove))

print(f"Part 1 answer: {totalScore}")
print(f"Part 2 answer: {part2TotalScore}")