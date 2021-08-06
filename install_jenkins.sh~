#!/bin/bash

# OpenJDK 8 package:

sudo yum install java-1.8.0-openjdk-devel -y 
sleep 5

echo "# enable the Jenkins repository ---->"
sudo curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo

echo "# add the repository ---->"
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

echo "#install jenkins "
sudo yum install jenkins -y 
sudo yum -y update 

echo " Restarting services ---->"
sudo systemctl start jenkins
sleep 5
echo " Enable Jenkins ---->"
sudo systemctl enable jenkins
sleep 5
sudo systemctl status jenkins
sleep 5
echo "Enablisng firewall "
sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp

sudo firewall-cmd --reload
