from setuptools import setup

import purifier


setup(
    name="html-purifier3",
    version=purifier.__version__,
    packages=["purifier"],
    url='https://github.com/meunierd/python-html-purifier',
    author='pixel',
    author_email='ivan.n.sergeev@gmail.com',
    maintainer='meunierd',
    maintainer_email='devon@eventmobi.com',
    license='GPL3',
    description='''Cuts the tags and attributes from HTML that are not in the
    whitelist. Their content is left.''',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
