from os import path
from pathlib import Path
from github import Github
import socket

hostname = socket.gethostname()

home = str(Path.home())

repo = 'fritzbox'
# repo = 'gman'

local_path = path.join(home, repo)

with open(path.join(home, 'ghtoken'), 'r') as file_:
    token = file_.read()
    # print(token)
g = Github(token)


config = '.config'

# url='git@192.168.178.36:/gt/'
url = 'git@github.com:tik9/'
url = path.join(url, repo)
# print(url)
ws = home
workspace = path.join(ws, 'workspace.code-workspace')

if hostname == 't--pc':
    ws = path.join(home, config, 'Code/Workspaces/1619293380488'
    workspace=path.join(ws, '/workspace.json')
