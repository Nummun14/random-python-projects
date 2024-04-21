amount = int(input("How many grades?"))
answer = input("Do you want an average or the highest?")
high = 0
if answer == "highest":
    for i in range(10):
        grade1 = int(input("input a grade"))
        if high < grade1:
            high = grade1
    print(high)
elif answer == "average":
    for i in range(10):
        grade2 = int(input("input a grade"))
        high = high + grade2
    print(high/10)
