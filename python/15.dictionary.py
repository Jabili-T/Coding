#assignment-15
#1.creating a dict with 5 key-value pairs the std id and name
std={1:"Abhi",2:"Jaya",3:"Thanmai",4:"Zoya",5:"Ravi"}
print("DICTIONARY:",std)
print("************")
#2.adding values to it
std[6]="Aarohi"
print("after add:",std)
print("************")
#3.updating the dict
std[3]="AKshu"
print("after updating:",std)
print("************")
#4.accesing a value for dict
a=std.get(6)
print("std with id 6:",a)
print("************")
#5.creating nest dict
nest_std={"A":{1:"ali",2:"ram"},"B":{3:"charu",4:"don"}}
print("Nested_dict:",nest_std)
print("************")
#6.accessing from nested_dict
print("stds in B:",nest_std["B"])
print("stds with ID 3 in B:",nest_std["B"][3])
print("************")
#7.printing all keys
print("keys in dict:",std.keys())
print("************")
#8.deleting a value from dict
del std[2]
print("After deletion ID 2:",std)
print("************")
