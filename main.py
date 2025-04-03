#TODO: Create a letter using starting_letter.docx 
file = open("./input/letters/starting_letter.docx", "r")
letter_content = file.read()
placeholder = file.readline()
names_list = open("./input/names/invited_names.txt", "r")
# names_list = names.readline()

for name in names_list:
    name = name.strip()
    x = letter_content.replace("[name]", name)
    letter = open(f"./output/readytosend/{name}"+"_letter.docx",mode="w")
    letter.write(x)
    
    
    letter.close()

file.close()
    


    
    


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp