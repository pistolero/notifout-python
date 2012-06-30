Python API for Notifout.com
===========================

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