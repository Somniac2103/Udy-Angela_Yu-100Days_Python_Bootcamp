# numbers = [1,2,3]
# new_numbers = [(n+1) for n in numbers]
# print(new_numbers)

# name="Barry"
# new_name = [letter for letter in name]
# print(new_name)

# range_list = range(1,5)
# new_range_list = [n*2 for n in range_list]
# print(new_range_list)

# names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# capitalize_names =[name.upper() for name in names if len(name) > 4]
# print(capitalize_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num%2==0]
# print(result)


file1 = open("./file1.txt", "r")
file1 = file1.readlines()
file1 = [int(num.strip(f'\n')) for num in file1]
print(file1)

file2 = open("./file2.txt", "r")
file2 = file2.readlines()
file2 = [int(num.strip(f'\n')) for num in file2]
print(file2)

result = [num for num in file1 if  num in file2]

print(result)