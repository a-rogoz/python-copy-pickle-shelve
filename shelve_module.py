import shelve


shelve_name = "shelve.shiv"

my_shelve = shelve.open(shelve_name, flag="c")
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve["USD"])
new_shelve.close()

# 'r'	Open existing database for reading only
# 'w'	Open existing database for reading and writing
# 'c'	Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
# 'n'	Always create a new, empty database, open for reading and writing


# Treat a shelve object as a Python dictionary, with a few additional notes:

# the keys must be strings;
# Python puts the changes in a buffer which is periodically flushed to the disk. To enforce an immediate flush, call the sync() method on your shelve object;
# when you call the close() method on an shelve object, it also flushes the buffers.