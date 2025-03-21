# # FileNotFound

# try:
#     print("Opening File")
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["dafd"])
# except FileNotFoundError:
#     print("Create File")
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up ")
#     # file.close()
#     # print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight /height **2
print(bmi)