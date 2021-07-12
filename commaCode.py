# Writes a list out - comma separated with the word 'and' before the
# last value in the list

def listString(listValue):
    listAsString = ''

    for item in listValue:
        if listValue.index(item) != len(listValue) - 1:
            listAsString += item + ', '
        elif listValue.index(item) == len(listValue) - 1:
            listAsString += 'and ' + item

    return listAsString


spam = ['milk', 'cheese', 'butter', 'bacon']

print(listString(spam))
