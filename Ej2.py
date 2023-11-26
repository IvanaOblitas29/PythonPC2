max_estrellas = 5
for i in range(1, 2*max_estrellas):
    if i <= max_estrellas:
        print('*' * i)
    else:
        print('*' * (2*max_estrellas - i))