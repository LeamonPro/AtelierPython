minn=0
maj=0
n=4
ch1="HeLlO"
print("longeur de la chaine = {}".format(len(ch1)))
for char in ch1:
    print(char)
    if char.isupper():
        maj+=1
    else:
        minn+=1
print("nombre des characters majuscule = {} \n nombre des characters minuscule = {}".format(maj,minn))
ch2="radar"
if ch2==ch2[::-1]:
    print("palindrome")
else:
    print("n'est pas palindrome")
#ch1[n]=""
#ch1[0:n]=ch1[n+1]
