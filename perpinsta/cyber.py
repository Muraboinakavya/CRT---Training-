str = input("Enter the string : ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for ch in str:
    if(ch==vowels):
        vowel_count = vowel_count+1
        print(vowel_count)
    #if(ch.isdigit()):
        
    if(ch!=vowels):
        consonant_count = consonant_count+1
        print(consonant_count)
if(vowel_count == consonant_count):

    print("Balanced")
else:
     print("not balanced")
