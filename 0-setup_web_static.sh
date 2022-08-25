#!/usr/bin/env bash
# comment for the checker

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '$ d' /etc/nginx/sites-available/default
echo "location /hbnb_static {
alias /data/web_static/current/;
error_page 404 /custom_404.html;
try_files \$uri \$uri/ =404;
}
}" >> /etc/nginx/sites-available/default
sudo service nginx restart
