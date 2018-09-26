import re
VOWELS = ('a', 'e', 'i', 'o', 'u')
punc = [".",",","?","!",'"',"@","#","$","%","^","&","*"]
        
def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'aeiouAEIOU':
            return index

def vowelz(a):
        vowels = ["a", "e", "i", "o", "u","A","E","I","O","U"]
        vowel = False
        for vowell in vowels:
                if vowell in a:
                    vowel = True
        return vowel
    
def igpay(word):
    new_sentence = "" 
    
    if "'" in word:
      
        first_letter = word[0]
    
        if first_letter.lower() in VOWELS:  
             
            if word.isupper():
                z = word + "WAY"
                new_sentence = new_sentence + z 
            else:
                z = word + "way"
                new_sentence = new_sentence + z
        elif vowelz(word):
            if word.isupper():
                x = first_vowel(word)
                z = word[x:] + word[:x] + "AY"
                new_sentence = new_sentence + z
            elif first_letter.isupper():
                x = first_vowel(word)
                z = word[x].upper()+ word[x+1:] + word[:x].lower() + "ay"
                print(z)
                new_sentence = new_sentence + z
            else:
                 
                x = first_vowel(word)
                z = word[x:] + word[:x] + "ay"
                new_sentence = new_sentence + z
                    
        else:
            new_sentence = new_sentence + word
    else:
        word_list = re.findall(r"\w+|[^\w\s]", word)
  
        for word in word_list:
            if word in punc:
                new_sentence = new_sentence + word
        
            else:
                first_letter = word[0]
                if first_letter.lower() in VOWELS:
                    
                    if word.isupper():
                        z = word + "WAY"
                        new_sentence = new_sentence + z 
                    else:
                        z = word + "way"
                        new_sentence = new_sentence + z
                elif vowelz(word):
                    
                    if word.isupper():
                        
                        x = first_vowel(word)
                        z = word[x:] + word[:x] + "AY"
                        new_sentence = new_sentence + z
                    elif first_letter.isupper():
                        x = first_vowel(word)
                        z = word[x].upper()+ word[x+1:] + word[:x].lower() + "ay"
                        new_sentence = new_sentence + z
                    else:
                        x = first_vowel(word)
                        z = word[x:] + word[:x] + "ay"
                        new_sentence = new_sentence + z
                    
                else:
                    new_sentence = new_sentence + word

    return new_sentence
    
    

if __name__ == "__main__":
    x = igpay("yes")
    y = igpay("parrot")
    z = igpay("knights")
    a = igpay("add")
    b = igpay("office")
    c = igpay("why")
    
    
    print("If the word is 'yes' the translation is : " + x)
    
    print("If the word is 'parrot' the translation is : " + y)
    
    print("If the word is 'knights' the translation is : " + z)
    
    print("If the word is 'add' the translation is : " + a)
    
    print("If the word is 'office' the translation is : " + b)
    
    print("If the word is 'why' the translation is : " + c)