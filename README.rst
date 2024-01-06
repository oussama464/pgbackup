pgbackup
===============

CLI for backup remote Postgresql database either locally or to S3.

Preparing the Devolopment
-------------------------
1. Ensure ``pip`` and ``pipenv`` are installed 
2. Clone Repo
3. ``cd`` into the repo 
4. Fetch dev dependencies ``make install`` 
5. activate virtualenv 

Usage
-----
Pass in a full database URL , the storage dirver , and the destination 

s3 Example w/ bucket name: 

::
    $ pgbackup postgresql://bob@example.com5432/db_one --driver s3 backups 

Local example w/ local path:

::
    $ pgbackup postgresql://bob@example.com5432/db_one --driver local /var/local/db_one/backups/dump.sql 



Running Tests
-------------

Run test locally using ``make`` if venv is active 

::
    $ make 

