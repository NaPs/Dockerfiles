KiwiIRC is a moden web based client for IRC.

How to use this image
=====================

Quick testing
-------------

    docker run -P naps/kiwiirc

Usage
-----

This image use a launcher which will generate a KiwiIRC configuration file based
on parameter it receives. You can see all the available settings running the
image with the `--help` parameter:

    docker run -P --rm naps/kiwiirc --help

Each available parameter is mapped to a configuration item in `config.js` file.

If you plan to host a kiwiirc container behind a reverse proxy, you will have to
set the `--http-proxies` parameter with the IP of the reverse proxy. This page
of the official documentation of KiwiIRC can help you to setup the reverse
proxy: https://kiwiirc.com/docs/installing/proxies. Here is an example:

    docker run -P -d naps/kiwiirc --http-proxies 127.0.0.1/32 192.168.0.10/32

To finish, here is an example of a KiwiIRC instance with defaults to join the
docker channel:

    docker run -P -d naps/kiwiirc --default-server irc.freenode.org \
           --default-channel "#docker" --default-quit-message "Docker rocks!"