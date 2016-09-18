#!/bin/sh
set -x

cd /vagrant

# INSTALL APT PACKAGES
sudo aptitude -y update
sudo aptitude -y upgrade
sudo aptitude install -y git python-pip python-dev libmysqlclient-dev htop
sudo pip install -r config/requirements/dev.txt

# SETUP THE LOCAL SETTINGS FILE
if [ ! -f /vagrant/config/settings/local.py ]; then
    python /vagrant/config/create_local_settings_file.py
fi

# SETUP THE DB
/vagrant/manage.py migrate

# START DEVELOPMENT MAILSERVER
maildump --smtp-ip 0.0.0.0 --smtp-port 2525 --http-ip 0.0.0.0 --http-port 8888 &

# REMOVE FILES THAT AREN'T NEEDED ANYMORE
make clean

# DONE
echo '
Done!

Now ssh to your vagrant box with `vagrant ssh` and then start the Django
development sever with the bash alias `drs`. Then go to http://127.0.0.1:8000/
in your browser to view your new base site!

The development mail server is available at 127.0.0.1:2525 and its web UI is
available at http://127.0.0.1:8888/.
'
