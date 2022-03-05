
# Bitcoin: A Peer-to-Peer Electronic Cash System

1. The objective of Bitcoin network is to change trust-based model of digital transaction into proof-based model.
2. Transaction:
    - To solve double spending problem. The example is if you have $1 to buy a burger, and you gave it to the burger maker, you can't spend that $1 elsewhere.
    - To ensure all transactions are verified, and there’s no room for fraud. Because Bitcoin made all public.
3. Timestamp Server
    - The timestamp proves that the data must have existed at the ime, obviously, in order to get into the hash. Each timestamp includes the previous timestamp in ts hash, forming a chain, with each additional timestamp reinforcing the ones before it
4. Proof-of-work
    - to verify and validate the chain of hashes
5. Network
    - New Transaction must be transmitted to all nodes
    - Each node gather each transaction into block
    - Each node work on proof of work process for each block, then broadcast it to other nodes
    - Nodes accept it if it's valid
    - Nodes approve the block and working on next block
