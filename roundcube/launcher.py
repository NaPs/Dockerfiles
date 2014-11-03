#!/usr/bin/env python

import random
import string
import argparse
import jinja2
import os


TEMPLATE_FILENAME = '/config.inc.php.tmpl'
OUTPUT_FILENAME = '/var/www/config/config.inc.php'


def mapping(data):
    key, sep, value = data.partition('=')
    if not sep:
        raise argparse.ArgumentTypeError('%r is not a key=value mapping' % data)
    return (key, value)


parser = argparse.ArgumentParser(description='Roundcube Launcher')

parser.add_argument('--hosts', default=[], nargs='*', help='List of imap servers on which to connect.')
parser.add_argument('--product-name', default='Roundcube Webmail')
parser.add_argument('--plugins', default=['archive', 'zipdownload'], nargs='*', help='List of plugins to enable.')
parser.add_argument('--set', type=mapping, default=[], nargs='*', help='Arbitrary define an option in config file.')

if __name__ == '__main__':
    args = parser.parse_args()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('/'))
    template = env.get_template(TEMPLATE_FILENAME)
    options = dict(args.set)
    
    options['default_host'] = 'array(%s)' % ', '.join(repr(x) for x in args.hosts)
    options['product_name'] = repr(args.product_name)
    options['plugins'] = 'array(%s)' % ', '.join(repr(x) for x in args.plugins)
    options['des_key'] = "'%s'" % ''.join(random.choice(string.letters + string.digits) for _ in xrange(24))

    with open(OUTPUT_FILENAME, 'w') as foutput:
        foutput.write(template.render({'options': options}))

    os.execl('/usr/sbin/apache2ctl', 'apache2ctl', '-D', 'FOREGROUND')