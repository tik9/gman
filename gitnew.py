# https://stackoverflow.com/jobs/447895/database-reliability-engineer-the-remote-company

from pathlib import Path
import subprocess
import sys
from os import path, chdir, listdir
from gitmanager import git_first_level, git_special_dirs


home = path.dirname(path.dirname(path.abspath(__file__)))

workspace = path.join(home, 'workspace1.code-workspace')

# github_maintain = 'https://github.com/tik9/bewerbung.git'
github_maintain='git@192.168.178.36:/gt/bewerbung.git'

gith, user, repo = github_maintain.rsplit('/', 2)

local_path = path.join(home, repo)


def main():
    # clone()

    # description = 'Game Dev in Javascript'

    # str = add_workspace()
    # print(str)

    pull_new()
    # with open(path.join(local_path,readme), 'w') as f:

def pull_new():
    # subprocess.check_call(['git', 'init'])
    # subprocess.check_call(['git','remote','add','origin',github_maintain])
    subprocess.check_call(['git', 'pull', 'origin', 'master'])


def clone():
    str_ = f'{gith}/{user}/{repo}'
    # print(str_)
    # print(local_path)
    subprocess.check_call(['git', 'clone', str_, local_path])


def new_repo():

    headers = {
        'Authorization': 'token <token>',
    }

    data = '{"name":"<name>","description": "<message>"}'

    response = requests.post(
        'https://api.github.com/user/repos', headers=headers, data=data)
    return response


def fork():
    # print(gith, user, repo)
    chdir(home)
    clone()

    # subprocess.check_call(['git','remote','add','upstream',github_maintain])
    # subprocess.check_call(['git', 'pull', 'upstream', 'master'])


def prep_workspace():
    str = '{\n'
    str += '"folders":[\n'

    git_special_dirs.extend(git_first_level())

    for dir in git_special_dirs:
        str += f'{{"path":"{dir}"}},'

    str += ']}'
    return str


def add_workspace():
    str = ''
    with open(workspace, 'r') as f:
        for line in f:
            if 'folders' in line:
                str += f'{line}{{\n"path": "{repo}"\n}},'
            else:
                str += line
    return str



def aliase():
    repoShort = 'gh'
    cap = path.join(custom, 'plugins/common-aliases/common-aliases.plugin.zsh')
    cf = path.join(custom, 'common_functions.zsh')
    # pro = path.join(home, 'Documents/WindowsPowerShell/Microsoft.Powershell_profile.ps1')
    # with open(cap, 'a',) as f:f.write(f'\n{repoShort}=$HOME/{repoShort')

    with open(cf, 'a', encoding='utf8') as f:
        f.write(f'\nfunction {repoShort} {{ cd ${repoShort} }}')

    with open(cf, 'r') as f:
        print(f.read())

    # with open(pro, 'a', encoding='utf8') as f:f.write(f'\n${repoShort}="$hw/{repo}"')


if __name__ == "__main__":
    main()
