#!/usr/bin/env python

from distutils.core import setup

setup(name='rosetta_form_scripts',
    version='0.1',
    description='Various form conversion hacks',
    author='QED Inc.',
    author_email='info@qed.ai',
    packages=[],
    scripts=['redcap2xlsform.py', 'split_xls_sheets.py'],
    install_requires=[
        'xlwt',
        'html2text',
        'xlrd',
        'pandas'
    ],
)
