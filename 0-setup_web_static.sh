#!/usr/bin/env bash
# sets up my web servers for the delpoyment of web_static
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
touch /data/web_static/releases/test/index.html
echo "simple content for a simple man" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
