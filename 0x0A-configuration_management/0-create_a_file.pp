# create school file with correct conf
file { '/tmp/school':
    ensure  => present,
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
