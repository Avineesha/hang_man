import random
def hang_man():
    list_of_word=["eduyea","hangman","india","laptop"]
    word=random.choice(list_of_word)
    print(word)
    turns=10
    guess_str=''
    valid_entry=tuple("abcdefghijklmnopqrstuvwxyz")

    while len(word)>0:
        main_word_store=""

        for letter in word:

            if letter in guess_str:
                main_word_store=main_word_store + letter
            else:
                main_word_store=main_word_store + "_ "

        if main_word_store == word:
            print(main_word_store)
            print("You won !!!!")
            break

        print("guss the word",main_word_store)
        guess=input()

        if guess in valid_entry:
            guess_str=guess_str+guess
        else:
            print("enter valid character")
            guess=input()
        
        if guess not in word:
            turns =turns -1

            if turns == 9:
                print("9 turns left")
                print("---------------")
            if turns == 8:
                print("8 turns left")
                print("---------------")
                print("       0       ")
            if turns == 7:
                print("7 turns left")
                print("---------------")
                print("      \0       ")
            if turns == 6:
                print("6 turns left")
                print("---------------")
                print("      \0/       ")
            if turns == 5:
                print("5 turns left")
                print("---------------")
                print("      \0/       ")
                print("       |        ")
            if turns == 4:
                print("4 turns left")
                print("---------------")
                print("      \0/       ")
                print("       |        ")
                print("      /         ")
            if turns == 3:
                print("3 turns left")
                print("---------------")
                print("      \0/       ")
                print("       |        ")
                print("      / \       ")
            if turns == 2:
                print("2 turns left")
                print("---------------")
                print("      \0/  |    ")
                print("       |        ")
                print("      / \       ")
            if turns == 1:
                print("only 1 turn left !!!! hangman on his last breath")
                print("---------------")
                print("      \0/__|    ")
                print("       |        ")
                print("      / \       ")
            if turns == 0:
                print("you loose")
                print("You let a good man die")
                print("---------------")
                print("       0__|    ")
                print("      /|\       ")
                print("      / \       ")
                break
                
n=input("enter your name -->>>")
print("!! Welcome to ",n,"!!")
print("<<<<---------------------->>>") 
print("Try to guess the word in less then 10 attempts")             
