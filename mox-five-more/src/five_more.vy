# pragma version 0.4.0
# @license MIT

import favorites

initializes: favorites
exports: (
    favorites.retrieve,
    favorites.add_person
)

@deploy
def __init__():
    favorites.__init__()

@external 
def store(new_number: uint256):
    favorites.my_favorite_number = new_number + 5
    

