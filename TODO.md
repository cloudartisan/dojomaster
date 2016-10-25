* In apps/base, override/replace the User model so that users do not
require a username, they only need an e-mail address and password

* In apps/club, extend the User model with one-to-one relationship
to an Owner profile model

* On registration/sign-up:

  ** Club Name
  ** Full Name / Your Name
  ** E-mail Address
  ** Password
  ** Phone

* On registration, create/populate the User, Owner, and Club records
and redirect to the dashboard

* Use Gravatar to automatically populate profile/avatar
