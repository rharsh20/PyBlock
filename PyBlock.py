import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,block_no,data,hash,prev_hash):
        self.block_no=block_no
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
        genLast=hashGenerator('genesis_last')
        genHash=hashGenerator('genesis_hash')
        genBlock=Block(1,'genesis_data',genLast,genHash)
        self.chain=[genBlock]
    
    def add_block(self,data):
        block_no=self.chain[-1].block_no + 1
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data + str(block_no) + prev_hash)
        block=Block(block_no,data,hash,prev_hash)
        self.chain.append(block)

bc=Blockchain()
while True:
    data=input("Enter the data for the block, press 0 to end: ")
    if(data=='0'):
        break
    bc.add_block(data)

for block in bc.chain:
    print(block.__dict__)



    
