# import
import json
import os.path

# Read file to check if generated
if os.path.exists("config.json"):
    print("config.json detected. Ensure you want to generate a new config.")

# pre-define counter and saver
n = 0
s = []


# define func
def newData(counter):
    owner = input("Repo Owner:")
    repo = input("Repo name:")
    module_name = input("Module name:")
    package_name = input("Downloadable package name:")
    start_version = input("Version Preset:")
    a = {'owner' + counter: owner, 'repo' + counter: repo, 'module_name' + counter: module_name,
         'package_name' + counter: package_name, module_name: start_version}
    return a


# main
moredata = True
while moredata:
    s[n] = newData(n + 1)
    confirm = input("More Data?(Y/N)")
    if confirm == 'Y' or confirm == 'y':
        moredata = True
    else:
        moredata = False
    if moredata is True:
        n += 1

# Add data into a dict
final = {}
for i in range(n):
    final.update(s[i])

# Write file
with open("config.json", "w") as conf:
    json.dump(final, conf)

print("Success")
