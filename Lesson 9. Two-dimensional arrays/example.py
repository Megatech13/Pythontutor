n = 10

a = [[abs((i-j)*2) for j in range(n)] for i in range(n)]

for i in a:
    print(' '.join([str(elem) for elem in i]))