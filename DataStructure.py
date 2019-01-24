def main():
    # problem1()
    problem2()


# Create a function that has a loop that quits with q
# Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names
# ADDITIONAL REQUIREMENTS:
#
# Your code should be able to process the quit command (q) the User enters regardless of case

# This function is given a loop to continue with the list until "q" is entered to quit

# def problem1():
#
#     givenLoop = input("Enter a name:")
#     givenLoop2 = ""
#     while(givenLoop != givenLoop2 ):
#         # if(givenLoop != 'q'):
#         givenLoop2 = input(givenLoop != "q")

       # print(givenLoop)

        # givenLoop(str(givenLoop2.insert))








#
def problem2():

 myDictionaryList = [0 ,1 ,2 ]
myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]


character = input("Enter the name or age in dictionary:")
# myDictionaryList
while character != 'q':
    print(character)

    # if(character == 'q'):
    # return myDictionaryList
    # print(myDictionaryList)


    if __name__ == '__main__':
        main()