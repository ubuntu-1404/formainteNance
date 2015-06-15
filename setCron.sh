cronpath=/home/ubuntu
backs=/home/ubuntu/bakup.sh
echo "* * * * * ${backs}" >> ${cronpath}/crontables
crontab -u root ${cronpath}/crontables
