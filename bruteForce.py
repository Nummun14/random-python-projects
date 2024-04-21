import string
for i in string.ascii_lowercase + string.digits + string.ascii_uppercase:
    for j in string.ascii_lowercase + string.digits + string.ascii_uppercase:
        for k in string.ascii_lowercase + string.digits + string.ascii_uppercase:
            for u in string.ascii_lowercase + string.digits + string.ascii_uppercase:
                print(i, j, k, u, sep='')
