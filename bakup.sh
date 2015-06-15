timep=`date -d today +"%Y-%m-%d_%H:%M:%S"`
backupath=/home/ubuntu/${timep}
tarFile=/home/ubuntu/startAgent.sh
mkdir ${backupath}
cp -R ${tarFile} ${backupath}
