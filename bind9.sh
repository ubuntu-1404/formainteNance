namehost=dns.wodezoon.com
apt-get install bind9
hostname ${namehost}
sed -i "/forwarders {/,+0a forwarders {" /home/ubuntu/demo.txt
sed -i "/0.0.0.0/,+0a 219.141.136.10" /home/ubuntu/demo.txt
sed -i "/219.141.136.10/,+0a };" /home/ubuntu/demo.txt

cp /etc/bind/named.conf.default-zones /etc/bind/named.conf.default-zones.bak
#nametoip in default
echo "zone \"wodezoon.com\"  {" >> /etc/bind/named.conf.default-zones
echo "  type master;" >> /etc/bind/named.conf.default-zones
echo "  file \"/etc/bind/nametoip\";" >> /etc/bind/named.conf.default-zones
echo "};" >> /etc/bind/named.conf.default-zones

#iptoname in default
#echo " zone \"1.168.192.in-addr.arpa\"  {" >> /etc/bind/named.conf.default-zone
#echo "  type master" >> /etc/bind/named.conf.default-zone
#echo "  file \"/etc/bind/iptoname\"" >> /etc/bind/named.conf.default-zone
#echo " };" >> /etc/bind/named.conf.default-zone

#update nametoip
cp -r /etc/bind/db.local /etc/bind/nametoip
sed -i "/localhost. root.localhost. (/,+0a @       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/nametoip
sed -i "/localhost. root.localhost. (/,+0d" /etc/bind/nametoip
sed -i "/NS/,+0d" /etc/bind/nametoip
sed -i "/127.0.0.1/,+0i @       IN      NS      wodezoon.com." /etc/bind/nametoip
sed -i "/AAAA/,+0a manager IN      A       192.168.102.253" /etc/bind/nametoip
sed -i "/AAAA/,+0d" /etc/bind/nametoip

#update iptoname
#cp -r /etc/bind/db.127 /etc/bind/iptoname
#
#sed -i "/^@       IN      SOA/c@       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/iptoname
#sed -i "/^@       IN      NS/c@       IN      NS      wodezoon.com." /etc/bind/iptoname
#sed -i "/^1.0.0   IN      PTR/c192.168.1.101   IN      PTR     master" /etc/bind/iptoname

/etc/init.d/bind9 restart
