WaffleGo
========

> Unpretentious and modest script tools for Waffle.io release notes

Scripts and code found here have one main goal: create release notes
on based on Waffle.io closed cards. It is based, and depends, on a
specific workflow while using such dashboard and would not make sense
using it otherwise.


The Workflow
============

Cards are closed and dragged into Done column. When a release is done,
you create a card tagged with `release`. All cards below that, until
preceding `release` card, will be added as part of release notes
within the card itself.
