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


## Run a playbook
ansible-playbook -i hosts rhos9.yaml
