#! /usr/bin/env python


from setuptools import setup


setup(
    name='mdx_semanticdata_aw',
    version='1.2',
    author='Alexandre Leray & Mike Johnson Jr',
    author_email='alexandre@stdin.fr',
    description='Python-Markdown extension to add support for semantic data (RDFa).',
    url='http://activearchives.org/',
    py_modules=['mdx_semanticdata'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
