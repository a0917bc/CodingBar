#%%
d = input()
intd = int(d)
numberList = list(range(intd))
ans = ''
for i in range(intd):
    numberList[i] = input()
for i in range(intd - 1):
    if int(numberList[i]) < int(numberList[i + 1]):
        ans = ans + '1'
    else:
        ans = ans + '0'
print(ans)
# %%