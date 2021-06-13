
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

	config_dir=.config
	# lx=~/$config_dir/openbox
	# ws=~/$config_dir/Code/Workspaces/1619293380488
	declare -A inf
	# echo ${(t)inf}

	inf=( [lx]=~/$config_dir/openbox [workspaces]=~/$config_dir/Code/Workspaces/1619293380488 [gitconfig]=/etc )
	for name dir in ${(kv)inf}; do

		cd $dir
		pwd
		# git remote add origin git@$ip:/gt/$name.git
		git remote -v
	done
}
# gitremote
gitlocal

# echo $0 loaded
