#node /^(hadoopmaster|hadoopslaver)\.wodezoon\.com$/ {
node /^hadoop\w+/ { 
	include hdsetup
}
node /^mongodb\w+$/ {
	include mongodb
}
