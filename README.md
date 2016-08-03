# TripleO UI Playbooks


## Prerequisites

Install Dependencies and Ansible

```
sudo yum install -y gcc
sudo yum install -y openssl-devel
sudo yum install -y python-devel
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

# Make some UI-related changes to the freshly installed undercloud.
ansible-playbook -i hosts rhos9-pre-install.yaml
```
