"""

Dump
====

Helps dumping Waffle.io cards information.

Reasoning
---------

Motivation behind this includes the ability to test a high level code
without spending too much time on planning it. We should see a general
algorithm for going through Waffle.io done cards, in the order they
appear in the dashboard.

"""

import sys

from .tools import Spoon
from .tools import main_done_selector


def dump_cards(bearer, repo):
    """Print release cards and their children."""
    spoon = Spoon(bearer, repo)
    release = None
    children = None
    for card in spoon.iter_cards(main_done_selector):
        if card.has_label('release'):
            dump_release(release, children)
            release = card
            children = []
        else:
            if release:
                children.append(card)
            else:
                number = '[#{0}]'.format(card.number)
                print number, card.title
    else:
        dump_release(release, children)


def dump_release(release, children):
    """Prints cards in release card."""
    if release is not None:
        release_number = '[#{0}]'.format(release.number)
        print ''
        print release_number, release.title.upper()
        for card in children:
            number = '(#{0})'.format(card.number)
            print '  -', number, card.title
        print ''


def main():
    dump_cards(*sys.argv[1:])


if __name__ == '__main__':
    main()
