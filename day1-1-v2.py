import utils 

#load all the text from the example
lines = utils.load_lines("day1.txt")

#print(lines)

#create an empty list of results
all_results = []

#go over each line
for line in lines:

    #print the line out
    #print(line)

    #define variables 'first_character' and 'last_character', initially with no value (None)
    first_character = None 
    last_character = None

    #loop over each character in the line
    for index in range(0,len(line)):
        character = line[index]

        #check if it is a digit 
        if character >= '0' and character <= '9':
            #store it in first character, and bail out of this loop
            first_character = character
            break

    #loop over each character in the line (reversed)
    line = line[::-1]
    for index in range(0,len(line)):
        character = line[index]

        #check if it is a digit 
        if character >= '0' and character <= '9':
            #store it in last character, and bail out of this loop
            last_character = character
            break

    #print(first_character + last_character)

    #combine first and last characters, then convert to an integer value
    integer_value = int(first_character + last_character)

    all_results.append(integer_value)

print(sum(all_results))