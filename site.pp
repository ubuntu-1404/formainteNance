node default {
	Exec
	{
		path=>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"
	}
	file 
	{
		"/home/ubuntu/hadoopmaster.sh":
		source=>"puppet:///wodezoon/hadoopmaster.sh",
		owner=>"ubuntu",
		group=>"ubuntu",
		mode=>"777",
	}
	file 
        {	
		"/home/ubuntu/hadoop.tar":
                source=>"puppet:///wodezoon/hadoop.tar",
                owner=>"ubuntu",
                group=>"ubuntu",
                mode=>"777",
        }
	exec
	{
		"/home/ubuntu/hadoopmaster.sh":
		cwd=>"/home/ubuntu",
		#path=>"/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin"
	}
}
#not exist then run "creates=>"
#only return 0 then run "onlyif=>[\"apt-get install git\",\"git --help\"]"
#another only "test `du /tmp/result.log i cut -f1` -gt 1024"#when file`s lenth over 1024 b then do next step
