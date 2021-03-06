#!/usr/bin/env python

import argparse
import sys

import liuproto.endpoint
import liuproto.link
import liuproto.storage


class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.format = '%d--%d'

    def __eq__(self, other):
        return self.start <= other <= self.end

    def __str__(self):
        return (self.format % (self.start, self.end)) + ' inclusive'

    def __repr__(self):
        return self.format % (self.start, self.end)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l', '--listen-address',
        type=str,
        help="The address upon which to listen.",
        default='0.0.0.0')

    parser.add_argument(
        '-p', '--port',
        type=int,
        help="The port upon which to listen.",
        default=8888,
        choices=[Range(1, 65535)])

    parser.add_argument(
        '-x', '--xml',
        help="Produce output in XML format.",
        action='store_true'
    )

    args = parser.parse_args()

    storage = liuproto.storage.Session('server')

    link = liuproto.link.NetworkServerLink(
        (args.listen_address, args.port),
        storage=storage)
    results = link.run_proto()

    link.close()

    if args.xml:
        print storage.xml
    else:
        for bit in results:
            if bit is None:
                continue

            if bit:
                sys.stdout.write('1')
            else:
                sys.stdout.write('0')

        sys.stdout.write("\n")
