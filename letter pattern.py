rows =int(input("Enter number of rows: "))
ch = ord('a')
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
