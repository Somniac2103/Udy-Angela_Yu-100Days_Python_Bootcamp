# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp

flist = open("./Input/Names/invited_names.txt", "r")
people_array = flist.readlines()
print(people_array)

for person in people_array:

    ftemplate = open("./Input/Letters/starting_letter.txt", "r")
    content_array = ftemplate.readlines()
    content = ""

    for part in content_array:
        content += part

    person = person.strip(f'\n') 

    content = content.replace("[name]", person)

    invitee = f'./Output/ReadyToSend/{person}.txt'

    f = open(invitee, "w")
    f.write(content)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
