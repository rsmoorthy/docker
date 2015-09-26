#!/bin/bash
if [ $APACHE_USER_UID != 0 ];then
  usermod -u $APACHE_USER_UID $APACHE_RUN_USER
fi
/usr/sbin/apache2 -DFOREGROUND
