import importlib

#defining the dynamic plugin system

# plugin_var="plugin.plugin_one"
plugin_var="plugin.plugin_two"

auth_plugin=importlib.import_module(plugin_var,".")

#creating a Plugin class object

auth_plugin.Plugin(name="rika",full_name="abismruta sarangi")

# print(auth_plugin)