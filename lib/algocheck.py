from twisted.internet import reactor, defer
import settings
import bitcoin_rpc
import util
from mining.interfaces import Interfaces

import lib.logger
log = lib.logger.get_logger('algocheck')

@defer.inlineCallbacks
def init(self):
    self.bitcoin_rpc = bitcoin_rpc
    result = (yield bitcoin_rpc.getblocktemplate())
    if result[5] == 'newmint':
	print("Contains Newmint")
    else: print("DOesnt contain newmint")
