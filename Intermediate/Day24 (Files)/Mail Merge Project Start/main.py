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

    
