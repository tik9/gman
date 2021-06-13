
arr01=('lx' 'lxqt/')
arr02=('ws' 'work/')
arr1=(arr01 arr02)

# arr1=((0 '1 2') (3 4))

declare -n elmv1
for elmv1 in "${arr1[@]}"; do
	for elm in "${elmv1[@]}"; do
		echo $elm
	done
done

# array=('d1=(v1 v2)' 'd2=(v1 v2)')
# for elt in "${array[@]}";do eval $elt;done
# echo "d1 ${#d1[@]} ${d1[@]}"
# echo "d2 ${#d2[@]} ${d2[@]}"

# echo $0 loaded
