import settings
import os
from pathlib import Path
from git import Repo

import subprocess
import sys

settings.init()
# sys.exit()

repo = 'git'
repoShort = 'gt'
cust = '.oh-my-zsh/custom'
cap = os.path.join(settings.homew, cust, 'plugins/common-aliases.plugin.zsh')
cf = os.path.join(cust, 'common_functions.zsh')
pro = os.path.join(
    settings.home, 'Documents/WindowsPowerShell/Microsoft.Powershell_profile.ps1')

dir = os.path.join(settings.homew, repo)
Path(dir).mkdir(exist_ok=True)
os.chdir(dir)
readme = os.path.join(dir, 'README.md')
# print(readme)

# if not os.path.exists(readme):os.mknod(readme)

repoCapital = dir.capitalize()

# print('listdir',os.listdir())
description = 'All scripts related to Git and Github such as Repo creation and fork'

# with open(readme, 'w', encoding='utf8'):pass
# with open(readme, 'w', encoding='utf8') as f:
    # f.write(f'## {repoCapital}\n{description}')
# for line in f:print(f)
# with open(cf, 'a', encoding='utf8') as f:f.write(f'function {repoShort} { cd ${reposhort} }')
# with open(cap, 'a', encoding='utf8') as f:f.write(f'{repoShort}=${dir})
# with open(pro, 'a', encoding='utf8') as f:f.write(f'\n${repoShort}="$hw/{repo}"')

# gi = git.cmd.Git(dir)
# gi.pull()
# gi.add('-A')
# grepo.git.commit('- m','first commit')
# git remote add origin 'https://github.com/tik9/'+repo+'.git
# git push - u origin master

# print('curdir', os.listdir(os.getcwd()))
# print('dir', dir)


def print_commit(commit):
    print('--')
    print(str(commit.hexsha))
    print(
        f"Message: {commit.summary},{commit.author.name}, {commit.author.email}")
    print(f'{commit.authored_datetime:%Y-%m-%d}')
    print(f"count commit: {commit.count()},size: {commit.size}")


def print_repository(repo):
    print(f'Repo description: {repo.description}')
    print(f'Repo active branch: {repo.active_branch}')
    for remote in repo.remotes:
        print(f'Remote named with URL: {remote}, {remote.url}')
    print(f'Last commit is {repo.head.commit.hexsha}')


# if __name__ == "__main__":
#     repo_path = os.getcwd()
#     repo = Repo(repo_path)
#     if not repo.bare:
#         print(f'Repo successfully loaded. {repo_path}')
#         print_repository(repo)
#         commits = list(repo.iter_commits('master'))[:5]
#         for commit in commits:
#             print_commit(commit)
#     else:
#         print('Could not load repository at {repo_path}')
