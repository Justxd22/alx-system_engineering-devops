# cofigure ssh client using ppupet
include stdlib
file_line { 'Turn off Password Auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    replace => true,
}

file_line { 'Use school rsa':
    ensure  => present,
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    replace => true,
}
