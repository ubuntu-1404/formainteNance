class jmeter {
	include jre
        $jmeter="apache-jmeter-2.13"
	$modulejar="jmeter.tar.gz"
        Exec {
                path=>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"}
	file {
		"/home/ubuntu/$jmeter.zip":
                source  =>      "puppet:///wodezoon/jmeter/$jmeter.zip",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "755",}~>
	file {
		"/home/ubuntu/jmeter.sh":
                source  =>      "puppet:///wodezoon/jmeter/jmeter.sh",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "755",}~>
	file {
		"/home/ubuntu/jmeter.properties":
                source  =>      "puppet:///wodezoon/jmeter/jmeter.properties",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "755",}~>
	file {
                "/home/ubuntu/$modulejar":
                source  =>      "puppet:///wodezoon/jmeter/$modulejar",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "755",}~>
        exec {
		"jmeterup":
                command =>      "/home/ubuntu/jmeter.sh",
                user    =>      "root",
                cwd     =>      "/home/ubuntu",
                require =>      Class["jre"],}
}
