#%%
loveLetter = []
tmp = []
listOfVoweles = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
while True:
    sentence = input()
    if sentence == "no":
        break
    words = sentence.split()
    for word in words:
        if word[0] in listOfVoweles:
            word += 'ay'
        else:
            word = word[1:] + word[0]
            word += 'ay'
        tmp.append(word)
    loveLetter.append(" ".join(tmp))
    tmp = []
for i in loveLetter:
    print(i)

# %%
