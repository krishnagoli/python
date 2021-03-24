my_string="Hello world"
print(my_string.isalpha())
Output : False

str1="HelloWorld"
print(str1.isalpha())
Output : True

str="hfdgkjfdhg"
print(str.isdigit())
Output : False

str="hfdgkjfdhg123"
print(str.isdigit())
Output : False

str="45435435435h"
print(str.isdigit())
Output : False

str="45435435435"
print(str.isdigit())
Output : True

a="Hello world"
print(a.isalnum())
Output : False

str2="356546"
print(str2.isalnum())
Output : True

str1="HELLO"
print(str1.isupper())
Output : True

str5="H78"
print(str5.isupper())
Output : True

str="Hello"
print(str.isupper())
Output : False

a='hello'
print(a.islower())
Output : True

a='Hello'
print(a.islower())
Output : False

a="hkh6767"
print(a.islower())
Output : True

b='Hello World'
print(b.endswith('d'))
Output : True

b='Hello World'
print(b.startswith('H'))
Output : True
