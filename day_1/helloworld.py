from sys import stdout, version
from os import write
import cmath
NoneType = type(None)
name = "Gabo"
family_name = "Barn"
country = "Uruguay"

stdout.write(version + '\n')
a = 3; b = 4
stdout.write(str(a+b)+'\n')
stdout.write(str(a-b)+'\n')
stdout.write(str(a*b)+'\n')
stdout.write(str(a%b)+'\n')
stdout.write(str(a/b)+'\n')
stdout.write(str(a**b)+'\n')
stdout.write(str(a//b)+'\n')

def write_to_stdout(strg=""):
    try:
        strg = str(strg)
    except Exception:
        stdout.write("Couldn't convert to str\n")
        return
    write(stdout.fileno(), (strg + "\n").encode())

def check_data_type(data):
    match data:
        case _ if isinstance(data, int):
            write_to_stdout("Data Type is Int")
        case _ if isinstance(data, float):
            write_to_stdout("Data Type is Float")
        case _ if isinstance(data, str):
            write_to_stdout("Data Type is String")
        case _ if isinstance(data, list):
            write_to_stdout("Data Type is List")
        case _ if isinstance(data, dict):
            write_to_stdout("Data Type is Dict")
        case _ if isinstance(data, bool):
            write_to_stdout("Data Type is Bool")
        case _ if data is None:
            write_to_stdout("Data Type is NoneType")
        case _:
            write_to_stdout("Unknown Data Type")


write_to_stdout(name+' '+family_name+' '+country)
check_data_type(10)
check_data_type(9.8)
check_data_type(3.14)
check_data_type(4 - 4j)
check_data_type(['Asabeneh', 'Python', 'SPAM'])
check_data_type(name)
check_data_type(family_name)
check_data_type(country)

integer = 40
floating = 23.42
complexNum = complex(a, b)
print(complexNum)
isNeg = a < 0
print(isNeg)
list1 = list([1, 2, 3, 4])
tuple1 = tuple((1, 2, 3, 4))
set1 = set([1, 2, 3, 4])
dictionary1 = dict(Albert=31, Sonya=23)
tuple_dict1 = dict([('Albert', 31), ('Sonya', 23)])
print(list1)
print(tuple1)
print(set1)
print(dictionary1)
print(tuple_dict1)

# todo: eucladian difference