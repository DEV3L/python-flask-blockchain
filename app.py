from uuid import uuid4

from flask import Flask, jsonify
from flask_script import Manager

from blockchains.blockchain import Blockchain

app = Flask(__name__)
manager = Manager(app)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route("/")
def index():
    return 'Hello world!'


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == "__main__":
    manager.run()
