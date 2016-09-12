# Contributing

## Virtual Environment

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

## Pre-Commit Hook

Depends on `flake8` which is in `config/requirements/dev.txt`. If you followed
the Virtual Environment instructions it will already be installed in your
environment.

```
flake8 --install-hook
```
