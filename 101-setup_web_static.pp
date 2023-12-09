#a puppet scritp that sets up your web servers for the deployment of web_static

$dir_list = ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test']
$nginx_conf = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location /hbnb_static {
                alias /data/web_static/current/;
        }
        add_header X-Served-By \$hostname;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /not_found.html;
        location /not_found.html {
                internal;
        }
        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}
"
exec {'update repo resources':
    command => 'sudo apt-get -y update',
    path => '/usr/bin/:/usr/local/bin/:/bin/'
}->
package { 'nginx':
    ensure => 'present',
    provider => 'apt'
}->
file { $dir_list:
    ensure => 'directory',
    owner => 'ubuntu',
    group => 'ubuntu',
}->

file { '/data/web_static/shared':
    ensure => 'directory',
    owner => 'ubuntu',
    group => 'ubuntu',
}->

file {'/data/web_static/releases/test/index.html':
    ensure => 'present',
    content => 'Hello Deployment!\n',
    owner => 'ubuntu',
    group => 'ubuntu',
}->
file {'/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test'
}->

file { '/etc/nginx/sites-available/default':
    ensure => 'present',
    content => $nginx_conf
}->

exec {'restart nginx':
    command => 'nginx restart',
    path => '/etc/init.d/'
}
