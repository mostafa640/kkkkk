print("how many raws should i have?")
raws = int(input())
print("how many column should i have?")
columns = int(input())
for row in range (0, raws, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
    print()
