#!/usr/bin/env python

import argparse
import jinja2
import json
import os


TEMPLATE_FILENAME = '/kiwi/config.js.template'
OUTPUT_FILENAME = '/kiwi/config.js'


def mapping(data):
    key, sep, value = data.partition('=')
    if not sep:
        raise argparse.ArgumentTypeError('%r is not a key=value mapping' % data)
    return (key, value)


def json_filter(value):
    return json.dumps(value)


parser = argparse.ArgumentParser(description='KiwiIRC Launcher')

group_network = parser.add_argument_group('Network connectivity')
group_network.add_argument('--outgoing-address-ipv4', default='0.0.0.0', help='Network interface for outgoing connections (ipv4)')
group_network.add_argument('--outgoing-address-ipv6', default=None, help='Network interface for outgoing connections (ipv6)')
group_network.add_argument('--max-client-conns', type=int, default=5, help='Max connections per connection. 0 to disable')
group_network.add_argument('--max-server-conns', type=int, default=0, help='Max connections per IRC server. 0 to disable')

group_irc = parser.add_argument_group('IRC')
group_irc.add_argument('--default-encoding', default='utf8', help='Default encoding to be used by the server')
group_irc.add_argument('--default-gecos', default='Web IRC Client', help='Default GECOS (real name) for IRC connections.')
group_irc.add_argument('--ip-as-username', default=(), nargs='*', help='IP/Host of IRCDs requiring the clients IP via the username/ident')
group_irc.add_argument('--webirc-secret', type=mapping, default=(), nargs='*', help='WebIRC password by server (eg: irc.foo.org=bar)')

parser.add_argument('--reject-unauthorized-ssl-certificates', type=bool, default=False, help='Reject non-recognized IRC servers certificates')
parser.add_argument('--http-proxies', default=('127.0.0.1/32',), nargs='*', help='IP networks (cidr) of authorized reverse proxies')
parser.add_argument('--http-proxy-ip-header', default='x-forwarded-for', help='HTTP header that contains the real IP address of the client')
parser.add_argument('--available-themes', default=('relaxed', 'mini', 'cli', 'basic'), help='List of themes available for the user to choose from')

group_defaults = parser.add_argument_group('Client defaults')
group_defaults.add_argument('--default-quit-message', default='http://www.kiwiirc.com/ - A hand-crafted IRC client')
group_defaults.add_argument('--default-server', default='irc.kiwiirc.com')
group_defaults.add_argument('--default-port', type=int, default=6667)
group_defaults.add_argument('--default-enable-ssl', type=bool, default=False)
group_defaults.add_argument('--default-channel', default='#kiwiirc')
group_defaults.add_argument('--default-channel-key', default='')
group_defaults.add_argument('--default-nick', default='kiwi_?')
group_defaults.add_argument('--default-window-title', default='Kiwi IRC')

group_restrict = parser.add_argument_group('Client restrict')
group_restrict.add_argument('--restrict-server')
group_restrict.add_argument('--restrict-port', type=int)
group_restrict.add_argument('--restrict-ssl', type=bool)
group_restrict.add_argument('--restrict-channel')
group_restrict.add_argument('--restrict-channel-key')
group_restrict.add_argument('--restrict-password')
group_restrict.add_argument('--restrict-nick')


if __name__ == '__main__':
    args = parser.parse_args()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('/'))
    env.filters['json'] = json_filter
    template = env.get_template(TEMPLATE_FILENAME)
    environ = args.__dict__

    outgoing_address = {}
    if args.outgoing_address_ipv4:
        outgoing_address['IPv4'] = args.outgoing_address_ipv4
    if args.outgoing_address_ipv6:
        outgoing_address['IPv6'] = args.outgoing_address_ipv6
    environ['outgoing_address'] = outgoing_address

    environ['webirc_secret'] = dict(args.webirc_secret)
    
    with open(OUTPUT_FILENAME, 'w') as foutput:
        foutput.write(template.render(environ))

    os.execl('/kiwi/kiwi', 'kiwi', '-f')