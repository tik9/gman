from os import path
from pathlib import Path
from github import Github
import socket

hostname = socket.gethostname()
# print (hostname)
home = str(Path.home())

repo = 'gitconfig_win'
# repo = 'gman'

local_path = path.join(home, repo)
local_path = path.join('c','git','etc')

documents = path.join(home, 'documents')

powershell = path.join(home, 'Documents/WindowsPowerShell')
user_code = 'Code/User'
user = path.join(home, 'AppData/Roaming', user_code)
ws = home
workspace = path.join(ws, 'workspace.code-workspace')

addlist = [path.join(home, '.oh-my-zsh', 'custom')]
if hostname == 't--pc':
    config = '.config'
    documents = path.join(home, 'Dokumente')
    ws = path.join(home, config, 'Code/Workspaces/1619293380488')
    workspace = path.join(ws, '/workspace.json')

    addlist.append('/etc')
    openbox = path.join(home, config, 'openbox')
    powershell = path.join(home, config, 'powershell')
    user = path.join(home, config, user_code)

addlist.extend([powershell, user, ws])

with open(path.join(documents, 'ghtoken'), 'r') as file_:
    token = file_.read()
g = Github(token[:-1])
pygh_user=g.get_user()
# print(pygh_user.name)


# url='git@192.168.178.36:/gt/'
url = 'git@github.com:tik9/'
url = path.join(url, repo)
# print(url)
