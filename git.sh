# set -x

arr01=('lx' 'lxqt/')
arr02=('ws' 'work/')
arr1=(arr01 arr02)

if [[ "$HOSTNAME" == "tik" ]]; then
	echo host $HOSTNAME
else
	echo 'lubuntu'
fi

declare -n elmv
for elmv in "${arr1[@]}"; do
	for elm in "${elmv[@]}"; do
		echo $elm
	done
done

# array=('d1=(v1 v2)' 'd2=(v1 v2)')
# for elt in "${array[@]}";do eval $elt;done
# echo "d1 ${#d1[@]} ${d1[@]}"
# echo "d2 ${#d2[@]} ${d2[@]}"

# echo $0 loaded
