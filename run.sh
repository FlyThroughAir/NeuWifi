#!/bin/bash

echo $(date)
workdir=$(cd $(dirname $0); pwd)
cd $workdir
echo $PWD
nohup python3 MyWifi.py >> nohup.out &
