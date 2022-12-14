#SecondMiner

import threading
import Miner
import Signatures
import time
import TxBlock

my_ip = 'localhost'

wallets = [(my_ip,5005),(my_ip,5006)]

my_pr, my_pu = Signatures.generate_keys()
t1 = threading.Thread(target = Miner.minerServer, args = (('localhost', 5007),))
t2 = threading.Thread(target = Miner.nonceFinder, args = (wallets, my_pu))
t1.start()
t2.start()
time.sleep(20)
Miner.StopAll()
t1.join()
t2.join()

print(TxBlock.findLongestBlockchain(Miner.head_blocks).nonce)
print(TxBlock.findLongestBlockchain(Miner.head_blocks).previousBlock.nonce)
print(TxBlock.findLongestBlockchain(Miner.head_blocks).previousBlock.previousBlock.nonce)
