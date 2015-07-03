host-name=dns.wodezoon.com
apt-get install bind9
hostname ${host-name}
#echo "forwarders{" >> /etc/bind/named.conf.options
#echo "	219.141.136.10" >> /etc/bind/named.conf.options
#echo "};" >> /etc/bind/named.conf.options

#nametoip in default
echo " zone \"elantech.com\"  {" >> /etc/bind/named.conf.default-zone
echo " 	type master" >> /etc/bind/named.conf.default-zone
echo " 	file \"/etc/bind/nametoip\"" >> /etc/bind/named.conf.default-zone
echo " };" >> /etc/bind/named.conf.default-zone

#iptoname in default
#echo " zone \"1.168.192.in-addr.arpa\"  {" >> /etc/bind/named.conf.default-zone
#echo "  type master" >> /etc/bind/named.conf.default-zone
#echo "  file \"/etc/bind/iptoname\"" >> /etc/bind/named.conf.default-zone
#echo " };" >> /etc/bind/named.conf.default-zone

#update nametoip
cp -r /etc/bind/db.local /etc/bind/nametoip

sed -i "/^@       IN      SOA     localhost. root.localhost. (/c@       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/nametoip
sed -i "/^@       IN      NS      localhost./c@       IN      NS      wodezoon.com." /etc/bind/nametoip
sed -i "/^@       IN      AAAA    ::1/cmaster       IN      A    192.168.1.101" /etc/bind/nametoip

#update iptoname
#cp -r /etc/bind/db.127 /etc/bind/iptoname
#
#sed -i "/^@       IN      SOA     localhost. root.localhost. (/c@       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/iptoname
#sed -i "/^@       IN      NS      localhost./c@       IN      NS      wodezoon.com." /etc/bind/iptoname
#sed -i "/^1.0.0   IN      PTR     localhost./c192.168.1.101   IN      PTR     master" /etc/bind/iptoname

/etc/init.d/bind9 restart
