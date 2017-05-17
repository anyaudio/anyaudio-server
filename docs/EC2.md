### Deploy on EC2

* Create an EC2 instance (ubuntu).
* ssh into it.
* apt-get update and upgrade

* Then run the following commands.

```sh
mkdir anyaudio.git
mkdir app
cd anyaudio.git
git init --bare
```

* Now set the post-receive git hook.

```sh
nano hooks/post-receive
```

* In nano, paste the contents of scripts/ec2_hook.sh

* Then chmod the script

```sh
chmod 775 hooks/post-receive
```

* Done.

```sh
git remote add ec2 ssh://ec2-user@<amazon-server-address>/home/ubuntu/anyaudio.git
git push ec2 master
```


### Running on EC2

* Install Python.

```sh
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh
```

* Install Postgres and build deps

```sh
sudo apt install build-essential postgresql libpq-dev
```

* Install ffmpeg

```sh
bash scripts/set_ffmpeg.sh
```

* Create postgres database

```sh
sudo -u postgres psql
```

```psql
create user aa with password 'aa';
create database anyaudio with owner aa;
```

* To access server on port 80, run the following command. Also add it to `/etc/rc.local` without the sudo. ([Credits](http://stackoverflow.com/questions/16573668/))

```
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000
```

* Now run the server manually. You can also `git push` to have server run trigerred.

```sh
python scripts/run_ec2.sh
```

### (Optional) Setting up nginx

* Install nginx

```
sudo apt-get install nginx
sudo service nginx start
```

* Create conf script.

```sh
sudo nano /etc/nginx/conf.d/anyaudio.conf
# ^^ copy anyaudio.site into it
# doesnt work: sudo nano /etc/init/anyaudio.conf
```

* Test and restart nginx

```sh
sudo nginx -t
sudo service nginx restart
```


### Setting custom domain

* Create an elastic IP and associate it with EC2 instance. http://andnovar.tech/2014/05/03/pointing-godaddy-domain-aws-ec2-instance/
* Now the EC2 url has changed so be sure to make the changes where necessary.
* Change A record in your domain DNS tool to the elastic IP.
* If you are using Cloudflare, change www to point to the EC2 domain and change A record to IP.


#### Credits

* https://gist.github.com/aviaryan/393fbb7d96b133d6dfbd430a21c5e73b
* http://stackoverflow.com/questions/4632749/how-to-push-to-git-on-ec2
