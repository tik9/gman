from os import path
from pathlib import Path
from github import Github
import socket

hostname = socket.gethostname()

home = str(Path.home())

repo = 'my-github-projects'
# repo = 'gman'

local_path = path.join(home, repo)
local_path = path.join(home)

custom = path.join(home, '.oh-my-zsh', 'custom')
powershell = path.join(home, 'Documents/WindowsPowerShell')
user_code = 'Code/User'
user = path.join(home, 'AppData/Roaming', user_code)
ws = home
workspace = path.join(ws, 'workspace.code-workspace')

if hostname == 't--pc':
    ws = path.join(home, config, 'Code/Workspaces/1619293380488')
    workspace = path.join(ws, '/workspace.json')

addlist = [custom, powershell, user, ws]
config = '.config'

if hostname == 't--pc':
    addlist.append('/etc')
    openbox = path.join(home, config, 'openbox')
    powershell = path.join(home, config, 'powershell')
    user = path.join(home, config, user_code)


with open(path.join(home, 'ghtoken'), 'r') as file_:
    token = file_.read()
# print(token)
g = Github(token)


# url='git@192.168.178.36:/gt/'
url = 'git@github.com:tik9/'
url = path.join(url, repo)
# print(url)
