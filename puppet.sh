echo "please choose your setup style ==> 1-master  2-slaver"
read ttyp
wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
dpkg -i puppetlabs-release-trusty.deb
apt-get update

if [ ${ttyp} -eq 1 ]; then
apt-get install puppetmaster-passenger
puppet resource package puppetmaster ensure=latest

#echo "dns_alt_names = puppet,puppet.example.com,puppetmaster01,puppetmaster01.example.com" >> /etc/puppet/puppet.conf
#puppet master --verbose --no-daemonize#if here is only one master-server
#puppet cert generate <NAME> --dns_alt_names=<NAME1>,<NAME2>
#puppet agent --test --ca_server=<SERVERa>
#puppet cert list
#puppet cert --allow-dns-alt-names sign <NAMEl>
fi
if [ ${ttyp} -eq 2 ]; then
apt-get install puppet
puppet resource package puppet ensure=latest
fi

