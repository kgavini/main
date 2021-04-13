birthdays = {'Krishna': 'September 7','Papay': 'July 9','Abhineet': 'May 8'}
while True:
   print('Enter a Name')
   name = input()
   if name == '':
    break

   if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
   else:
    print('Under construction')
