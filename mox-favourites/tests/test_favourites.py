from script.deploy import deploy_favorites
import pytest

@pytest.fixture
def favorites_contract(scope="session"):
    return deploy_favorites()

def test_starting_values(favorites_contract):
    assert favorites_contract.retrieve() == 77

def test_can_change_values(favorites_contract):
    # Arrange
    # Act
    favorites_contract.store(42)
    # Assert
    assert favorites_contract.retrieve() == 42

def test_can_add_people(favorites_contract):
    # Arrange
    new_person = "Becca"
    favorite_number = 16

    # Act
    favorites_contract.add_person(new_person, favorite_number)

    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)
