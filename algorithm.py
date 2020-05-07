import json

# Key = Choise String | Value = Choise Value
# The max number of different choises are 32 (for a integer) 
# Choise value always is the 2 raised by Choise Index
# V Starts with 2 raised by 0 and Ends with 2 raised by
# Where N is the number of choises
choises = dict([
    ("choise 1",1),
    ("choise 2",2),
    ("choise 3",4),
    ("choise 4",8),
    ("choise 5",16),
    ("choise 6",32),
    ("choise 7",64),
    ("choise 8",128),
])

def retrieveValuesDataFromUniqueNumber(entrada, saida=[], start=2**len(choises)):
    if (entrada == 0):
        return saida
    else:
        if(entrada >= start):
            saida.append(start)
            return retrieveValuesDataFromUniqueNumber(entrada-start,saida,int(start/2))
        else:
            return retrieveValuesDataFromUniqueNumber(entrada,saida,int(start/2))

def retrieveKeysDataFromUniqueNumber(entrada, saida=[], start=2**len(choises)):
    if (entrada == 0):
        return saida
    else:
        if(entrada >= start):
            saida.append([k for k,v in choises.items() if v == start])

            return retrieveKeysDataFromUniqueNumber(entrada-start,saida,int(start/2))
        else:
            return retrieveKeysDataFromUniqueNumber(entrada,saida,int(start/2))


def main():
    # Get a unique choise number by sum of user choises
    myChoises = choises["choise 1"] + choises["choise 3"] + choises["choise 8"]
    print("Your unique choise number to store in database/user: ",myChoises)


    # Now you can retrieve all the chosen options by that function
    myChoisesVectorKeys = retrieveKeysDataFromUniqueNumber(myChoises)
    myChoisesVectorValues = retrieveValuesDataFromUniqueNumber(myChoises)
    print("\nInput Number: ",myChoises)
    print("\nInput Number Chosen Keys: ", myChoisesVectorKeys)
    print("Input Number Chosen Values : ", myChoisesVectorValues)
main()
