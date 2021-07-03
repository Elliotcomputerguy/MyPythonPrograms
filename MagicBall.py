def MyMagicBall(fortuneReply):
    ''' A return value of yes/no or maybe to a users input ''' #<--- This is called a docstring for the help() function.
    import random                                                    # By placing a docstring into the fucntion it will help
    dict = {                                                         # other developers understand what the function does.                                                                          
        'Yes': 'Yes go for it',                #  help(myMagicBall)
        'No' : 'No, it will nt work out',
        #'Maybe' : '',
    }
    answer = random.choice(list(dict.values())) #<-- As a dictionary is not ordered we convert it to a list so the random.choice()                                                
    return answer                               # function can iterate over the list.

userFortuneQuestion = input('Ask your question:')
print(MyMagicBall(userFortuneQuestion)) #<-- This line calls the function and passes in the argument from the above input() function.
                                        # It then returns the expression of a random choice from the dictionary of answers. 

# ===========================================