# cofigure ssh client using ppupet
file_line { 'Turn off Password Auth':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
}

file_line { 'Use school rsa':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
}
