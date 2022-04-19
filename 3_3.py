# num = 0 # iterator / incrementor 
# while num <= 5:
#   print("Hello World! " + str(num))
#   num += 1 # i = 1 + 1




#print("This program displays a famous movie quotations.")


#resps = ("1", "2", "3")
#resp = "0"

#while resp not in resps:
#    resp = input("Enter 1, 2 or 3: ")
#    if resp == "1":
#        print("Plastic.")
#    elif resp == "2":
#        print("Rosebud.")
#    elif resp == "3":
#        print("This's all folks.")
#        


## Display facts about the United States.
print("Enter a number from the menu to obtain a fact")
print("about the United States or to exit the program.\n")
print("1. Capital")
print("2. National Bird")
print("3. National Flower")
print("4. Quit\n")
while True:
    num= int(input("Make a selection from the main: "))
    if num == 1:
        print("Washington, DC is the capital of the United States.")
    elif num == 2:
        print("The American Bald Eagle is the national bird.")
    elif num == 3:
        print("The Rose is the national flower.")
    elif num == 4:
        break 
    