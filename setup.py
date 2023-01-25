import re
from setuptools import setup

VERSION = ''
with open('discord/__init__.py') as f:
    searched = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)
    if searched:
        VERSION = searched.group(1)
    else:
        raise RuntimeError('Cannot find version.')

README = ''
with open('README.rst') as f:
    README = f.read()

HISTORY = ''
with open('HISTORY.rst') as f:
    HISTORY = f.read()

requirements = [
    'aiohttp==3.8.3'
]

packages = [
    'discord',
    # Add sub-packages here, example: 'discord.subpackage'
]

# This project uses semantic versioning, see https://semver.org/
# https://pypi.org/classifiers/
# Development Status :: 1 - Planning
# Development Status :: 2 - Pre-Alpha
# Development Status :: 3 - Alpha
# Development Status :: 4 - Beta
# Development Status :: 5 - Production/Stable
# Development Status :: 6 - Mature
# Development Status :: 7 - Inactive

setup(
    name='discord.bot',
    author='Tygo',
    url='https://github.com/Tygo01/discord.bot',
    project_urls={
        'Documentation': 'https://discordbot.readthedocs.io/en/latest/',
        'Issue Tracker': 'https://github.com/Tygo01/discord.bot/issues'
    },
    version=VERSION,
    packages=packages,
    license='GPL-3.0',
    description='An API wrapper for discord bots, written in python.',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.10.0,<3.11.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed'
    ],
)