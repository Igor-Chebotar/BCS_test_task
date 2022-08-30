

from .tx_creation import BCS_net
from pycoin.solve.utils import build_hash160_lookup
from pycoin.ecdsa.secp256k1 import secp256k1_generator
from bitcoinrpc.authproxy import AuthServiceProxy
from .conf import NET_PARAMS, addr_to_spend


def send_transaction():
    Bcs_network = BCS_net(addr_to_spend, rpc_user='bcs_tester', rpc_pass='iLoveBCS', NET_PARAMS=NET_PARAMS)
    Bcs_network.create_tx(satoshis=1000000, solver_f=build_hash160_lookup, generator=secp256k1_generator)
    conn = AuthServiceProxy('http://bcs_tester:iLoveBCS@45.32.232.25:3669')
    answer = None
    try:
        answer = conn.sendrawtransaction(Bcs_network.signed_new_tx_hex)
        print("send successfully")
    except Exception as e:
        print('send fail')
        raise e
    finally:
        conn.close()
    return answer

