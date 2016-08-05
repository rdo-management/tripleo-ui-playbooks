#!/bin/bash

# Set up prerequisites for undercloud installation.
ansible-playbook -i hosts rhos9-pre-install.yaml

# Continue with the undercloud install.
openstack undercloud install

# Install TripleO UI and make related changes.
ansible-playbook -i hosts rhos9-post-install.yaml
