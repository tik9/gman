import subprocess
from os import path, chdir
from settings import *


def main():
    # clone()
    chdir(local_path)
    # remote_addchange()
    # new_repo()

    # str_ = ch_workspace()
    # with open(workspace, 'w') as file_:
    # file_.write(str_)
    # print(str_)
    push_new()


def remote_addchange():
    # subprocess.check_call(['git', 'remote', 'add', 'origin', url])
    print(local_path,url)
    subprocess.check_call(['git', 'remote', 'set-url', 'origin', url])
    subprocess.check_call(['git', 'remote', '-v'])


def clone():
    # print(url, local_path)
    # print(local_path)
    subprocess.check_call(['git', 'clone', url, local_path])


def new_repo():
    new = g.get_user().create_repo(repo)
    print(new.json())


def push_new():
    subprocess.check_call(
        ['git', 'push', '--set-upstream', 'origin', 'master'])


def ch_workspace():
    str_ = ''
    with open(workspace, 'r') as file_:
        # head = list(islice(file_, 8))
        for line in file_:
            # print(line)
            if 'folders' in line:
                str_ += f'{line}{{\n"path": "{local_path}"\n}},'
                continue
            str_ += line
    return str_


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
