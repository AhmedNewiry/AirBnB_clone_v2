#!/usr/bin/env bash
#a Bash script that configures my servers for the deployment of web_static
sudo nginx -v
if ! [ $? -eq 0 ]
then
	sudo apt-get -y update
	sudo apt-get install -y nginx;
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello Deployment!" >> /data/web_static/releases/test/index.html
sudo ls -l /data/web_static/current
if [ $? -eq 0 ]
then
	sudo rm -rf /data/web_static/current
fi

sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name _;/a  location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart
