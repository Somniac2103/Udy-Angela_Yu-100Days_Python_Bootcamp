# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp


#TODO: Create a letter using starting_letter.txt 
ftemplate = open("./Input/Letters/starting_letter.txt", "r")
print(ftemplate)

f = open("./Output/new.txt", "w")
f.write(ftemplate)
print(f)


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
