from src import favorites, favorites_factory
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    return favorites_contract

def deploy_factory(favorites_contract: VyperContract):
    factory_contract: VyperContract = favorites_factory.deploy(favorites_contract)
    factory_contract.create_favorites_contract()

    new_favorites_address: str = factory_contract.list_of_favorites_contracts(0)
    new_favorites_contract: VyperContract = favorites.at(new_favorites_address)
    new_favorites_contract.store(77)
    print(f"Stored value in new favorites contract: {new_favorites_contract}")


def moccasin_main():
    favorites_contract = deploy_favorites()
    deploy_factory(favorites_contract)