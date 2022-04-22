# import
import os
import sys
import platform
import time
import shutil
import zipfile
import requests
import urllib3
import json
import wget

# define func
def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    for names in zip_file.namelist():
        zip_file.extract(names, 'update/')
    zip_file.close()

# initialize session
s = requests.session()
s.headers = {
    'Accept': 'application/vnd.github.v3+json'
}
urllib3.disable_warnings()

# initialize consts
github_release_api_url1 = 'https://api.github.com/repos/{owner}/{repo}/releases/latest'
#github_release_api_url2 = 'https://api.github.com/repos/{owner}/{repo}/releases/latest'

# read config.json
with open("config.json","r") as conf:
    updateConf = json.load(conf)
    conf.close()

{module1}ver = updateConf.get({module1})
## add more modules

response1 = s.get(github_release_api_url1, verify = False).text.strip('[]')
remoteVer1 = json.loads(response1).get('tag_name')

# compare local and remote
if remoteVer1 == {module1}ver:
    print('You have the latest release.')
    time.sleep(2)
    sys.exit()
else:
    print('A newer version has been released.')
    print('New:' + remoteVer1)
    print(json.loads(response1).get('body'))

    updateChoice = input('Update?(Y/N)')
    if updateChoice == 'Y' or updateChoice == 'y':
        os.mkdir('update')
        updateConf.update({module1}ver = remoteVer1)
    else:
        sys.exit()

    if platform.system() == 'Windows':
        sysType = 'win'
    elif platform.system() == 'Linux':
        sysType = 'linux'
    elif platform.system() == 'Darwin':
        sysType = 'osx'
    else:
        print('Unknown system')

    download_url = 'https://github.com/{owner}/{repo}/releases/download/' + remoteVer1 + '/{package_name}-' + sysType + '.zip'
    path = 'temp.zip'
    try:
        wget.download(download_url, path)
    except Exception as e:
        print('Error')
        print(e)
        sys.exit()

    un_zip('temp.zip')
    if os.path.exists('update/config.json'):
        os.remove('update/config.json')
    with open("update/config.json","w") as conf:
        json.dump(updateConf, conf)


    if sysType == 'win':
        os.system('start update.bat')
    elif sysType == 'linux' or sysType == 'osx':
        os.system('sh update.sh')
    sys.exit()