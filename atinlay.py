from igpay import *
import sys
punc = [".",",","?","!","'",'"',"@","#","$","%","^","&","*"]
        
fn = sys.argv[1]

lines = open(fn).read().splitlines()

def convert_sentence(sentence):
    list_of_words = sentence.split(" ")
    #re.findall(r"\w+|[^\w\s]", sentence)
    new_sentence = ""   
    count = 0
    
    for word in list_of_words:
       
        count+=1
        new_sentence = new_sentence + igpay(word)    # ...like this
#         i
        new_sentence = new_sentence + " "   # but don't forget the space!
              
    return new_sentence

if __name__ == "__main__":
    
    for line in lines:
        print(convert_sentence(line))