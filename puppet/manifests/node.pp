#node /^(hadoopmaster|hadoopslaver)\.wodezoon\.com$/ {
node /^hadoop\w+/ { 
	include hdsetup
}
node /^mongodb\w+$/ {
	include mongodb
}
node /^(genarate\d|gili)\.wodezoon\.com$/ {
	include jmeter
}
node /^jmeter\w+/ {
	include jmeter
}
