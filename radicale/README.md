Radicale is a very simple Caldav and Carddav server.

How to use this image
=====================

Quick testing
-------------

    docker run -P naps/radicale

Usage
-----

This image use a launcher which will generate a default configuration file you
can edit in the /radicale volume. I recommend to mount the /radicale volume on
a well-know location of the host filesystem (eg: "-v /mnt/storage/radicale:/radicale").

For instance, a full example usage could be:

    docker run -P -v /mnt/storage/radicale:/radicale naps/radicale

You can then edit configuration file in /mnt/storage/radicale/radicale.conf and
restart the container to apply changes.