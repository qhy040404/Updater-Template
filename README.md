# Updater Template
This is a template of updater.
## Use
- You need to change data in ```config.json``` and ```Updater.py```
## Detail
- ```config.json```
    - ```channel``` : ```stable``` or ```beta```
        - ```stable``` requests the latest release version
        - ```beta``` requests the latest pre-release version
    - ```{module1}``` is the module name which is defined by you
    - Just add more module if you have more module in one project.
- ```Updater.py```
    - ```%7Bowner%7D``` is your GitHub name
    - ```{repo}``` is your repository name
    - ```{module1}``` is the local version defined in ```config.json```
    - ```{package_name}``` is the universal name that is used in GitHub Release.