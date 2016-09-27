from debug import *
from zoodb import *

import rpclib
import hashlib
import random


def transfer(sender, recipient, zoobars, token):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('transfer', sender=sender, recipient=recipient, zoobars=zoobars, token=token)
        return ret

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('balance', username=username)
        return ret


def new_user(username, token):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('new_user', username=username, token=token)
        return ret


