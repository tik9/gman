from os import path
from pathlib import Path
from github import Github
import socket
import sys


home = str(Path.home())

sysex = sys.executable

hostname = socket.gethostname()

gm_folder = path.dirname(__file__)
home_folder = path.dirname(gm_folder)

repos = ['tik']

local_path = path.join(home_folder, repos[0])

local_path = path.join(
        home_folder, 'Library Application Support', 'Code/User')

gh_url = 'git@github.com:tik9/'
repo_url = path.join(gh_url, repos[0])

user_code = 'Code/User'
user = path.join(home_folder, 'AppData/Roaming', user_code)

with open(path.join(gm_folder, '.env'), 'r') as file_:
    token = file_.readlines()[0].split('=')[1]

if hostname == 't--pc':
    documents = path.join(home_folder, 'Dokumente')
    config = '.config'
    token = token[:-1]
    ws = path.join(home_folder, config, 'Code/Workspaces/1619293380488')
    user = path.join(home_folder, config, user_code)


print(token)
g = Github(token)
pygh_user = g.get_user()
