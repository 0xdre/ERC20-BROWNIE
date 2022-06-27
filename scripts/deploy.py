from brownie import DREToken
from scripts.helpers import get_account
from web3 import Web3

init_supply = Web3.toWei(9999, 'ether')

def deploy():
    account = get_account()

    dre_token = DREToken.deploy(init_supply, {'from': account})

    print(f'{dre_token.name} was deployed !')


def main():
    deploy()