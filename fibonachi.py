length = int(input("how long?"))
fibo1 = 1
fibo2 = 1
print(fibo1)
print(fibo2)
for i in range(length // 2):
    fibo1 = fibo1 + fibo2
    print(fibo1)
    fibo2 = fibo1 + fibo2
    print(fibo2)
