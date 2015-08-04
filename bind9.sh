namehost=dns.wodezoon.com
apt-get install bind9
echo ${namehost}                            >   /etc/hostname
hostname ${namehost}
sed -i "/forwarders {/,+0a forwarders {"        /etc/bind/named.conf.options
sed -i "/0.0.0.0/,+0a 219.141.136.10"           /etc/bind/named.conf.options
sed -i "/219.141.136.10/,+0a };"                /etc/bind/named.conf.options

cp /etc/bind/named.conf.default-zones           /etc/bind/named.conf.default-zones.bak
#nametoip in default
echo "zone \"wodezoon.com\"  {"             >>  /etc/bind/named.conf.default-zones
echo "  type master;"                       >>  /etc/bind/named.conf.default-zones
echo "  file \"/etc/bind/nametoip\";"       >>  /etc/bind/named.conf.default-zones
echo "};"                                   >>  /etc/bind/named.conf.default-zones

#iptoname in default
echo " zone \"1.168.192.in-addr.arpa\"  {"  >>  /etc/bind/named.conf.default-zone
echo "  type master"                        >>  /etc/bind/named.conf.default-zone
echo "  file \"/etc/bind/iptoname\""        >>  /etc/bind/named.conf.default-zone
echo " };"                                  >>  /etc/bind/named.conf.default-zone

#update nametoip
cp -r /etc/bind/db.local /etc/bind/nametoip
sed -i "/localhost. root.localhost. (/,+0a @       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/nametoip
sed -i "/localhost. root.localhost. (/,+0d"                                                         /etc/bind/nametoip
sed -i "/NS/,+0d"                                                                                   /etc/bind/nametoip
sed -i "/127.0.0.1/,+0i @       IN      NS      wodezoon.com."                                      /etc/bind/nametoip
sed -i "/AAAA/,+0a manager IN      A       192.168.102.253"                                         /etc/bind/nametoip
sed -i "/AAAA/,+0d"                                                                                 /etc/bind/nametoip

#update iptoname
cp -r /etc/bind/db.127 /etc/bind/iptoname
sed -i "/localhost. root.localhost. (/,+0a @       IN      SOA     wodezoon.com. root.localhost. (" /etc/bind/iptoname
sed -i "/localhost. root.localhost. (/,+0d"                                                         /etc/bind/iptoname
sed -i "/NS/,+0d"                                                                                   /etc/bind/iptoname
sed -i "/PTR/,+0i @       IN      NS      wodezoon.com."                                            /etc/bind/iptoname

/etc/init.d/bind9 restart
