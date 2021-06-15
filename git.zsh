# set -x

ip=192.168.178.36
user=git
# user=tk;ip=192.168.178.23

gitremote() {

	 ssh $user@$ip \
	 '
	#  echo ip $ip
	gc=gitconfig
	lx=lx
	ws=workspaces
	# echo ${(C)ws}

	for elem in $gc $lx $ws ; do
	echo $elem
 	#  mkdir /gt/$elem.git 
	#  cd /gt/$elem.git
	#  git init --bare
	 done
	  '
}

gitlocal (){

	declare -A dirs
	# echo ${(t)dirs}

	if [[ "$HOST" == "tik" ]] ; then
		# ho=/mnt/c/Users/User
		dirs=([workspaces]=/mnt/c/Users/User)
		# echo host $HOST;
		git=/mnt/c/git/cmd/git.exe
	else
		git=/usr/bin/git
		config_dir=.config
		# lx=~/$config_dir/openbox
		# ws=~/$config_dir/Code/Workspaces/1619293380488	workspace_dir=~/$config_dir/Code/Workspaces/1619293380488
		dirs=( [lx]=~/$config_dir/openbox [workspaces]=~/$config_dir/Code/Workspaces/1619293380488 [gitconfig]=/etc )
	fi
	
	for name dir in ${(kv)dirs}; do
		cd $dir
		# pwd
		# ls
		# git remote add origin git@$ip:/gt/$name.git
		# git remote -v
		$git status
		$git add .
		$git commit -am "commit from git.zsh $HOST"
		$git push
	done
}
# gitremote
gitlocal

# echo $0 loaded
