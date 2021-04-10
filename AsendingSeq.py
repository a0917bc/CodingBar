#%%
import sys
products = []
min = -sys.maxsize - 1
while True:
    data = input()
    if data == "0":
        break
    products.append(data)
tmp = min
ans = ''
for i in range(len(products)):
    if int(products[i]) >= int(tmp):
        tmp = products[i] 
        ans = ans + tmp
print(ans)
# %%