import pandas as pd
l = [1,2,3,4,5,6]
var = pd.DataFrame(l)
print(var)
print(type(var))

dic = {"a":[1,2,3,4,5],"r":[1,2,3,4,5]}
var = pd.DataFrame(dic,columns=["a"])
print(var)
print(type(var))