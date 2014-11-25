# -*- coding: utf-8 -*-

WHITELIST = {
    'a': ['class', 'dir', 'href', 'id', 'lang', 'name', 'rel', 'rev', 'style',
          'target', 'title', 'xml:lang'],
    'abbr': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'acronym': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'address': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'b': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'basefont': ['color', 'face', 'id', 'size'],
    'bdo': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'big': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'blockquote': ['cite', 'class', 'dir', 'id', 'lang', 'style', 'title',
                   'xml:lang'],
    'br': ['class', 'clear', 'id', 'style', 'title'],
    'caption': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
                'xml:lang'],
    'center': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'cite': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'code': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'col': ['align', 'charoff', 'class', 'dir', 'id', 'lang', 'span', 'style'
            'title', 'valign', 'width', 'xml:lang'],
    'colgroup': ['align', 'charoff', 'class', 'dir', 'id', 'lang', 'span',
                 'style', 'title', 'valign', 'width', 'xml:lang'],
    'dd': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'del': ['cite', 'class', 'dir', 'id', 'lang', 'style', 'title',
            'xml:lang'],
    'dfn': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'dir': ['class', 'compact', 'dir', 'id', 'lang', 'style', 'title',
            'xml:lang'],
    'div': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
            'xml:lang'],
    'dl': ['class', 'compact', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'dt': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'em': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'font': ['class', 'color', 'dir', 'id', 'lang', 'style', 'title',
             'xml:lang'],
    'h1': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'h2': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'h3': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'h4': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'h5': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'h6': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title',
           'xml:lang'],
    'hr': ['align', 'class', 'dir', 'id', 'lang', 'noshade', 'size', 'style',
           'title', 'width', 'xml:lang'],
    'i': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'img': ['align', 'border', 'class', 'dir', 'height', 'hspace',
            'id', 'lang', 'longdesc', 'name', 'src', 'style', 'title',
            'vspace', 'width', 'xml:lang'],
    'ins': ['cite', 'class', 'dir', 'lang', 'style', 'title', 'xml:lang'],
    'kbd': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'li': ['class', 'dir', 'id', 'lang', 'style', 'title', 'type', 'value',
           'xml:lang'],
    'menu': ['class', 'compact', 'dir', 'id', 'lang', 'style', 'title',
             'xml:lang'],
    'ol': ['class', 'compact', 'dir', 'id', 'lang', 'start', 'style', 'title',
           'type', 'xml:lang'],
    'p': ['align', 'class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'pre': ['class', 'dir', 'id', 'lang', 'style', 'title', 'width',
            'xml:lang'],
    'q': ['cite', 'class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    's': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'samp': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'small': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'span': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'strike': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'strong': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'sub': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'sup': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'table': ['align', 'bgcolor', 'border', 'cellpadding', 'cellspacing',
              'class', 'dir', 'frame', 'id', 'lang', 'rules', 'style',
              'summary', 'title', 'width', 'xml:lang'],
    'tbody': ['align', 'charoff', 'class', 'dir', 'id', 'lang', 'style',
              'title', 'valign', 'xml:lang'],
    'td': ['abbr', 'align', 'bgcolor', 'charoff', 'class', 'colspan', 'dir',
           'height', 'id', 'lang', 'nowrap', 'rowspan', 'scope', 'style',
           'title', 'valign', 'width', 'xml:lang'],
    'tfoot': ['align', 'charoff', 'class', 'dir', 'id', 'lang', 'style',
              'title', 'valign', 'xml:lang'],
    'th': ['abbr', 'align', 'bgcolor', 'charoff', 'class', 'colspan', 'dir',
           'height', 'id', 'lang', 'nowrap', 'rowspan', 'scope', 'style',
           'title', 'valign', 'width', 'xml:lang'],
    'thead': ['align', 'charoff', 'class', 'dir', 'lang', 'style', 'title',
              'valign', 'xml:lang'],
    'tr': ['align', 'bgcolor', 'charoff', 'class', 'dir', 'id', 'lang',
           'style', 'title', 'valign', 'xml:lang'],
    'tt': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'u': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang'],
    'ul': ['class', 'compact', 'dir', 'id', 'lang', 'title', 'type',
           'xml:lang'],
    'var': ['class', 'dir', 'id', 'lang', 'style', 'title', 'xml:lang']
}