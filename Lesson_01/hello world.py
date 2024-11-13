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
string = str("num_str")
print (string)
print (type(string))

string = "Hi, my name is Python!"
string = string.replace ("y", "0",)
print (string)
string = string.replace ("i", "1")
print (string)

split_test = "This is a split test"
split_test = split_test.split()
print (split_test)


string = str (split_test)
string = string.join(split_test)
split_test = string
print (split_test)