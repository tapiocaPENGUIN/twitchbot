def getName():
    print('Hello World')
    print('What is your name')
    myName = input()
    print('Your name is: ' + myName)
    #print('The length of your name is: ' + str(len(myName)))

    if(len(myName) > 5):
        print('Your name is longer than 5 characters!')
    else:
        print('Your name is less that 5 characters!')

    print('How old are you? ')
    age = input()
    if(int(age) >=21):
        print('You are old enough to drink!')
    else:
        print('You may not drink legally!')

getName()
# Adding this comment
