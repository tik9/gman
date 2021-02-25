from pathlib import Path
import subprocess
import sys
from os import path, chdir, listdir
from gitmanager import git_first_level, git_special_dirs


home = path.dirname(path.dirname(__file__))

workspace = path.join(home, 'workspace1.code-workspace')


github_maintain = ''
github_maintain = 'https://github.com/tik9/game'

gith, user, repo = github_maintain.rsplit('/', 2)
# user = 'tik9'

local_path = path.join(home, repo)


def main():
    # aliase()
    # clone()
    # Path(dir).mkdir(exist_ok=True)

    description = 'Game Dev in Javascript'

    # with open(workspace, 'r') as f:print(f.read())

    # str = add_workspace()
    # print(str)
    # with open(workspace,'w') as f:f.write(str)

    # fork()

    # repoCapital = repo.capitalize()
    # with open(path.join(local_path,readme), 'w') as f:
    # f.write(f'## {repo.capitalize()}\n\n<br>{description}')


def new_repo():

    headers = {
        'Authorization': 'token e5f9a4b83b05d4fa8e552d4aef7bd29f6af30103',
    }

    data = '{"name":''}'

    response = requests.post(
        'https://api.github.com/user/repos', headers=headers, data=data)
    return response


def fork():
    # print(gith, user, repo)
    chdir(home)
    clone()

    # subprocess.check_call(['git','remote','add','upstream',github_maintain])
    # subprocess.check_call(['git', 'pull', 'upstream', 'master'])


def clone():
    str = f'{gith}/{user}/{repo}'
    # print(local_path)
    subprocess.check_call(['git', 'clone', str, local_path])


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


def print_commit(commit):
    str += '--'
    str += str(commit.hexsha)
    str += f"Message: {commit.summary},{commit.author.name}, {commit.author.email}"
    str += f'{commit.authored_datetime:%Y-%m-%d}'
    str += f"count commit: {commit.count()},size: {commit.size}"
    return str


def print_repository(repo):
    str += f'Repo description: {repo.description}'
    str += f'Repo active branch: {repo.active_branch}'
    for remote in repo.remotes:
        str += f'Remote named with URL: {remote}, {remote.url}'
    str += f'Last commit is {repo.head.commit.hexsha}'
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
