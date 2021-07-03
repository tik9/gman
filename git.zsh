# set -x

ip=192.168.178.36
user=git
# user=tk;ip=192.168.178.23

# echo ${(%):-%F{green}}text${(%):-%f}


gitlocal (){

	declare -A dirs
	# echo ${(t)dirs}

	if [[ "$HOST" == "tik" ]] ; then
		# echo host $HOST;
		mntc=/mnt/c
		gitdir=$mntc/git
		ho=$mntc/Users/User
		dirs=(
			# [workspaces]=$ho
			[gitconfig_win]=$gitdir/etc
			# [vsco]=$ho/appdata/roaming/code/user
		)
		git=$gitdir/cmd/git.exe
	else
		config_dir=.config
		
		dirs=( 
			[gitconfig]=/etc 
			[lx]=~/$config_dir/openbox
			[vsco]=~/$config_dir/Code/User
			[workspace_linux]=~/$config_dir/Code/Workspaces/1619293380488
		)
		
		git=/usr/bin/git
	fi
	# printf '%s\n' "${(%):-green}$text${(%):-%f}"

	for name dir in ${(kv)dirs}; do
		cd $dir
		pwd
		# ls
		# git remote add origin git@$ip:/gt/$name.git
		# $git remote -v
		# $git status

		# $git add .
		# $git commit -am "commit from git.zsh $HOST"
		# $git push --set-upstream origin master
		$git pull
		# $git diff --summary
	done
}

gitremote() {

	 ssh $user@$ip \
	 '
	fs=gitconfig_win

	echo ${(C)fs}

	for elem in $fs ; do
	# echo $elem
 	 mkdir /gt/$elem.git 
	 cd /gt/$elem.git
	 git init --bare
	 done
	  '
}

# gitremote
gitlocal

# echo $0 loaded
