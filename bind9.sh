namehost=dns.wodezoon.com
apt-get install bind9
hostname ${namehost}
#echo "forwarders{" >> /etc/bind/named.conf.options
#echo "	219.141.136.10" >> /etc/bind/named.conf.options
#echo "};" >> /etc/bind/named.conf.options

cp /etc/bind/named.conf.default-zones /etc/bind/named.conf.default-zones.bak
#nametoip in default
echo "zone \"wodezoon.com\"  {" >> /etc/bind/named.conf.default-zones
echo "	type master;" >> /etc/bind/named.conf.default-zones
echo "	file \"/etc/bind/nametoip\";" >> /etc/bind/named.conf.default-zones
echo "};" >> /etc/bind/named.conf.default-zones

#iptoname in default
#echo " zone \"1.168.192.in-addr.arpa\"  {" >> /etc/bind/named.conf.default-zone
#echo "  type master" >> /etc/bind/named.conf.default-zone
#echo "  file \"/etc/bind/iptoname\"" >> /etc/bind/named.conf.default-zone
#echo " };" >> /etc/bind/named.conf.default-zone

#update nametoip
cp -r /etc/bind/db.local /etc/bind/nametoip

sed -i "SOA/c@       IN      SOA     wodezoon.com. post.wodezoon. (" /etc/bind/nametoip
sed -i "NS/c@       IN      NS      wodezoon.com." /etc/bind/nametoip
sed -i "AAAA/cmaster       IN      A    192.168.1.101" /etc/bind/nametoip

#update iptoname
#cp -r /etc/bind/db.127 /etc/bind/iptoname
#
#sed -i "/^@       IN      SOA/c@       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/iptoname
#sed -i "/^@       IN      NS/c@       IN      NS      wodezoon.com." /etc/bind/iptoname
#sed -i "/^1.0.0   IN      PTR/c192.168.1.101   IN      PTR     master" /etc/bind/iptoname

/etc/init.d/bind9 restart
