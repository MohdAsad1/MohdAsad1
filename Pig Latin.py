original = input("Enter any sentence :-").strip().lower()
words=original.split()
new_words=[]
for word in words:
    if word[0] in "aeiou":
        new_word=word +"yay"
        new_words.append(new_word)
        #print(new_words)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
            cons=word[:vowel_pos]
            the_rest=word[vowel_pos:]
            new_word=the_rest+cons+"ay"
            new_words.append(new_word)

output=" ".join(new_words)
print(output)