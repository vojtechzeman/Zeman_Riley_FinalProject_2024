
list = [0, 1, 2, 3, 4, 5, 6]
print(list[0:6:2])

# hello hello

print("hello")

# hello hello
# hello hello

print("hello")
# make a list 3,6,9,12,... to 30
list = [i for i in range(3, 31, 3)]
print(list)



# Filter out lines containing '@'
with open('requirements.txt', 'r') as file:
    lines = file.readlines()
filtered_lines = [line for line in lines if '@' not in line]
with open('requirements.txt', 'w') as file:
    file.writelines(filtered_lines)

print("Removed lines containing '@' from requirements.txt.")
