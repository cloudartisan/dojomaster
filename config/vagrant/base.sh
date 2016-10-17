#!/bin/sh
set -x

cd /vagrant

# Install APT packages
sudo aptitude -y update
sudo aptitude -y upgrade
sudo aptitude install -y build-essential libssl-dev libffi-dev
sudo aptitude install -y git python-pip python-all-dev libmysqlclient-dev htop
# Required by Pillow
sudo aptitude install -y libjpeg-dev zlib1g-dev
# Required by GEvent
sudo aptitude install -y libevent-dev
sudo pip install -r config/requirements/dev.txt

# Setup the local settings file
if [ ! -f /vagrant/config/settings/local.py ]; then
    python /vagrant/config/create_local_settings_file.py
fi

# Setup the DB
/vagrant/manage.py migrate

# Remove files that aren't needed anymore
make clean

# Done
echo '
Done!

Now SSH to your vagrant box with `vagrant ssh` and start the
Django development server with the bash alias `drs`. 

Go to http://127.0.0.1:8000/ in your browser to view the site.
'
