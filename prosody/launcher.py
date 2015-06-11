#!/usr/bin/env python

import argparse
import os
import shutil


DEFAULT_CONFIGURATION = '/default_prosody.cfg.lua'
CONFIGURATION_FILENAME = 'prosody.cfg.lua'
CONFIGURATION_DIRECTORY = '/prosody'


parser = argparse.ArgumentParser(description='Prosody Launcher')
parser.add_argument('--config', default=CONFIGURATION_FILENAME, help='Specify an alternative name for the configuration file.')


if __name__ == '__main__':
    args = parser.parse_args()

    configuration_fullname = os.path.join(CONFIGURATION_DIRECTORY, args.config)

    if not os.path.exists(configuration_fullname):
        shutil.copyfile(DEFAULT_CONFIGURATION, configuration_fullname)

    cmdline = ['/usr/bin/prosody', 'prosody', '--config', configuration_fullname]

    os.execl(*cmdline)
