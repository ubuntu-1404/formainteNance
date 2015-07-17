class jre {
        file {
                "/home/ubuntu/jdk-8u45-linux-x64.tar.gz":
                source	=>	"puppet:///wodezoon/jdk/jdk-8u45-linux-x64.tar.gz",
                owner	=>	"root",
                group	=>	"root",
		ensure	=>	present,
                mode	=>	"777";} ~>
        file {
                "/etc/profile":
                source	=>	"puppet:///wodezoon/jdk/profile",
                owner	=>	"root",
                group	=>	"root",
                mode	=>	"665", } ~>
        file {
                "/home/ubuntu/jdk.sh":
                source	=>	"puppet:///wodezoon/jdk/jdk.sh",
                owner	=>	"root",
                group	=>	"root",
		ensure	=>	present,
                mode	=>	"777",} ~>
        exec {
                "/home/ubuntu/jdk.sh":
                cwd	=>	"/home/ubuntu",
		creates =>	"/home/ubuntu/javad",
		path	=>	"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin",}
}
