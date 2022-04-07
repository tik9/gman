from os import chdir, getcwd, path, walk
from pathlib import Path
from github import Github
import socket
import sys


home = str(Path.home())

sysex = sys.executable

hostname = socket.gethostname()
w_home = path.join('/', 'mnt', 'c', 'users', 'user')

gm_folder = path.dirname(__file__)
home_folder = path.dirname(gm_folder)

repo = 'php'
repo = 'vscode'

# local_path = path.join(home_folder, repo)
local_path = path.join(home_folder, 'Library',
                       'Application Support', 'Code/User')

gh_url = 'git@github.com:tik9/'
repo_url = path.join(gh_url, repo)

user_code = 'Code/User'
user = path.join(home_folder, 'AppData/Roaming', user_code)

with open(path.join(gm_folder, 'ghtoken'), 'r') as file_:
    token = file_.read()

ws = 'workspace.code-workspace'
workspace = path.join(home_folder, ws)

if hostname == 'tik':
    workspace = path.join(w_home, ws)

if hostname == 't--pc':
    documents = path.join(home_folder, 'Dokumente')
    config = '.config'
    token = token[:-1]
    ws = path.join(home_folder, config, 'Code/Workspaces/1619293380488')
    workspace = path.join(ws, 'workspace.json')
    user = path.join(home_folder, config, user_code)


g = Github(token)
pygh_user = g.get_user()
# print(next(walk('.'))[2])
