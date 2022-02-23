from os import chdir, getcwd, path, sep
from pathlib import Path
from github import Github
import socket
import sys

pythonex = path.dirname(sys.executable)

hostname = socket.gethostname()
home = str(Path.home())

script_folder = path.dirname(__file__)

repo = 'spa'

documents = path.join(home, 'documents')
# local_path = path.join('c:' + sep, 'git', 'etc')

local_path = path.join(home, repo)

if hostname == 't--pc':
    documents = path.join(home, 'Dokumente')

# print(chdir(local_path))

# url = 'git@192.168.178.36:/gt/'
gh_url = 'git@github.com:tik9/'
repo_url = path.join(gh_url, repo)

powershell = path.join(documents, 'windowspowershell')

user_code = 'Code/User'
user = path.join(home, 'AppData/Roaming', user_code)

workspace = path.join(home, 'workspace.code-workspace')

custom = path.join(home, '.oh-my-zsh', 'custom')
addlist = [custom]

with open(path.join(script_folder, 'ghtoken'), 'r') as file_:
    token = file_.read()
ws = ''
if hostname == 't--pc':
    config = '.config'
    token = token[:-1]
    ws = path.join(home, config, 'Code/Workspaces/1619293380488')
    workspace = path.join(ws, 'workspace.json')
    addlist.append('/etc')
    openbox = path.join(home, config, 'openbox')
    powershell = path.join(home, config, 'powershell')
    user = path.join(home, config, user_code)

addlist.extend([powershell, user, ws])

g = Github(token)
pygh_user = g.get_user()
print(pygh_user)
