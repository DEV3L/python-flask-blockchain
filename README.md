# python-flask-blockchain
Python 3.6 Flask blockchain example application

Blockchain is an immutable, sequential chain of records called Blocks.
They can contain transactions, files or any data you like, really.
They’re chained together using hashes.


## References
*Learn Blockchains by Building One*
- https://hackernoon.com/learn-blockchains-by-building-one-117428612f46


# Prerequisites
* Python 3.6+ installed
    * <https://www.python.org/downloads/>
* Virtualenv installed
    * <https://virtualenv.pypa.io/en/latest/>
    * sudo pip install --upgrade pip virtualenv virtualenvwrapper


## Run

```bash
mkvirtualenv python-flask-blockchain
python setup.py develop

python app.py runserver --port 5006
python app.py runserver --port 5005

```


## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b python_flask_blockchain`
3. Commit your changes: `git commit -am 'Add some help'`
4. Push to the branch: `git push origin python_flask_blockchain`
5. Submit a pull request :D
