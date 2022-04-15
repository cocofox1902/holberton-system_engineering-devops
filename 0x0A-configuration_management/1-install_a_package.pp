# Using Puppet, install puppet-lint
package {'puppet-lint':
  ensure   => 'present',
  provider => 'gem',
}
