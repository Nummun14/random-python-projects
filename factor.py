total = 0
factors = []
values = []

print("this is a factoring tool. It's meant to be used if you're struggling to decide whether to so something or not.")
print("To use it, input a factor, and assign it a value depending on how important it is. For example:\n")
print("if you're deciding if you want to get a new job but it's far away, and the distance is important to you,")
print("you could add the factor 'distance' with the value '-5'. On the other hand, if the job has a good salary, ")
print("but that's not really important to you, you could add the factor 'salary' with the value '2'.\n")
print("After you input all the factors you type 'done', and you will get an overall score.")
print("The higher the score, the better it is.\n")
print("This is useful for comparing different options and overall making a decision.")
while True:
    factor = input('input a factor, if your done type "done"')
    if factor == "done":
        break
    factors.append(factor)
    value = int(input('input the value'))
    total = total + value
    values.append(value)
for i in range(len(factors)):
    print(factors[i], values[i])
print("total:", total)
