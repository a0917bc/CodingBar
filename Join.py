#%%
products = []
equation = []
ans = 1
while True:
    data = input()
    if data == '0':
        break
    products.append(data)
    ans = ans * int(data)
mulStr = ' x '
equation = mulStr.join(products) + ' = '
print(equation + str(ans))
a = equation.split()#delete space and let char. individually be
while 'x' in a: a.remove('x')
# %%
