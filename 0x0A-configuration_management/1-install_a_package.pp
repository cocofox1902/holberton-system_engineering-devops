# Using Puppet, install puppet-lint
exec {'puppet-lint':
  path => '/usr/bin',
}
