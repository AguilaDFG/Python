with open("file1.txt") as file1:
    file_1 = file1.readlines()
    file_1 = [int(n) for n in file_1]
with open("file2.txt") as file2:
    file_2 = file2.readlines()
    file_2 = [int(n) for n in file_2]
result = [n for n in file_1 if n in file_2]
print(result)