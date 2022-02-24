import subprocess
from os import chdir, path, walk
from settings import *
from git import Repo

# 'custom'
excludedirs = ['.oh-my-zsh', 'gman', 'ghtemplate']


def main():
    # chdir(local_path)
    repo = 'game'
    # delete_ghrepo(repo)
    # run('commit','-am','first commit')
    # delete_localrepo(path.join(home,repo))
    dlist = dwalk()
    # dlist.extend(addlist)
    localrepos(dlist)
    # print(dlist)
    # print(ghrepos())


def localrepos(dlist):
    # print(type(dlist))
    for dir in dlist:

        # chdir(repo)
        print(dir+'\n')
        repo = Repo(dir).git
        # result = repo.status()
        result = repo.pull()
        # result=repo.diff()
        print(result)

        # run('diff', '--summary')
        # run('diff')
        # | grep --color "mode change 100644 => 100755"'
        # commit(repo)
    return 0


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
    num_sep = base_folder.count(path.sep)
    for root, dirs, files in walk(base_folder):
        yield root, dirs, files
        dirs.sort()
        num_sep_this = root.count(path.sep)
        if num_sep + 1 <= num_sep_this:
            del dirs[:]


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def delete_ghrepo(repo):
    repo = pygh_user.get_repo(repo)
    repo.delete()


if __name__ == '__main__':
    main()
