bold=$(tput bold)
norm=$(tput sgr0)

home=/home/tk
# home=\\wsl$\debian/home/tk
# w_home=/mnt/c/Users/User
repo=(
    .config/Code/User
    .config/powershell
    .oh-my-zsh/custom
)
cmds=(pull)
commit='Newest commit'
# ======== Ende Settings

echo -e "\n[*** Start Gitman"

function gi_do() {
    cd $1
    for cmd in "${cmds[@]}"; do
        echo -e "\n$bold[***  Git $cmd: " $1 $normal
        git $cmd 
        # --porcelain >> log.txt
    done
}

# remote update
# cmd='add .'
# cmd="commit -m '$commit'"
# cmd=push
# clone https://github.com/tik9/$elem.git $home/$elem

for elem in ${repo[@]}; do
    gi_do $home/$elem
    # git "$elem"
    # echo $home/$elem
done

cm_find=$(find $home -maxdepth 1 -not -type f -and -not -name '.*')

for elem in $cm_find; do
    if [ -d $elem/.git ]; then
        gi_do $elem
        # echo $elem
    fi
done

echo -e "\n[*** End Gitman"
