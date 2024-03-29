import subprocess
from os import path, walk
from settings import *
from git import Repo

excludedirs = ['.oh-my-zsh', 'apps', 'gman']

def main():
    # chdir(local_path)
    # dlist = dwalk()
    # dlist.extend(addlist)
    print(ghrepos())
    # delete_ghrepo()


def localrepos(dlist):
    resultlist = []
    for dir in dlist:

        # chdir(repo)
        repo = Repo(dir).git
        result = repo.status()
        # result = repo.pull()
        # result=repo.diff()
        resultlist.append(result)

        # run('diff', '--summary')
        # run('diff')
        # | grep --color "mode change 100644 => 100755"'
    return resultlist


def ghrepos():
    repos = []
    for repo in pygh_user.get_repos():
        repos.append(repo.name)
    return list(enumerate(repos))


def dwalk():
    dlist = []
    for root, dirs, files in walklevel():
        if '.git' in dirs:
            if not(any(excl in root for excl in excludedirs)):
                dlist.append(root)

    return dlist


def walklevel():
    num_sep = home_folder.count(path.sep)
    for root, dirs, files in walk(home_folder):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


def run(*args):
    return subprocess.Popen(['git'] + list(args))


def delete_ghrepo():
    for repo in repos:
        ghrepo = pygh_user.get_repo(repo)
        # ghrepo.delete()


if __name__ == '__main__':
    main()
