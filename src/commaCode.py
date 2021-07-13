# Writes a list out - comma separated with the word 'and' before the
# last value in the list

def listString(listValue):
    listAsString = ''

    # If the list contains no values:
    if len(listValue) == 0:
        listAsString += 'This list is empty.'

    # If the list contains one or more values:
    for item in listValue:
        if listValue.index(item) != len(listValue) - 1:
            listAsString += item + ', '
        elif listValue.index(item) == len(listValue) - 1:
            listAsString += 'and ' + item

    return listAsString


groceries = ['milk', 'cheese', 'butter', 'bacon']
empty = []

print(listString(groceries))
print(listString(empty))
