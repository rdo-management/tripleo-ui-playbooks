#!/bin/bash

# Exit on error
set -e

# Install the latest puddle
sudo yum localinstall -y http://rhos-release.virt.bos.redhat.com/repos/rhos-release/rhos-release-latest.noarch.rpm

# Install mistral packages from rhos10
sudo rhos-release 10 -p 2016-09-07.6
sudo yum install -y openstack-mistral-all
sudo yum install -y openstack-mistral-api
sudo yum install -y openstack-mistral-engine
sudo yum install -y openstack-mistral-executor

# Switch pack to 9-director and remove rhos10 repo
sudo rm /etc/yum.repos.d/rhos-release-10.repo
sudo yum clean all
sudo rhos-release -P 9-director

# Install dependencies for ansible installation
sudo yum install -y gcc
sudo yum install -y openssl-devel
sudo yum install -y python-devel
sudo easy_install pip
sudo pip install ansible

# Set up prerequisites for undercloud installation.
ansible-playbook -i hosts rhos9-pre-install.yaml

