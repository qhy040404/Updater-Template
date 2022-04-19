# import
import os
import sys
import platform
import zipfile
import requests
import json
import wget

# define func
def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir('update'):
        pass
    else:
        os.mkdir('update')
    for names in zip_file.namelist():
        zip_file.extract(names, 'update/')
    zip_file.close()

# initialize session
s = requests.session()
s.headers = {
    'Accept': 'application/vnd.github.v3+json'
}

# initialize consts
github_release_api_url1 = 'https://api.github.com/repos/{owner}/{repo}/releases'
#github_release_api_url2 = 'https://api.github.com/repos/{owner}/{repo}/releases'

# read config.json
with open("config.json","r") as conf:
    updateConf = json.load(conf)

if updateConf.get('channel') == 'stable':
    github_release_api_url += '/latest'
elif updateConf.get('channel') == 'beta':
    github_release_api_url += '?per_page=1'
else:
    print('Unknown channel.')

{module1} = updateConf.get({module1})
## add more modules

response1 = s.get(github_release_api_url1, verify = False).text.strip('[]')
remoteVer1 = json.loads(response1).get('tag_name')

# compare local and remote
if remoteVer1 is {module1}:
    print('You have the latest release.')
else:
    print('A newer version has been released.')
    print('New:' + remoteVer1)
    print(json.loads(response1).get('body'))

    if platform.system() == 'Windows':
        sysType = 'win'
    elif platform.system() == 'Linux':
        sysType = 'linux'
    elif platform.system() == 'Darwin':
        sysType = 'osx'
    else:
        print('Unknown system')

    download_url = 'https://github.com/{owner}/{repo}/releases/download/{tag_name}/{package_name}-' + sysType + '.zip'
    path = 'temp.zip'
    wget.download(download_url, path)

    un_zip('temp.zip')

    if sysType == 'win':
        os.system('update.bat')
    elif sysType == 'linux' or sysType == 'osx':
        os.system('update.sh')
    sys.exit()