import boa

from script.deploy import INITIAL_SUPPLY, deploy

RANDOM_USER = boa.env.generate_address("random_user")


def test_token_supply():
    snek_token = deploy()

    assert snek_token.totalSupply() == INITIAL_SUPPLY


def test_token_emits_event():
    snek_token = deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER, INITIAL_SUPPLY)
        logs = snek_token.get_logs()
        log_owner = logs[0].topics[0]
        assert log_owner == snek_token.owner()
        assert snek_token.balanceOf(RANDOM_USER) == INITIAL_SUPPLY
