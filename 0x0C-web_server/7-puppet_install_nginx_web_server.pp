# Nginx installation and configuration
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/redirect_me':
    ensure  => file,
    content => "
      server {
        listen 80;
        server_name your_domain.com; # Replace with your domain name

        location /redirect_me {
          rewrite ^/redirect_me(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4$1 permanent; # Replace example.com with your desired redirect URL
        }

        error_page 404 /404.html;
        location = /404.html {
          root /var/www/html;
          internal;
        }

        root /var/www/html;
        index index.html;
      }
    ",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect_me':
    ensure  => link,
    target  => '/etc/nginx/sites-available/redirect_me',
    require => File['/etc/nginx/sites-available/redirect_me'],
    notify  => Service['nginx'],
  }

}

class { 'nginx': }

