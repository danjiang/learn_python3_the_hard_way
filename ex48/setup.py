try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'ex48',
        'author': 'Dan Jiang',
        'url': 'https://github.com/danjiang/learn_python3_the_hard_way',
        'download_url': 'https://github.com/danjiang/learn_python3_the_hard_way',
        'author_email': 'danjiang5955@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex48'],
        'scripts': [],
        'name': 'ex48'
        }

setup(**config)
