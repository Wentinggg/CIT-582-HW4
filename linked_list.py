import hashlib
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, content, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.content = content
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.content).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


M4BlockChain = []


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")


M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
'''
Takes as input a block (a Python object of class Block) and returns a new block that follows the block provided. 
Your “next_block” function should set the index of the next block to be the index of the previous block plus one, 
the timestamp should be the current time, 
and the content should be string “this is block i” where i is the index of the block.
'''
def next_block(last_block):
    index = len(M4BlockChain)
    content = "this is block " + str(index)
    return Block(index, datetime.now(), content, last_block.hash)


# append 5 blocks to the blockchain
# take an existing chain “block_list” and append five blocks to it
def app_five(block_list):
    for i in range(5):
        block_list.append(next_block(block_list[len(block_list) - 1]))
