#!bin/bash

LOCAL_IP=$(grep '^local_ip' /home/stack/undercloud.conf | tail -1 | sed -E 's/^[^=]+=[ ]*([^\/]+)\/?.*$/\1/')
LOCAL_IP_DEFAULT=$(grep '^#local_ip' /home/stack/undercloud.conf | tail -1 | sed -E 's/^[^=]+=[ ]*([^\/]+)\/?.*$/\1/')

if [ -n "$LOCAL_IP" ]
then
    echo $LOCAL_IP
else
    echo $LOCAL_IP_DEFAULT
fi
