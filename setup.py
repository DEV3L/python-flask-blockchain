from setuptools import setup, find_packages

setup(
    name='python-flask-blockchain',
    packages=find_packages(),
    version='0.1',
        description='A Python Flask application that demonstrates blockchain technology using Heroku.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
        url='https://github.com/DEV3L/python-flask-blockchain',
        download_url='https://github.com/DEV3L/python-flask-blockchain/tarball/0.1',
    keywords=['dev3l', 'flask', 'heroku', 'blockchain', 'cryptocurrency', 'BitCoin', 'Ethereum'],
    install_requires=[
        'Flask==0.12.2',
        'Flask-Runner==2.1.1',
        'Flask-Script==2.0.6',
        'Jinja2==2.9.6',
        'MarkupSafe==1.0',
        'Werkzeug==0.12.2',
        'click==6.7',
        'gunicorn==19.7.1',
        'itsdangerous',
        'requests==2.18.4',
        'pytest==3.2.3'
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
