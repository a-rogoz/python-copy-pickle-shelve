import pickle


a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open("multidata.pckl", "wb") as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)


with open("multidata.pckl", "rb") as file_in:
    data1 = pickle.load(file_in)
    data2 = pickle.load(file_in)

print(type(data1))
print(data1)
print(type(data2))
print(data2)

# Send via network or store in database
bytes = pickle.dumps(a_list)
print("Intermediate object type, used to preserve data:", type(bytes))

b_list = pickle.loads(bytes)
print("A type of deserialized object:", type(b_list))
print("Contents:", b_list)

# Attempts to pickle non-pickleable objects will raise the
# PicklingError exception.

# Trying to pickle a highly recursive data structure (mind the cycles)
# may exceed the maximum recursion depth, and a RecursionError
# exception will be raised in such cases.

# The code that calls the load() or loads() functions of pickle should
# already know the function/class definition.