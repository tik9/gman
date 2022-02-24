from os import path
from pathlib import Path
from github import Github
import socket
import sys

sysex = sys.executable

hostname = socket.gethostname()
home = str(Path.home())
w_home = path.join('/', 'mnt', 'c', 'users', 'user')

script_folder = path.dirname(__file__)
base_folder = path.dirname(script_folder)

repo = 'spa'

documents = path.join(base_folder, 'documents')

local_path = path.join(base_folder, repo)

if hostname == 't--pc':
    documents = path.join(home, 'Dokumente')

gh_url = 'git@github.com:tik9/'
repo_url = path.join(gh_url, repo)

powershell = path.join(documents, 'windowspowershell')

user_code = 'Code/User'
user = path.join(base_folder, 'AppData/Roaming', user_code)

custom = path.join(base_folder, '.oh-my-zsh', 'custom')
addlist = [custom]

with open(path.join(script_folder, 'ghtoken'), 'r') as file_:
    token = file_.read()
workspace = path.join(w_home, 'workspace.code-workspace')
if hostname == 't--pc':
    documents = path.join(base_folder, 'Dokumente')
    config = '.config'
    token = token[:-1]
    ws = path.join(base_folder, config, 'Code/Workspaces/1619293380488')
    workspace = path.join(ws, 'workspace.json')
    addlist.append('/etc')
    openbox = path.join(base_folder, config, 'openbox')
    powershell = path.join(base_folder, config, 'powershell')
    user = path.join(base_folder, config, user_code)

# addlist.extend([powershell, user, ws])

g = Github(token)
pygh_user = g.get_user()
# print(pygh_user)
