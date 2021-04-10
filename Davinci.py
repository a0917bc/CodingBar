#%%
sentence = input()
numberList = list(range(5))
for i in range(5):
    numberList[i] = input()
for i in range(5):
    print(sentence[int(numberList[i])])
# %%
sentence = input()
index = list(map(int, input().split()))
for i in index:
    print(sentence[i])
# The culture of the United States of America is primarily of Western origin.
# Test data
# %%
