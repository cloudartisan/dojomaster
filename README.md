# Development Environment

There are 2 primary ways to setup the development environment: using
Vagrant or using virtualenv.

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

Install the pre-requisites:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
pip install virtualenv
pip install virtualenvwrapper
pip install autoenv
```

Add something like the following to `$HOME/.bash_profile`:

```
if [ ! -z "$(which virtualenvwrapper.sh)" ]
then
  export WORKON_HOME=$HOME/.virtualenvs
  mkdir -p $WORKON_HOME
  . `which virtualenvwrapper.sh`
fi

if [ ! -z "$(which activate.sh)" ]
then
  . `which activate.sh`
fi
```

Then reload:

```
. $HOME/.bash_profile
```

That will add `autoenv` support to your shell.

Next, create a `.env` file inside the project root that contains:

```
# Only initialise the virtual environment upon cd'ing to the top level
BASE_PATH=`dirname "${BASH_SOURCE}"`
PWD=`pwd`
if [[ "${BASE_PATH}" == "${PWD}" ]]
then
  mkvirtualenv dojomaster
  workon dojomaster
  pip install -r config/requirements/dev.txt
fi
```

### Use

Now, whenever you cd to the top-level of the dojomaster project you
should have your virtual environment initialised. E.g.:

```
neuromancer:~ $ cd git/cloudartisan/dojomaster/
New python executable in /Users/david/.virtualenvs/dojomaster/bin/python2.7
Not overwriting existing python script /Users/david/.virtualenvs/dojomaster/bin/python (you must use /Users/david/.virtualenvs/dojomaster/bin/python2.7)
Installing setuptools, pip, wheel...done.
[...]
(dojomaster) neuromancer:~/git/cloudartisan/dojomaster (master)$
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
already be installed.

If not:

```
pip install maildump
```

To run, simply:

```
maildump --smtp-ip 127.0.0.1 --smtp-port 2525 --http-ip 127.0.0.1 --http-port 8888
```

The development environment is already configured to communicate with
Maildump running on the Vagrant server. The SMTP settings are in
`config/settings/dev.py`.

Go to http://127.0.0.1:8888/ to see e-mail.

## Database

The development database is SQLite in `config/db/db.sqlite3`.

### Seed

Load the `initial_data` fixture.

```
python manage.py loaddata initial_data
```
