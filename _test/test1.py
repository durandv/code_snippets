x = ['4', 6, '10', '17', 7]
to_int = [i if type(i) == int else int(i) for i in x]
print(to_int)