# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  servers=[
    {
      :hostname => "server1",
      :box => "centos/7",
      :ip => "10.0.2.16",
      :ssh_port => "2200"
    },
    {
      :hostname => "server2",
      :box => "bento/ubuntu-18.04",
      :ip => "10.0.2.17",
      :ssh_port => "2201"
    },
    {
      :hostname => "server3",
      :box => "centos/7",
      :ip => "10.0.2.18",
      :ssh_port => "2200"
   }
  ]

  #define the loop 
  servers.each do |machine|
    config.vm.define machine[:hostname] do |node|
            node.vm.box = machine[:box]
            node.vm.hostname  = machine[:hostname]
            node.vm.network :private_network, ip: machine[:ip]
            node.vm.network "forwarded_port", guest: 22, host: machine[:ssh_port], id: "ssh" 
            node.vm.synced_folder "C:\\Users\\fwere\\vagworkstation\\data", "/home/vagrant/data"
            node.vm.provision "file", source: "C:\\Users\\fwere\\vagworkstation\\data\\copiedfile.txt", destination: "/home/vagrant/data/copiedfile.txt"

            node.vm.provider :virtualbox do |vb|
              vb.customize ["modifyvm", :id, "--memory", 1024]
              vb.customize ["modifyvm", :id, "--cpus", 2]
            end
    end 
  end
end 






# Vagrant on a single machine:

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.define :client do |devopsss_demo|
      devopsss_demo.vm.host_name = "devopsssforall"
      devopsss_demo.vm.network "private_network", ip:"192.168.200.100"
      devopsss_demo.vm.network "forwarded_port", guest: 22, host: 6000, auto_correct: true
      devopsss_demo.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correct: true
      devopsss_demo.vm.provision "shell", path: "install_jenkins.sh"
      devopsss_demo.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--memory", "2048"]
          vb.customize ["modifyvm", :id, "--cpus", "1"]
      end
  end
end
