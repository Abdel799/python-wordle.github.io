


import random                                   # Importing random, to be used later on when determining the unknown string

def color_text(text, color_code):               # Function for colouring text    
    return f"\033[{color_code}m{text}\033[0m"    


print("Welcome to Wordle!")
 
print("The rules are simple: You are given five chances to guess an unknown five letter word. Once you type in a word, the program will return your word")
print("and it will colour the letters green, if a specific letter in your input string is in the EXACT same position as the unknown string. The program will")
print("colour a letter red, if a letter in your input string, is in the unknown string, but in a different position. And finally the program will colour")
print("the letters gray if a letter isn't in the unknown string.")

def project():                                  # importing function that contains game (used for replaying)
    

    cond = False                                # condition used for win / lose. If cond == False, the user loses, otherwise the user wins and loop breaks
    
    
    
    difficulty = 0                              # difficulty level for list of unknown words
    
    while difficulty > 3 or difficulty < 1:     # while loop to keep running while the user enters a number outside of the range 1 - 3 (inclusive)
        difficulty = int(input("\nEnter a level of difficult (1,2,3) 1. Amateur Hour, 2. Normal, 3. Shakespeare: "))
        
        
    
    if difficulty == 1:
        l = ["about","enjoy","enter","juice","alert"]       # list of easy words
    
    elif difficulty == 2:
        l = ["mount","jumbo","cider","latch","exile"]       # list of moderate words
    
    elif difficulty == 3:
        l = ["haste","joust","quell","mirth","chide"]       # list of shakespearen words
    
    unknownlist = list(random.choice(l))                    # chooses random string in list
    string2 = ''.join(unknownlist)                          # converts the random string into list
    
    for i in range(5):                                      # for loop runs five times because the user gets five chances (if needed) to guess the word
        
        string1 = ""
        
        while len(string1) != 5:                            # loop keeps looping until the user enters a five letter word
            string1 = input("\nEnter a 5 letter word: ")
            
        
        string1 = string1.lower()                           # converts input string into all lower case
        string = string1
        inputlist = list(string)
        
        '''
        The string variable is used when changing the colours of the letters, while
        string1 is used to compare to the unknown string (string2)
        The reason why I didn't compare string to string2 is because when you change the colours of a string,
        you're also changing the actual content so if I try to compare it to string2 (unknown string) they will never be equal.
        '''
        
        l = []
        
        '''
        The list 'l' is used to append the green letters so that the program doesn't colour the green letters red in the next loop
        '''
        
        for i in range (len(inputlist)):
            
            if inputlist[i] == unknownlist[i]:                          # if the letters are in the exact same position
                inputlist[i] = color_text(inputlist[i],"32")            # colours letters green
                l.append(inputlist[i])                                  # appends green letter into list
                
    
        for i in range (len(inputlist)):
            
            if inputlist[i] in l:                                       # if a letter is already green, continue and skip passed it
                continue
            
            
            if inputlist[i] in unknownlist:                             # if a letter is in the unknown string, but not in the same position
                    
                inputlist[i] = color_text(inputlist[i],"33")            # colours letters red
                l.append(inputlist[i])
                    
            
            else:
                inputlist[i] = color_text(inputlist[i],"37")            # if letters aren't in unknown string, colour them gray
                
                
        string = ''.join(inputlist)                                     # joins the coloured input string
        print(string)                                                   # prints out the coloured string
        
        
        if string1 == string2:                                          # if input string is the same as unknown string, you win
            print("\nCongratulations, YOU'VE WON!")
            
            
            cond = True                                                 # condition turns to true (will be used later)
            break                                                       # breaks the loop, ends the game
    
    if cond == False:                                                   # if user fails to guess the word, the following prompt will be printed
        print("\nYou have failed to guess the word! The unknown word was",string2)
        
    
    
    play = 0
    
    while play < 1 or play > 2:     # keeps running loop until user picks 1 or 2
        play = int(input("\nWould you like to play again (1 for yes) (2 for no): "))        # would you like to play again?
        
     
    
    if play == 1:       # if user wants to play again
        project()       # recursion to reload the function again, allowing the user to replay
    
    else:               
        print("\nGoodbye")
 
        
    

project()                               # calls the function to start the program
