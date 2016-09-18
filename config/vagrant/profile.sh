#!/bin/sh
set -x

cat >> /home/vagrant/.bashrc << EOF

alias drs='/vagrant/manage.py runserver 0.0.0.0:8000'
alias d='/vagrant/manage.py'
complete -cf sudo

cd /vagrant

echo ""
echo "Commands:"
echo "drs - Start Django's runserver"
echo "d   - Alias to Django's manage.py"
echo ""
EOF

