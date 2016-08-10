# TripleO UI Playbooks


## Prerequisites

### Virtual Env

If you are using a virtual environment, use the following steps to create the virtual machines:

```
# Create a stack user

sudo useradd stack
echo stack | sudo passwd stack --stdin
echo "stack ALL=(root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/stack
sudo chmod 0440 /etc/sudoers.d/stack
su - stack

# Enable the latest puddle and install

sudo yum localinstall -y http://rhos-release.virt.bos.redhat.com/repos/rhos-release/rhos-release-latest.noarch.rpm
sudo rhos-release -P 9-director
sudo yum update -y
sudo yum install -y instack-undercloud wget
wget http://download.eng.brq.redhat.com/brewroot/packages/rhel-guest-image/7.2/20160302.0/images/rhel-guest-image-7.2-20160302.0.x86_64.qcow2
export DIB_LOCAL_IMAGE=rhel-guest-image-7.2-20160302.0.x86_64.qcow2
export  DIB_YUM_REPO_CONF="/etc/yum.repos.d/rhos-release-9.repo  /etc/yum.repos.d/rhos-release-rhel-7.2.repo  /etc/yum.repos.d/rhos-release-9-director.repo"
export USE_DELOREAN_TRUNK=0
export RHOS=1
export UNDERCLOUD_NODE_CPU=4
export UNDERCLOUD_NODE_MEM=16384

# Set up the VMs
instack-virt-setup
```

Once that's done login to the `instack` vm.


### Make sure the `stack` user exists or create it:

```
sudo useradd stack
echo stack | sudo passwd stack --stdin
echo "stack ALL=(root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/stack
sudo chmod 0440 /etc/sudoers.d/stack
su - stack
```


### Install latest puddle

```
sudo yum localinstall -y http://rhos-release.virt.bos.redhat.com/repos/rhos-release/rhos-release-latest.noarch.rpm
sudo rhos-release -P 9-director
```


### Install Dependencies and Ansible

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

The 3 steps above can be run with one `./rhos9-complete.sh` call.
