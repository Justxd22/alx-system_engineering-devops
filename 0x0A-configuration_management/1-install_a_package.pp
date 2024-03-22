# install flask ver 2.1.0
Package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}

Package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
