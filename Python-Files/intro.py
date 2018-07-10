size_to_read = 10

print(list(range(1,2)))

# MODO 1
# f = open('../README.md', 'r')
# print(f.name, f.mode)
# f.close()

# MODO 2
with open('file.txt', 'r') as f:
    # print(f.name, f.mode)

    # Lee de a linea
    # for line in f:
    #     print(line, end='')

    # Lee de a linea
    # f_contens = f.readline()
    # print(f_contens)

    # Lee n caracteres
    # f_contents = ' '
    # while len(f_contents) > 0:
    #     f_contents = f.read(size_to_read)
    #     print(f_contents, end='')

    # Posicion
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    print(f.tell())