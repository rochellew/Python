# Working with lists CHANGED
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or nothing to stop.)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # List conCATenation MEOW ;3

if len(catNames) >= 1:
    print('The cat names are: ')
    for name in catNames:
        print(" " + name)
else:
    print('There are no cat names to display.')
