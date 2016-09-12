# Contributing

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

## Development

### Pre-Commit Hook

Depends on `flake8` which is in `config/requirements/dev.txt`. If you followed
the Virtual Environment instructions it will already be installed in your
environment.

```
flake8 --install-hook
```

### Frontend Framework

DojoMaster uses Twitter Bootstrap-SASS (v3.2.0).
