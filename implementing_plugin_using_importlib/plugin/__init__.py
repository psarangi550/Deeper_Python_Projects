import importlib

os=importlib.import_module("os")

eval("importlib.import_module('os').system('ls')")

eval("importlib.import_module('os')")

exec("importlib.import_module('os')")

# eval("a=10")

exec("a=10")

print(a)