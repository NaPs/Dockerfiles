#!/usr/bin/env python

import argparse
import os



parser = argparse.ArgumentParser(description='Apache2-PHP Launcher')

if __name__ == '__main__':
    args = parser.parse_args()

    os.execl('/usr/sbin/apache2ctl', 'apache2ctl', '-D', 'FOREGROUND')
