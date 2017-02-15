### Deploy on EC2

* Create an EC2 instance.
* ssh into it.

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

* Now run the server manually. You can also `git push` to have server run trigerred.

```sh
python scripts/run_ec2.sh
```


#### Credits

* https://gist.github.com/aviaryan/393fbb7d96b133d6dfbd430a21c5e73b
* http://stackoverflow.com/questions/4632749/how-to-push-to-git-on-ec2
