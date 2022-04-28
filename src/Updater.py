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

# config inside
owner = ''
repo = ''
module_name = ''
package_name = ''

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
github_release_api_url = 'https://api.github.com/repos/' + owner + '/' + repo + '/releases/latest'

# delete old files
if os.path.exists('update'):
    shutil.rmtree('update')

# read config.json
with open("config.json","r") as conf:
    updateConf = json.load(conf)
    conf.close()

localVer = updateConf.get(module_name)
localVerVal = localVer.split('.')

response = s.get(github_release_api_url, verify = False).text.strip('[]')
remoteVer = json.loads(response).get('tag_name')
remoteVerNum = remoteVer.strip('v')
remoteVerVal = remoteVerNum.split('.')

# compare local and remote
verCount = len(localVerVal)
latest = True
for i in range(verCount):
    if localVerVal[i] < remoteVerVal[i]:
        latest = False

# compare operation
if latest:
    print('You have the latest release.')
    time.sleep(2)
    sys.exit()
else:
    print('A newer version has been released.')
    print('New:' + remoteVer)
    print(json.loads(response).get('body'))

    updateChoice = input('Update?(Y/N)')
    if updateChoice == 'Y' or updateChoice == 'y':
        os.mkdir('update')
        updateConf[module_name] = remoteVer
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

    download_url = 'https://github.com/' + owner + '/' + repo + '/releases/download/' + remoteVer + '/' + package_name + '-' + sysType + '.zip'
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