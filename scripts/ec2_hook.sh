#!/bin/bash
export PATH="/home/ubuntu/miniconda2/bin:$PATH"

while read oldrev newrev ref
do
  branch=`echo $ref | cut -d/ -f3`
  if [ "ec2" == "$branch" -o "master" == "$branch" ]; then
    git --work-tree=/home/ubuntu/app/ checkout -f $branch
    echo 'Changes pushed to Amazon EC2 PROD.'
    cd /home/ubuntu/app
    pip install --upgrade -r requirements.txt --no-cache-dir
    echo 'Python requirements upgraded'
    pkill -f gunicorn || true
    echo 'Killed old instance'
    echo 'Server is live'
  fi
done
