# PyBlock

A simple implementation of a blockchain using Python and the 'hashlib' library.

The 'hashGenerator' function at first converts the input data to a secure hash using the SHA256 algorithm from the 'hashlib' library.

The 'Block' class defines a block using it's contents i.e. block number, data, the previous block hash and the current hash.

The 'Blockchain' class defines the Genesis Block and has an 'add_block' function for appending new blocks to the chain with the given input data.
