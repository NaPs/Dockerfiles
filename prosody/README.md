Prosody is a modern XMPP communication server. It aims to be easy to set up and configure, and efficient with system resources. 

How to use this image
=====================

Quick testing
-------------

    docker run -P naps/prosody

Usage
-----

This image use a launcher which will generate a default configuration file you
can edit in the /prosody volume. I recommend to mount the /prosody volume on
a well-know location of the host filesystem (eg: "-v /mnt/storage/prosody:/prosody").

For instance, a full example usage could be:

    docker run -P -v /mnt/storage/prosody:/prosody naps/prosody

You can then edit configuration file in /mnt/storage/prosody/prosody.cfg.lua 
and restart the container to apply changes.