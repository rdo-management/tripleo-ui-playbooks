# TripleO UI Playbooks


## Prerequisites

Install Pip and Ansible

```
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
