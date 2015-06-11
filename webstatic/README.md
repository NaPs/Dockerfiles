Static HTML pages hosting.

How to use this image
=====================

Quick testing
-------------

    docker run -P naps/webstatic

Usage
-----

This image use a launcher which will generate a default configuration file you
can edit in the /nginx volume. I recommend to mount the /nginx volume on
a well-know location of the host filesystem (eg: "-v /mnt/storage/nginx:/nginx").

For instance, a full example usage could be:

    docker run -P -v /mnt/storage/nginx:/nginx naps/webstatic

You can then edit configuration file in /mnt/storage/nginx/nginx.conf
and restart the container to apply changes.