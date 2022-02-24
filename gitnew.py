from os import makedirs
import shutil
from settings import *
from os import chdir
import subprocess
from git import Repo
import git


def main():
    pass
    # chdir(local_path)
    # new_localrepo()
    # str_ = new_ghrepo()
    # str_=clone()

    # str_ = ch_workspace()
    # with open(workspace, 'w') as file_: file_.write(str_)
    # add_ignore()
    # str_ = new_ghrepo()
    # str_ = remote_addchange()
    # push_new()
    # readme()
    # print(str_)


def new_ghrepo():
    new = g.get_user().create_repo(repo)
    return new


def clone():
    try:
        repo = Repo.clone_from(repo_url, local_path)
        return repo
    except git.exc.InvalidGitRepositoryError:
        print('error here')


def new_localrepo():
    makedirs(local_path, exist_ok=True)
    repo = git.Repo.init(local_path)


def remote_addchange():
    chdir(local_path)
    subprocess.check_call(['git', 'remote', 'add', 'origin', repo_url])
    return subprocess.check_call(['git', 'remote', '-v'])


def add_ignore_readme():
    src = path.join(base_folder, 'ghtemplate', '.gitignore')
    shutil.copy(src, local_path)
    src = path.join(base_folder, 'ghtemplate', 'README.md')
    shutil.copy(src, local_path)


def push_new():
    subprocess.check_call(
        ['git', 'push', '--set-upstream', 'origin', 'master'])


def ch_workspace():
    str_ = ''
    with open(workspace, 'r') as file_:
        # head = list(islice(file_, 8))
        for line in file_:
            print(line)
            if 'folders' in line:
                str_ += f'{line}{{\n"path": "{local_path}"\n}},'
                continue
            str_ += line
    return str_


if __name__ == "__main__":
    main()
