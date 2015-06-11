#!/usr/bin/env python

import argparse
import os
import shutil

DEFAULT_CONFIGURATION = '/default_nginx.conf'
CONFIGURATION_FILENAME = 'nginx.conf'
CONFIGURATION_DIRECTORY = '/nginx'
HARD_CONF = ['daemon off', 'user www-data']

parser = argparse.ArgumentParser(description='Web static Launcher')
parser.add_argument('--config', default=CONFIGURATION_FILENAME, help='Specify an alternative name for the configuration file.')


if __name__ == '__main__':
    args = parser.parse_args()

    configuration_fullname = os.path.join(CONFIGURATION_DIRECTORY, args.config)

    if not os.path.exists(configuration_fullname):
        shutil.copyfile(DEFAULT_CONFIGURATION, configuration_fullname)

    try:
        os.mkdir(os.path.join(CONFIGURATION_DIRECTORY, 'static'))
    except:
        pass

    os.execl('/usr/sbin/nginx', 'nginx', '-c', configuration_fullname, '-g', ';'.join(HARD_CONF) + ';')
