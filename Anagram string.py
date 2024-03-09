s1=input("Enter first string: ")
s2=input("Enter second string: ")
s1.lower()
s2.lower()
if sorted(s1)==sorted(s2):
    print("The given strings are anagrams")
else:
    print("The given strings are not anagrams")
