# Nginx installation and configuration
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

class { 'nginx': }

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

exec { 'configure_redirect':
  command  => "sed -i '/^server {$/a \ location /redirect_me {return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;}' /etc/nginx/sites-available/default",
  path     => '/usr/bin:/bin',
  provider => 'shell',
  unless   => "grep -q 'location /redirect_me' /etc/nginx/sites-available/default",
  require  => File['/etc/nginx/sites-available/default'],
}
