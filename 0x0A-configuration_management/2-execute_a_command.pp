# kill a kiddie :)
exec { 'kill_a_proccess_pid':
    command => 'pkill killmenow',
    path    => ['/usr/bin', '/bin'],
}
