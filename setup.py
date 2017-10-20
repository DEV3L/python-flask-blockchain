from setuptools import setup, find_packages

setup(
    name='python_flask_blockchain',
    packages=find_packages(),
    version='0.1',
        description='A Python Flask application that demonstrates blockchain technology using Heroku.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
        url='https://github.com/DEV3L/python-flask-blockchain',
        download_url='https://github.com/DEV3L/python-flask-blockchain/tarball/0.1',
    keywords=['dev3l', 'flask', 'heroku', 'blockchain', 'cryptocurrency', 'BitCoin', 'Ethereum'],
    install_requires=[
        'Flask',
        'Flask-Runner',
        'Flask-Script',
        'Jinja2',
        'MarkupSafe',
        'Werkzeug',
        'click',
        'gunicorn',
        'itsdangerous',
        'requests',
        'pytest'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: THE BEER-WARE LICENSE',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
