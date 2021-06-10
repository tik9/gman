from os import path
from pathlib import Path
from github import Github

home = str(Path.home())

repo = 'fritzbox'

local_path = path.join(home, repo)

with open(path.join(home, 'ghtoken'), 'r') as file_:
    token = file_.read()
    # print(token)
g = Github(token)

config = '.config'
user_code = 'Code/User'
# user = path.join(home, 'AppData/Roaming', user_code)
user = path.join(home, config, user_code)

workspace = config + '/Code/Workspaces/1619293380488/workspace.json'
# workspace='workspace1.code-workspace'
workspace = path.join(home, workspace)

url_api = 'https://api.github.com/user/repos'

# url='git@192.168.178.36:/gt/'
url = 'git@github.com:tik9/'
url = path.join(url, repo)
# print(url)
