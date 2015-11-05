#!/bin/bash
timep=`date -d today +"%Y-%m-%d_%H:%M:%S"`
goal=("*.xml" "*.conf")
goalpath="/root/aback"
backdir="/backup/${timep}"

#create backup dirary
if [ ! -d ${backdir} ] ; then
 mkdir ${backdir}
fi
#find goals and backup them (include compare oldbackups and new one)
for goals in "${goal}" ; do
 dirs=(`find ${backdir} -name "${goals}"`)
 for i in "${dirs[@]}";do
  if [ ! -f ${goalpath}/${i##*/} ] ; then
   cp ${i} ${goalpath}/${i##*/}
  else
   type=(`diff -q ${goalpath}/${i##*/} ${i}`)
   if [ ${type[4]} =  "differ" ] ;then
    mv ${goalpath}/${i##*/} ${goalpath}/${i##*/}.bak
    cp ${i} ${goalpath}/${i##*/}
   fi
  fi
 done
done

#backup entired folder to tar
#tar -zcvf /backup/${timep}/backup.tar.gz /mail/linkgent.com/
#timed=`date -d today +"%Y-%m-%d_%H:%M:%S"`
#echo "startTime=${timep} and endTime=${timed}" >> /backup/${timep}/last
