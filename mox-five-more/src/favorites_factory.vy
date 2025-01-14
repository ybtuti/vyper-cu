# pragma version 0.4.0
# @license MIT

from interfaces import i_favorites


list_of_favorites_contracts: public(DynArray[i_favorites, 100])
original_favorite_contract: address


@deploy
def __init__(original_favorite_contract: address):
    self.original_favorite_contract = original_favorite_contract

@external
def create_favorites_contract():
    new_favorites_contract: address = create_copy_of(self.original_favorite_contract)
    favorites_contract: i_favorites = i_favorites(new_favorites_contract)

    self.list_of_favorites_contracts.append(i_favorites(new_favorites_contract))


@external
def store_from_factory(favorites_index: uint256, new_number: uint256):
    favorites_contract: i_favorites = self.list_of_favorites_contracts[favorites_index]
    extcall favorites_contract.store(new_number)

@external
def view_from_factory(favorites_index: uint256) -> uint256:
    return staticcall self.list_of_favorites_contracts[favorites_index].retrieve()

