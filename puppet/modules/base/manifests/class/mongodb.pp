class mongodb {
	$mongovsion="mongodb-linux-x86_64-ubuntu1404-3.0.3"
	Exec {
                path=>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"}
	file {
                "/home/ubuntu/$mongovsion.tar":
                source  =>      "puppet:///wodezoon/mongodb/$mongovsion.tar",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "777",}
	file {
                "/home/ubuntu/mongodb.sh":
                source  =>      "puppet:///wodezoon/mongodb/mongodb.sh",
                owner   =>      "root",
                group   =>      "root",
                mode    =>      "777",}
	exec {
		"/home/ubuntu/mongodb.sh":
		cwd	=>	"/home/ubuntu",}
}
