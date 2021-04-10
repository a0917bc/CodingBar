#%%
products = []
while True:
    data = input()
    if data == "no":
        break
    products.append(data)
searchWord = input()
total = []
for i in range(len(searchWord)):
    target = searchWord[:i+1]
    ans = []
    for j in products:
        if target == j[:i+1]:
            ans.append(j)
    ans.sort()
    total.append(ans[:3])
print(total)
#%%