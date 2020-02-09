textH = "H"
for row in range(5):
    for col in range(4):
        if col == 0 or col == 3 or (row == 2 and (0 < col < 3)):
            print("*", end="")
        else:
            print(end=" ")
    print()

for row in range(5):
    for col in range(4):
        if col == 0 or row == 0 or row == 2 or row == 4:
            print("*", end="")
        else:
            print(end=" ")
    print()