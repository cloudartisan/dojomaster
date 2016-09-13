# Development Environment

## Vagrant

It's as simple as:

```
vagrant up
```

Then to connect:

```
vagrant ssh
```

And to start the web application:

```
drs
```

## Virtual Environment

Alternatively, to develop using a local virtual environment, do the following
setup and initialisation.

### Setup

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
pip install virtualenv
pip install virtualenvwrapper
pip install autoenv
```

### Initialisation

```
cd .
```

# Development

## Pre-Commit Hook

Depends on `flake8` which is in `config/requirements/dev.txt`. If you followed
the Virtual Environment instructions it will already be installed in your
environment.

```
flake8 --install-hook
```

## Frontend Framework

DojoMaster uses Twitter Bootstrap-SASS (v3.2.0).

## Handling E-mail

### Vagrant

If you're using the Vagrant development environment e-mail handling
is already sorted.

The development environment is already configured to communicate with
Maildump running on the Vagrant server. The SMTP settings are in
`config/settings/dev.py`.

Go to http://127.0.0.1:8888/ to see e-mail. 

### Virtual Environment

If you're using the virtualenv development environment.

#### Install Maildump

If you followed the Virtual Environment instructions it should
already be installed and running in your environment.

If not:

```
pip install maildump
maildump --smtp-ip 127.0.0.1 --smtp-port 2525 --http-ip 127.0.0.1 --http-port 8888
```

The development environment is already configured to communicate with
Maildump running on the Vagrant server. The SMTP settings are in
`config/settings/dev.py`.

Go to http://127.0.0.1:8888/ to see e-mail.
