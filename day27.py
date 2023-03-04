var_in = input("Enter a string not more than 50 chars :")

print("Enter the range to loop on :")
loopvar1=int( input("Enter the first number :"))
loopvar2=int( input("Enter the second number :"))

search_word=input("Enter the word to search for :")

num_of_existence = 0

if len(var_in) > 50 :
    print ("Error! More than 50 chars")
    exit()
else:
    word = var_in.split()
    for i in range (0,len(word)) :
        print (word[i])

    for j in range (loopvar1, loopvar2) :

        if word[j] == search_word :
            num_of_existence +=1

        elif word[j][0].isupper() == True : 
            print ("uppercase word :" + word[j])

    for i in range (0, len(var_in)) :
        lowerstrr= var_in.lower()
        if (lowerstrr[i] == 'a' or lowerstrr[i] == 'e' or lowerstrr[i] == 'o' or lowerstrr[i] == 'i' or lowerstrr[i] == 'u'):
            print ("vowels are" + lowerstrr[i])

    print ("Number of existence of the word is :" + str(num_of_existence))
    
        

