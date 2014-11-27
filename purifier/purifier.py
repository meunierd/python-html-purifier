# -*- coding: utf-8 -*-
"""
Based on native Python module HTMLParser purifier of HTML
"""
from __future__ import unicode_literals  # NOQA

try:
    from HTMLParser import HTMLParser
except ImportError:  # python2
    from html.parser import HTMLParser

import logging


logger = logging.getLogger(__name__)


class InvalidMarkupException(Exception):
    pass


class InvalidTagException(InvalidMarkupException):
    pass


class InvalidAttributeException(InvalidMarkupException):
    pass


class HTMLPurifier(HTMLParser):
    """
    Cuts the tags and attributes are not in the whitelist. Their content is
    leaves.
    Signature of whitelist:
    {
        'enabled tag name' : ['list of enabled tag's attributes']
    }
    You can use the symbol '*' to allow all tags and/or attributes
    """

    isNotPurify = False
    removeEntity = False
    unclosedTags = ['br', 'hr']
    isStrictHtml = False
    log = logger

    def __init__(self, whitelist=None, remove_entity=False, validate=False):
        """
        Build white list of tags and their attributes and reset purifying data
        """
        self.removeEntity = remove_entity
        HTMLParser.__init__(self)
        self.__set_whitelist(whitelist)
        self.reset_purified()
        self.validate = validate

    def feed(self, data):
        """
        Main method for purifying HTML (overrided)
        """
        self.reset()
        self.reset_purified()
        HTMLParser.feed(self, data)
        return self.html()

    def reset_purified(self):
        """
        Reset of inner purifying data
        """
        self.data = []

    def html(self):
        """
        Current representation of purifying data as unicode
        """
        return ''.join(self.data)

    def handle_starttag(self, tag, attrs):
        """
        Handler of starting tag processing (overrided, private)
        """
        self.log.debug('Encountered a start tag: %s %s', tag, attrs)
        if self.isNotPurify or tag in self.whitelist:
            attrs = self.__attrs_str(tag, attrs)
            attrs = ' ' + attrs if attrs else ''
            if tag in self.unclosedTags and self.isStrictHtml:
                tmpl = '<%s%s />'
            else:
                tmpl = '<%s%s>'
            self.data.append(tmpl % (tag, attrs,))
        elif self.validate and tag not in self.whitelist:
            raise InvalidTagException(tag)

    def handle_endtag(self, tag):
        """
        Handler of ending tag processing (overrided, private)
        """
        self.log.debug('Encountered an end tag : %s', tag)
        if tag in self.unclosedTags:
            return
        if self.isNotPurify or tag in self.whitelist:
            self.data.append('</%s>' % tag)
        elif self.validate and tag not in self.whitelist:
            raise InvalidTagException(tag)

    def handle_data(self, data):
        """
        Handler of processing data inside tag (overrided, private)
        """
        self.log.debug('Encountered some data: %s', data)
        self.data.append(data)

    def handle_entityref(self, name):
        """
        Handler of processing entity (overrided, private)
        """
        self.log.debug('Encountered entity: %s', name)
        if not self.removeEntity:
            self.data.append('&%s;' % name)

    def __set_whitelist(self, whitelist={}):
        """
        Update default white list by customer white list
        """
        # add tag's names as key and list of enabled attributes as value for
        # defaults
        self.whitelist = {}
        # tags that removed with contents
        if isinstance(whitelist, dict) and '*' in whitelist.keys():
            self.isNotPurify = True
            return
        else:
            self.isNotPurify = False
        self.whitelist.update(whitelist)

    def __attrs_str(self, tag, attrs):
        """
        Build string of attributes list for tag
        """
        enabled = self.whitelist.get(tag, ['*'])
        all_attrs = '*' in enabled
        items = []
        for attribute, value in attrs:
            if all_attrs or attribute in enabled:
                items.append('%s="%s"' % (attribute, value or '',))
            elif self.validate and attribute not in enabled:
                raise InvalidAttributeException(attribute)
        return ' '.join(items)
