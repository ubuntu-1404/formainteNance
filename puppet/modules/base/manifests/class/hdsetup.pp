class hdsetup {
	include jre
	$tmp="/home/ubuntu/hadoop"
        Exec {
                path=>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"}
	exec {
		"mkdir -p $tmp/":
		creates	=>	"/$tmp",
		user	=>	"root",
		cwd	=>	"/home/ubuntu",} ~>
        file {
                "$tmp/hadoop-2.7.1.tar.gz":
                source	=>	"puppet:///wodezoon/hadoop/hadoop-2.7.1.tar.gz",
                owner	=>	"ubuntu",
		ensure	=>	present,
                mode	=>	"777",}~>
        file {
                "$tmp/hadoopsetup.sh":
                source	=>	"puppet:///wodezoon/hadoop/hadoopsetup.sh",
                owner	=>	"ubuntu",
		ensure	=>	present,
                mode	=>	"777",}~>
        file {
                "$tmp/slaves":
                source	=>	"puppet:///wodezoon/hadoop/slaves",
                owner	=>	"ubuntu",
		ensure	=>	present,
                mode	=>	"777",}~>
	exec {
		"hadoopsetup":
		command	=>	"/home/ubuntu/hadoop/hadoopsetup.sh",
		user	=>	"root",
		cwd	=>	"$tmp",
                require =>      Class["jre"],}
}
#not exist then run "creates=>"
#only return 0 then run "onlyif=>[\"apt-get install git\",\"git --help\"]"
#another only "test `du /tmp/result.log i cut -f1` -gt 1024"#when file`s lenth over 1024 b then do next step
#sed 's/hadoop01/hadoopmaster/g' /home/ubuntu/yarn-site.xml
