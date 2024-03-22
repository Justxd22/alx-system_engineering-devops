# install flask ver 2.1.0
exec { 'install_flask_ver_2.1.0':
    command => 'pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/usr/local/bin'],
    unless  => 'pip3 show requests | grep "Version: 2.1.0"',
}
