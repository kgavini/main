import os
import sys
import sys
print(sys.version)
#cls = os.system('cls')

stdname = 'Abhineet'
print ("Student name is : " + stdname)





print('What is your name?')
myName = input()
print('Welcome ' + myName)


if myName == 'Krishna':
    for i in range(5):
       print('WELCOME our GREAT hero ' + myName + str(i))
else:
    print('Please ask Krishna to make an appearance')

def hello(name):
    print("Hello " + name)

'''while True:
    print('Type "exit" to exit the Loop')
    exit = input()
    if exit =='exit':
        sys.exit()
        print('Exiting the Loop since a exit string was iput')'''

hello('Krishna')


