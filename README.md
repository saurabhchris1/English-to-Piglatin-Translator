# English-to-Piglatin-Translator

**1. [ 50 points ]
Write a Python module igpay.py that contains a function igpay() that will return the translation of its (string) argument, assumed to be a word, into Pig Latin.
The rules of Pig Latin are:**
```
(a) Vowels are "a", "e", "i", "o" and "u". All other letters are consonants. "y" and
"w" count as consonants in this case (e.g.: igpay("yes") returns "esyay").

(b) If a word begins with a consonant, move all of the characters up to but not 
     including the first vowel to the end of the word and add "ay" (e. g., igpay("parrot") returns
     "arrotpay". igpay("knights") returns "ightsknay").

(c) If a word begins with a vowel, append "way" (e.g.: igpay("add") returns "addway". 
     igpay("office") returns "officeway".)

(d) If there are no vowels in the word, return the word unchanged (ex: igpay("why") returns "why").
     For this part of the assignment only, you may assume that the words will all be in lower case.
     Include a self-test program (i.e. a suite beginning with “if     name     == ’ main ’:” at the end)
     in the module that will test and print the results of all of the above rules when it is
     invoked via $ python3 igpay.py

```
**2. [ 50 points ] Create a Python script atinlay that will translate every word in a text file into Pig Latin and print the result on standard output. atinlay will import the above igpay module (which will be enhanced as below). It should observe the following constraints:**
```
(a) The command syntax should be
     $ ./atinlay {file_name}
     Import the sys module. sys.argv[] will then give you the command line arguments.

(b) Enhance igpay() to do the right thing with upper case, so that igpay("The") returns 
     "Ethay", not "eThay" and   igpay("STUFF") is "UFFSTAY". igpay should continue to work 
      with lower case words as before.

(c) Words can be delimited by white space (tabs, newlines, and spaces) or by punc- tuation, 
     so that if the file is this line:
     
         The parrot is deceased.
         
atinlay should produce:
         Ethay arrotpay isway eceasedday.
         
not
         Ethay arrotpay isway eceasedd.ay
         
(d) The file is of arbitrary size and may have any number of lines.

```
