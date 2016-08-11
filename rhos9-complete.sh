#!/bin/bash

# Exit on error
set -e

/bin/bash rhos9-pre-undercloud-install.sh

# Continue with the undercloud install.
openstack undercloud install

# Install TripleO UI and make related changes.
ansible-playbook -i hosts rhos9-post-install.yaml
