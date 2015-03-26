#!/usr/bin/env python

import random
import string
import argparse
import os
import shutil


DEFAULT_CONFIGURATION = '/default_radicale_config.conf'
CONFIGURATION_FILENAME = 'radicale.conf'
CONFIGURATION_DIRECTORY = '/radicale'


parser = argparse.ArgumentParser(description='Radicale Launcher')
parser.add_argument('--config', default=CONFIGURATION_FILENAME, help='Specify an alternative name for the configuration file.')
parser.add_argument('--debug', '-d', action='store_true', default=False)


if __name__ == '__main__':
    args = parser.parse_args()

    configuration_fullname = os.path.join(CONFIGURATION_DIRECTORY, args.config)

    if not os.path.exists(configuration_fullname):
        shutil.copyfile(DEFAULT_CONFIGURATION, configuration_fullname)

    cmdline = ['/usr/local/bin/radicale', 'radicale', '--config', configuration_fullname, '--foreground']

    if args.debug:
        cmdline += ['--debug']

    os.execl(*cmdline)