#class deployed ($verion) {
#        file {
#                "/home/ubuntu/hello.txt":
#                content =>      "$(date) and $version",}
#}
	$tmp=welcome
class deployed {
	$class_c = regsubst($ipaddress, "(.*)\..*", "\1.0")
	file {
		"/home/ubuntu/hello.txt":
		content =>	"$tmp\n$class_c\n$ipaddress\n",
	}
}
