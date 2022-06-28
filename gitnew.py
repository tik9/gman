from os import makedirs
import shutil
from settings import *
from os import chdir
from git import Repo
import git
from gmanager import run


def main():
    # new_localrepo()
    # str_ = new_ghrepo()
    str_=clone()

    # str_ = ch_workspace()
    # with open(workspace, 'w') as file_:
    #     file_.write(str_)
    # str_ = new_ghrepo()
    # str_ = remote_add()
    # ignore_readme_add()
    # push_new()

    print(str_)
    pass

def clone():
    try:
        repo = Repo.clone_from(repo_url, local_path)
        return repo
    except git.exc.InvalidGitRepositoryError:
        print('error here')

def new_ghrepo():
    new = g.get_user().create_repo(repo)
    return new


def new_localrepo():
    makedirs(local_path, exist_ok=True)
    git.Repo.init(local_path)

    chdir(local_path)
    run('remote', 'add', 'origin', repo_url)
    return run('remote', '-v')


def ignore_readme_add():
    src = path.join(home_folder, 'ghtemplate', '.gitignore')
    shutil.copy(src, local_path)
    src = path.join(home_folder, 'ghtemplate', 'README.md')
    shutil.copy(src, local_path)


def push_new():
    chdir(local_path)
    run('add', '.')
    run('commit', '-am', 'first commit')
    run('push', '--set-upstream', 'origin', 'master')


def ch_workspace():
    str_ = ''
    with open(workspace, 'r') as file_:
        for line in file_:
            if 'folders' in line:
                str_ += f'{line}{{\n"path": "{local_path}"\n}},'
                continue
            str_ += line
    return str_


if __name__ == "__main__":
    main()
