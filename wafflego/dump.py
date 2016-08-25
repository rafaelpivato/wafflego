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

from .tools import Spoon


def dump_cards(bearer, repo, selector):
    """Print cards to the standard output that pass the given selector."""
    spoon = Spoon(bearer, repo)
    in_release = []
    for card in spoon.iter_cards(selector):
        if card.has_label('release'):
            dump_release(card, in_release)
        else:
            in_release.append(card)


def dump_release(release, children):
    """Prints cards in release card."""
    print '[RELEASE]', release.title
    for card in children:
        print '  - ', card.title
