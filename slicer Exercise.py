#slicing :-------       variable[Start:End:steps]

# here is a very long word
#word = "antidisestablishmentarianism"
# use a slice to take out the word "establishment"
# and store it in the answer variable....

"""
word="antidisestablishmentarianism"
answer=word[word.index("establishment"):word.index("ari")]
print(answer)
"""

#email Slicer

"""
email=input("enter your email address? ").strip("")
name=email[:email.index("@")]
domain = email[email.index("@")+1:]
output="your email name is {} and domain is {}".format(name,domain)
print(output)
"""