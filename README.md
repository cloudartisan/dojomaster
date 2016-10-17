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
  mkvirtualenv runmydojo
  workon runmydojo
  pip install -r config/requirements/dev.txt
fi
```

If you have any problems installing `pillow` or other packages it might be
because the XCode command-line tools are not installed. To install the XCode
command-line tools:

```
xcode-select --install
```

It might also be that JPEG librares are missing. To install them:

```
brew install jpeg
```

### Use

Now, whenever you cd to the top-level of the runmydojo project you
should have your virtual environment initialised. E.g.:

```
neuromancer:~ $ cd git/cloudartisan/runmydojo/
New python executable in /Users/david/.virtualenvs/runmydojo/bin/python2.7
Not overwriting existing python script /Users/david/.virtualenvs/runmydojo/bin/python (you must use /Users/david/.virtualenvs/runmydojo/bin/python2.7)
Installing setuptools, pip, wheel...done.
[...]
(runmydojo) neuromancer:~/git/cloudartisan/runmydojo (master)$
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

Twitter Bootstrap-SASS (v3.2.0).

## Database

The development database is SQLite in `config/db/db.sqlite3`.

### Seed

Load the `initial_data` fixture.

```
python manage.py loaddata initial_data
```
