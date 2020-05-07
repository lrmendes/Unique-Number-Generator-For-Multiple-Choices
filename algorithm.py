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

def retrieveValuesDataFromUniqueNumber(uniqueValue, output=[], start=2**len(choices)):
    if (uniqueValue == 0):
        return output
    else:
        if(uniqueValue >= start):
            output.append(start)
            return retrieveValuesDataFromUniqueNumber(uniqueValue-start,output,int(start/2))
        else:
            return retrieveValuesDataFromUniqueNumber(uniqueValue,output,int(start/2))

def retrieveKeysDataFromUniqueNumber(uniqueValue, output=[], start=2**len(choices)):
    if (uniqueValue == 0):
        return output
    else:
        if(uniqueValue >= start):
            output.append([k for k,v in choices.items() if v == start])

            return retrieveKeysDataFromUniqueNumber(uniqueValue-start,output,int(start/2))
        else:
            return retrieveKeysDataFromUniqueNumber(uniqueValue,output,int(start/2))


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
