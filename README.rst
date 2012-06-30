Python API for Notifout.com
===========================

What is Notifout.com
--------------------
Notifout.com is an online service which helps your application have nice-looking and reliable email notifications.

See `notifout.com <http://notifout.com/>`_ for details.


Installation
------------

::

    pip install notifout


Usage
-----


::

    from notifout import Notifout

    notifout = Notifout('ohsh6Iez3Nah0ahmohz2ge')
    notifout.send('signup', 'Dummy User <user@example.com>', {'first_name': 'Dummy'})