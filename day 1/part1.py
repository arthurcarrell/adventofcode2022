# get the highest answer
answer = 0
# current answer for the list
currentAnswer = 0
# open input.txt and split it for each empty space
file = open("day 1\input.txt","r")
# split into a list
file = file.read().split("\n")
# get each item in the list.
for item in range(sum(1 for line in open("day 1\input.txt","r"))):
    print(f"Checking Line {item}...")
    if file[item] != "":
        file[item] = int(file[item])
        print(f"Adding {file[item]} to the answer list.")
        currentAnswer += file[item]
    else:
        print("Found an empty space!")
        print("Taking the current answer and comparing it to the real answer.")
        if currentAnswer > answer:
            answer = currentAnswer
            print("This is higher then the current answer, this is the new answer.")
        else:
            print(f"Lower or equal to highest answer. ({answer} > {currentAnswer})")
        currentAnswer = 0
print(f"The answer is {answer}!")
