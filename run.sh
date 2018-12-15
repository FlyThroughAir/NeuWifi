#!/bin/bash

echo $(date)
workdir=$(cd $(dirname $0); pwd)
cd $workdir
echo $PWD

case $1 in
	login)
		nohup python3 MyWifi.py --type login >> nohup.out &;;
	logout)
		nohup python3 MyWifi.py --type logout >> nohup.out &;;

	*)
		echo "require login|logout"
esac
