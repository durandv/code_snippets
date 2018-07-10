fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# conditionals after for
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# conditionals before for with else
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]
print(new_fellowship)

# dictioynary
new_fellowship = {member:len(member) for member in fellowship}
print(new_fellowship)


