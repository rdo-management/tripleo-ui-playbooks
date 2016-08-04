# TripleO UI Playbooks


## Prerequisites

Install latest puddle

```
sudo yum localinstall -y http://rhos-release.virt.bos.redhat.com/repos/rhos-release/rhos-release-latest.noarch.rpm
sudo rhos-release -P 9-director
```


Install Dependencies and Ansible

```
sudo yum install -y gcc
sudo yum install -y openssl-devel
sudo yum install -y python-devel
sudo yum install -y python-setuptools
sudo easy_install pip
sudo pip install ansible
```

## Settings

```
cp hosts.sample hosts
```

Add necessary settings to hosts file.


## Install UI on OSP9
```
# Set up prerequisites for undercloud installation.
ansible-playbook -i hosts rhos9-pre-install.yaml

# Continue with the undercloud install.
openstack undercloud install

# Install TripleO UI and make related changes.
ansible-playbook -i hosts rhos9-post-install.yaml
```
