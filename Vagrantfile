# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 2525, host: 2525
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.ssh.forward_agent = true
  config.vm.provision "shell", path: "config/vagrant/base.sh"
  config.vm.provision "shell", path: "config/vagrant/profile.sh"

  config.vm.provider "virtualbox" do |v|
    v.memory = 256
  end

end
