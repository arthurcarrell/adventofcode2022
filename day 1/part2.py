# This is my part 1 code but modifed to get the top three.

# get all the answers.
answer = [0,0,0]
# current answer for the list
currentAnswer = 0
# open input.txt and split it for each empty space
file = open("day 1\input.txt")
# split into a list
file = file.read().split("\n")
# get each item in the list.
for item in range(sum(1 for line in open("day 1\input.txt","r"))):
    print(f"Checking Line {item+1}...")
    if file[item] != "":
        file[item] = int(file[item])
        print(f"Adding {file[item]} to the answer list.")
        currentAnswer += file[item]
    else:
        print("Found an empty space!")
        print("Taking the current answer and comparing it to the real answer.")
        if currentAnswer > answer[0]:
            answer[0] = currentAnswer
            print("This is higher then the current answer, this is the new answer.")
        else:
            print(f"Lower or equal to highest answer. ({answer[0]} > {currentAnswer})")
            if currentAnswer > answer[1]:
                answer[1] = currentAnswer
                print("This is higher then the second current answer, this is the new answer.")
            else:
                print(f"Lower or equal to second highest answer. ({answer[1]} > {currentAnswer})")
                if currentAnswer > answer[2]:
                    answer[2] = currentAnswer
                    print("This is higher then the second current answer, this is the new answer.")
                else:
                    print(f"Lower or equal to third highest answer. ({answer[2]} > {currentAnswer})") 
        currentAnswer = 0
print(f"\nAnswer 1: {answer[0]}")
print(f"Answer 2: {answer[1]}")
print(f"Answer 3: {answer[2]}")
print(f"The total sum is {int(answer[0]) + int(answer[1]) + int(answer[2])}!")
