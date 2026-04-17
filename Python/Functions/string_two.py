def separate():
    phrase = input("Enter a phrase with - separating them: ")
    separate= phrase.split('-')
    separate.sort()  
    resultado = '-'.join(separate)
    print(resultado) 

separate()