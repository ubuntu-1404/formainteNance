timep=`date -d today +"%Y-%m-%d_%H:%M:%S"`
mkdir /backup/${timep}
tar -zcvf /backup/${timep}/backup.tar.gz /mail/linkgent.com/
timed=`date -d today +"%Y-%m-%d_%H:%M:%S"`
echo "startTime=${timep} and endTime=${timed}" >> /backup/${timep}/last
