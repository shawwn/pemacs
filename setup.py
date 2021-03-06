# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pemacs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pemacs',
    'version': '0.1.0',
    'description': 'An Emacs-style runtime for Python',
    'long_description': None,
    'author': 'Shawn Presser',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
