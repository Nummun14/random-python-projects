def pyramid(n):
    answer = []
    for i in range(n):
        item = [1]
        for j in range(i):
            item.append(1)
        answer.append(item)
    return answer


print(pyramid(0))
print(pyramid(1))
print(pyramid(2))
print(pyramid(3))
