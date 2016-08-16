# FEATURES

## Dependencies

- Install tox, tmux, gcc, openssl-devel, python-devel, pip, ansible
- Update virtualenv

## Mistral

- Install missing Mistral packages
- Patch mistral puppet modules, so Mistral doesn't run under httpd

## Zaqar

- Patch instack_undercloud.undercloud module: Add missing option.

## Undercloud installation

- Install python-tripleoclient
- Enable mistral and zaqar in undercloud.conf

## tripleo-ui

- Clone rdo-director-ui-production repo
- Set API/websocket URLs in app.conf
- Add JS/CSS assets based on OSP9-specific patches
- Creates a tmux session that runs the UI server

## CORS Settings

- Add settings and restart:
    - Keystone
    - Ironic
    - Heat
    - Mistral
    - Swift

## Validations API

- Clone repo from ansible1.9 branch
- Install requirements
- Configure/restart iptables to open port 5001 if necessary 
- Creates a tmux session that runs the Validations server

## tripleo-common

- Clone tripleo-common repo
- Patch tripleo_common.utils.tarball to remove unneeded files from plan creation
- Remove existing tripleo-common installation and install from repo
- Restart systemctl restart openstack-mistral-executor
- Restart systemctl restart openstack-mistral-engine
- Populate mistral db
- Create or update plan_management workflow
- Create or update baremetal workflow
- Create or update deployment workflow
- Create default plan if there is none

## rhci/tripleo-api
- Install libffi-devel
- Install openssl-devel
- Clone rhci-tripleo-api repository
- Create and update tripleo.conf:
    - CORS settings
    - Set keystone credentials (from `~/undercloud-passwords.conf`)
- Configure/restart iptables to open port 8585 if necessary 
- Creates a tmux session that runs the Validations server
- Patch tripleo_api.utils.capabilities module to detect capabilities map file based on path instead of metadata

## Glance endpoint

- Change Glance's name in serviceCatalog from 'Image Service' to 'glance'

