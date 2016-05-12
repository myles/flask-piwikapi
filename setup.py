"""
Flask Piwik API
---------------

This is a super simple Flask extension to have support for doing in code
tracking in Piwik.
"""

from setuptools import setup

setup(
    name='flask-piwikapi',
    version='0.1.0',
    url='https://github.com/myles/flask-piwikapi',
    license='BSD',
    author='Myles Braithwaite',
    author_email='me@mylesbraithwaite.com',
    description='Track Flask in Piwik',
    long_description=__doc__,
    py_modules=['flask_piwikapi'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', 'piwikapi'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
