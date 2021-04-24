from pathlib import Path
import subprocess
import sys
from os import path, chdir, listdir
from gmanager import calculator, game, git_first_level, git_special_dirs, home_w, rest_test
from pathlib import Path
import requests
from itertools import islice


home = str(Path.home())

repo = 'react-app'
workspace = path.join(home_w, 'workspace1.code-workspace')

# url_api = 'https://api.github.com/user/repos'
# home_w = home_w.split('\\\\')[1]
# url='git@192.168.178.36:/gt/'
url = 'git@github.com:tik9/'
# url = 'https://github.com/tik9/'
url = path.join(url, repo)
# print(url)
# base, user, repo = url.rsplit('/', 2)

# local_path = repo
local_path = path.join(home, repo).replace('\\', '/')
# print(local_path)


def main():
    str_ = ''
    # clone()
    # remote_add()
    # description = 'Game Dev in Javascript'

    str_ = ch_workspace(True)
    # print(str_)
    with open(workspace, 'w') as file_:file_.write(str_)
    # print(new_repo())


def ch_workspace(rm=False):
    str = ''
    next_line_rm = False
    with open(workspace, 'r') as file_:
        # head = list(islice(file_, 8))

        for line in file_:
            if 'folders' in line:
                if not rm:
                    str += f'{line}{{\n"path": "{local_path}"\n}},'
                else:
                    str += line
                    next_line_rm = True
                continue
            if next_line_rm:
                next_line_rm = False
                continue
            if repo in line and rm:
                next_line_rm = True
                continue
            str += line
    return str


def remote_add():
    chdir(local_path)
    subprocess.check_call(['git', 'remote', 'add', 'origin', url])
    # subprocess.check_call(['git', 'remote', 'set-url', 'origin', url])
    subprocess.check_call(['git', 'remote', '-v'])


def clone():
    # print(url, local_path)
    # print(local_path)
    subprocess.check_call(['git', 'clone', url, local_path])


def new_repo():

    headers = {
        'Authorization': 'token <token>',
    }

    data = '{"name": "","description": ""}'

    response = requests.post(url_api, headers=headers, data=data)
    return response


def pull_new():
    subprocess.check_call(['git', 'init'])
    # subprocess.check_call(['git', 'pull', 'origin', 'master'])


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
