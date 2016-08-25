"""

Tools
=====

Common tools for ironing our waffle cards. You should find here
objects to help you accessing Waffle.io cards.

"""

import requests

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
    def number(self):
        return self.meta.get('number', 0)

    @property
    def labels(self):
        return self.meta.get('labels', [])

    def has_label(self, label):
        for current in self.labels:
            if current.get('name') == label:
                return True
        return False


class Spoon(object):
    """Used to access Waffle.io content."""

    def __init__(self, bearer, repo):
        """Creates new spoon with bearer token and repo path slug.

        Repo account/repo slug should have the format
        `<username>/<repository>` like in `rafaelpivato/wafflego`.

        :param str bearer: Waffle.io bearer token
        :param str repo: GitHub account/repo slug
        :raises ValueError: if any argument is `None`

        """
        if bearer is None or repo is None:
            ValueError('missing spoon parameter')
        self.bearer = bearer
        self.repo = repo

    @property
    def authorization(self):
        return 'Bearer {0}'.format(self.bearer)

    def iter_cards(self, selector):
        """Iterate over cards with the given selector.

        This will iterate through cards returning only those which
        `selector(card)` returns True.

        :param selector: function used to filter cards
        :returns: iterator over cards

        """
        url_format = 'https://api.waffle.io/{0}/cards'
        url = url_format.format(self.repo)
        headers = dict(authorization=self.authorization)
        resp = requests.get(url, headers=headers)
        for card_data in resp.json():
            card = Card(card_data)
            if selector(card):
                yield card


def main_done_selector(card):
    """Selector for cards done and not connected."""
    return not card.associations and card.state == 'closed'
