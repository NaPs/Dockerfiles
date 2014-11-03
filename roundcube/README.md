KiwiIRC is a moden web based client for IRC.

How to use this image
=====================

Quick testing
-------------

    docker run -P naps/roundcube --hosts you.imap.server

Usage
-----

This image use a launcher which will generate a Roundcube configuration file
based on parameter it receives. You can see all the available settings running
the image with the `--help` parameter:

    docker run -P --rm naps/roundcube --help

Each available parameter is mapped to a configuration item in `config.inc.php`
file.

The `--set` parameter allow you to define arbitrary options on config file:

    docker run -P -d naps/roundcube --hosts your.imap.server --plugins managesieve --set managesieve_host="'%h'"