from __future__ import absolute_import
# selectors in stdlib as of py3.4
try:
    import selectors  # pylint: disable=import-error
except ImportError:
    # vendored backport module
    from kafka.vendor import selectors34 as selectors
selectors.DefaultSelector = selectors.PollSelector  # TODO: fix for general case
