# TripleO UI Playbooks

Scripts and playbooks to setup the TripleO-UI on RHOS9.


## Environment (optional)

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

Once that's done login to the`instack` vm.


## Make sure the `stack` user exists or create it:

```
sudo useradd stack
echo stack | sudo passwd stack --stdin
echo "stack ALL=(root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/stack
sudo chmod 0440 /etc/sudoers.d/stack
su - stack
```

## Settings and Installation

Clone this repository and create a `hosts` file:

```
git clone https://github.com/flofuchs/tripleo-ui-playbooks.git
cd tripleo-ui-playbooks
cp hosts.sample hosts
```

Change your `hosts` file:

**`undercloud_service_host`:** This is the IP or hostname the GUI will use to connect to the undercloud. It needs to be accessible from outside the undercloud.

**Note:** In a virtual env, if you use a tunnel from the VM host machine to the undercloud vm, this needs to be set to the VM host's IP/hostname.

**`dib_install_type_puppet_modules`:** can be set to install puppet modules from source instead of using the packages. **Not recommended!**

Once the `hosts` file exists you can start the installation:

This will start the whole installation using the default values in `undercloud.conf`:

```
# Inside the repository directory:
./rhos9-complete.sh
```

If you'd like to make changes to `undercloud.conf` between the installation of python-tripleoclient and the undercloud, run these three commands in sequence:

```
# Inside the repository directory:
./rhos9-pre-undercloud-install.sh
# Make changes to undercloud.conf here...
openstack undercloud install
ansible-playbook -i hosts rhos9-post-install.yaml
```


## UI and API services

The setup will create three tmux sessions to run the TripleO-UI as well as the legacy TripleO and Validations APIs.

To attach to these sessions, use one of the following commands:

```
# TripleO UI:
tmux attach -t tripleo-ui

# TripleO API:
tmux attach -t tripleo-api

# Validations API:
tmux attach -t validations-api
```


## Image creation and upload

To create the images for the overcloud nodes, continue with the following commands:

```
source ~/stackrc
mkdir ~/images

sudo yum install -y rhosp-director-images rhosp-director-images-ipa
cp /usr/share/rhosp-director-images/overcloud-full-latest-9.0.tar ~/images/.
cp /usr/share/rhosp-director-images/ironic-python-agent-latest-9.0.tar ~/images/.
cd ~/images
for tarfile in *.tar; do tar -xf $tarfile; done
openstack overcloud image upload --image-path /home/stack/images/

#  Make sure all images have been uploaded:
openstack image list
```

## Node registration (optional)

The following steps can be done through the UI as well, so this step is optional.

```
# Register nodes.
openstack baremetal import --json ~/instackenv.json
openstack baremetal configure boot

# List nodes to see if registration has been successful.
ironic node-list

# Start introspection.
openstack baremetal introspection bulk start
```

