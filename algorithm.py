import json

# Key = Choice String | Value = Choice Value
# The max number of different choices are 32 (for a integer) 
# Choice value always is the 2 raised by Choice Index
# V Starts with 2 raised by 0 and Ends with 2 raised by
# Where N is the number of choices
choices = dict([
    ("choice 1",1), # choosed
    ("choice 2",2),
    ("choice 3",4), # choosed
    ("choice 4",8),
    ("choice 5",16),
    ("choice 6",32),
    ("choice 7",64),
    ("choice 8",128), # choosed
])

def retrieveValuesDataFromUniqueNumber(entrada, saida=[], start=2**len(choices)):
    if (entrada == 0):
        return saida
    else:
        if(entrada >= start):
            saida.append(start)
            return retrieveValuesDataFromUniqueNumber(entrada-start,saida,int(start/2))
        else:
            return retrieveValuesDataFromUniqueNumber(entrada,saida,int(start/2))

def retrieveKeysDataFromUniqueNumber(entrada, saida=[], start=2**len(choices)):
    if (entrada == 0):
        return saida
    else:
        if(entrada >= start):
            saida.append([k for k,v in choices.items() if v == start])

            return retrieveKeysDataFromUniqueNumber(entrada-start,saida,int(start/2))
        else:
            return retrieveKeysDataFromUniqueNumber(entrada,saida,int(start/2))


def main():
    # Get a unique choice number by sum of user choices
    myChoices = choices["choice 1"] + choices["choice 3"] + choices["choice 8"]
    print("Your unique choice number to store in database/user: ",myChoices)


    # Now you can retrieve all the chosen options by that function
    myChoicesVectorKeys = retrieveKeysDataFromUniqueNumber(myChoices)
    myChoicesVectorValues = retrieveValuesDataFromUniqueNumber(myChoices)
    print("\nConvert Unique Number to Choices: ",myChoices)
    print("\nUnique Number Chosen Keys: ", myChoicesVectorKeys)
    print("Unique Number Chosen Values : ", myChoicesVectorValues)
main()
