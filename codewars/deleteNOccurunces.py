def delete_nth(order, max_e):
    output = []
    for item in order:
        if output.count(item) == max_e:
            continue
        output.append(item)
    return output


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
