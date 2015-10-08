#!/bin/bash
hostip=(`ifconfig eth0 | grep "inet " | tr -sc '[0-9.]' ' '`) 
newHOST=${hostip[0]}
Oport=28080
deshost=192.168.11.1
Iport=8080
logpath="/home/sam/runNAT/${deshost}:${Iport}"
echo "newHOST=${hostip[0]} ! For reset Iptables-rules push 0,for add/del an iptables-rule push 1"
read itype
if [ ${itype} -eq 0 ]; then
  iptables -F
  iptables -t nat -F
  iptables -A INPUT -d ${newHOST} -p tcp --dport 20022 -j ACCEPT
  iptables -A INPUT -d ${newHOST} -j REJECT --reject-with icmp-host-prohibited
  iptables -t nat -A POSTROUTING -s 192.168.11.0/24 -j MASQUERADE
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 28080 -j DNAT --to-destination 192.168.11.1:8080
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 21422 -j DNAT --to-destination 192.168.11.14:22
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 21522 -j DNAT --to-destination 192.168.11.15:22
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 21722 -j DNAT --to-destination 192.168.11.17:22
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 21822 -j DNAT --to-destination 192.168.11.18:22
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 20080 -j DNAT --to-destination 192.168.11.17:80
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 20070 -j DNAT --to-destination 192.168.11.236:9200
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 20088 -j DNAT --to-destination 192.168.11.14:8088
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 20042 -j DNAT --to-destination 192.168.11.15:8042
  iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport 44444 -j DNAT --to-destination 192.168.11.15:44444
elif [ ${itype} -eq 1 ]; then
  if [ ! -f ${logpath} ] ; then
     echo "iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport ${Oport} -j DNAT --to-destination ${deshost}:${Iport}"
     iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport ${Oport} -j DNAT --to-destination ${deshost}:${Iport}
     echo "iptables -t nat -A PREROUTING -d ${newHOST} -p tcp --dport ${Oport} -j DNAT --to-destination ${deshost}:${Iport}" > ${logpath}
  else
     echo "iptables -t nat -D PREROUTING -d ${newHOST} -p tcp --dport ${Oport} -j DNAT --to-destination ${deshost}:${Iport}"
     iptables -t nat -D PREROUTING -d ${newHOST} -p tcp --dport ${Oport} -j DNAT --to-destination ${deshost}:${Iport}
     rm -rf ${logpath}
  fi
fi
