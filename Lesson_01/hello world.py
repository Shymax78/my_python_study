print("Hello world")
string = "Hello my world"
print (string)
int_1 = 5
int_2 = 7
print (type(int_1),(int_2))
name_1 = int_1 == int_2
print (name_1)
print (type(name_1))
list = ["apple", "banana", "pineapple", "potatoes"]
print(type(list))

dict = {"Name":"Petro","age":"30","where":"Kyiv"}
print (type(dict))

Tuple = (1, 2, 3, 5, 6, 7, 9)
print (type(Tuple))

none = ()
print (type(none))

num_str = 125
string = str(num_str)
print (string)
print (type(string))

string = "Hi, my name is Python!"
print (string)
string = string.replace ("y", "0",)
print (string)
string = string.replace ("i", "1")
print (string)

split_test = "This is a split test"
split_test = split_test.split()
print (split_test)



string_join = " ".join(split_test)
print (string_join)

print(len(string_join))



list_append = [1, 2, 3]
print(len(list_append))
list_append.append (4)
list_append.append (5)
print (list_append)

list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))
print(len(list_append))


dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}

print(dict_test["car"], dict_test["where"])

print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())

