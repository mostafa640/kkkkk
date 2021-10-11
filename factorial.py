print("please enter a number")
number = int(input())
count = 0
total = 1
while count < number:
    count += 1
    total = total * count
print(f"The factorial number is {total}")