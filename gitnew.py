from pathlib import Path
import subprocess
import sys
from os import path, chdir, listdir
from gitmanager import git_first_level, git_special_dirs
from pathlib import Path

home_w = path.dirname(path.dirname(path.abspath(__file__)))
home = str(Path.home())

workspace = path.join(home_w, 'workspace1.code-workspace')

# url = 'https://github.com/tik9/game'
url = 'git@192.168.178.36:/gt/bewerbung'

# base, user, repo = url.rsplit('/', 2)
repo = url.rsplit('/', 1)[1]

local_path = path.join(home, 'downloads', 'PortableJekyll-master', repo)


def main():
    # clone()

    # description = 'Game Dev in Javascript'

    str_ = add_workspace()
    # print(str_)
    with open(workspace, 'w') as f:f.write(str_)


def add_workspace():
    str = ''
    with open(workspace, 'r') as f:
        for line in f:
            if 'folders' in line:
                str += f'{line}{{\n"path": "{local_path}"\n}},'
            else:
                str += line
    return str


def clone():
    # print(url, local_path)
    # print(local_path)
    subprocess.check_call(['git', 'clone', url, local_path])


def pull_new():
    # subprocess.check_call(['git', 'init'])
    # subprocess.check_call(['git','remote','add','origin',url])
    subprocess.check_call(['git', 'pull', 'origin', 'master'])


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

    # subprocess.check_call(['git','remote','add','upstream',url])
    # subprocess.check_call(['git', 'pull', 'upstream', 'master'])


def prep_workspace():
    str = '{\n'
    str += '"folders":[\n'

    git_special_dirs.extend(git_first_level())

    for dir in git_special_dirs:
        str += f'{{"path":"{dir}"}},'

    str += ']}'
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
