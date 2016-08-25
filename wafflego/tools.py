"""

Tools
=====

Common tools for ironing our waffle cards. You should find here
objects to help you accessing Waffle.io cards.

"""

from itertools import ifilter


class Card(object):
    """Represents one card loaded from Waffle.io."""

    def __init__(self, data):
        self.data = data

    @property
    def associations(self):
        return self.data.get('associations', [])

    @property
    def meta(self):
        return self.data.get('githubMetadata', [])

    @property
    def title(self):
        return self.meta.get('title', 'Untitled')

    @property
    def state(self):
        return self.meta.get('state', 'unknown')

    @property
    def labels(self):
        return self.meta.get('labels', [])

    def has_label(self, label):
        found = next(
            ifilter(
                lambda label: label['name'] == label,
                self.meta.labels,
            ),
            None,
        )
        return found


class Spoon(object):
    """Used to access Waffle.io content."""

    def __init__(self, bearer, repo):
        self.bearer = bearer
        self.repo = repo

    def iter_cards(self, selector):
        raise NotImplementedError()


def main_done_selector(card):
    """Selector for cards done and not connected."""
    return not card.associations and card.state == 'closed'
