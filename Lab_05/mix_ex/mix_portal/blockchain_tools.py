import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.proof}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "proof": self.proof,
            "hash": self.hash,
        }


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = Block(
            len(self.chain) + 1,
            previous_hash,
            time.time(),
            self.current_transactions,
            proof,
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            value = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if value[:4] == "0000":
                return new_proof
            new_proof += 1

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append(
            {"sender": sender, "receiver": receiver, "amount": amount}
        )
        return self.get_previous_block().index + 1

    def is_chain_valid(self):
        previous_block = self.chain[0]
        for block in self.chain[1:]:
            if block.previous_hash != previous_block.hash:
                return False
            proof_value = hashlib.sha256(
                str(block.proof**2 - previous_block.proof**2).encode()
            ).hexdigest()
            if proof_value[:4] != "0000":
                return False
            previous_block = block
        return True

    def to_dict(self):
        return {
            "pending_transactions": self.current_transactions,
            "is_valid": self.is_chain_valid(),
            "chain": [block.to_dict() for block in self.chain],
        }
