# 2

exec {'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => present,
  name    => 'nginx',
  require => Exec['apt-get-update'],
}

file_line { 'header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => running,
  require    => Package['nginx'],
}
