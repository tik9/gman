from pathlib import Path
import subprocess
import sys
from os import path

home = path.dirname(path.dirname(__file__))
settingsDir = path.join(home, 'tesseractToMarkdown')
sys.path.append(settingsDir)
from helper import gitFirstLevel
from settings import color, custom, gitSpecialDirs, readme

workspace = path.join(home, 'workspace1.code-workspace')

github = 'https://github.com'

# user = 'MichaelCurrin'
# repo = 'my-github-projects'

# local_path = path.join(home, repo)


def main():
    # aliase()
    # clone()
    # Path(dir).mkdir(exist_ok=True)

    description = 'Jekyll Use in Github Pages'
    # repoCapital = repo.capitalize()
    # str = prepWorkspace()
    # str = addWorkspace()
    fork()
    # print(str)

    # with open(workspace,'w') as f:f.write(str)

    # with open(path.join(local_path,readme), 'w') as f:
    # f.write(f'## {repo.capitalize()}\n\n<br>{description}')


def fork():
    # repogit = f'{github}/{user}/{repo}'
    repogit = 'https://g/M/m'
    # user, repo, t,v = repogit.split('/')
    # print(user[1])
    gihu, user, repo = repogit.rsplit('/', 2)
    print(gihu, user, repo)

    # git remote add upstream repoMaintainer
    # git pull upstream master


def clone():
    subprocess.Popen(['git', 'clone', github + '/' +
                      user + '/' + repo + '.git', local_path])


def prepWorkspace():
    str = '{\n'
    str += '"folders":[\n'
    gitSpecialDirs.extend(gitFirstLevel())
    for dir in gitSpecialDirs:
        str += f'{{"path":"{dir}"}},'

    str += ']}'
    return str
    # with open(workspace, 'w') as f:f.write(str)


def addWorkspace():
    str = ''
    with open(workspace, 'r') as f:
        for line in f:
            if 'folders' in line:
                str += f'{line}{{\n"path": "{local_path}"\n}},'
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
