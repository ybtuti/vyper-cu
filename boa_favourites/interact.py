import os
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import boa
from dotenv import load_dotenv

load_dotenv()


MY_CONTRACT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favourite_deployer = boa.load_partial("favourites.vy")
    favourite_contract = favourite_deployer.at(MY_CONTRACT)

    favourite_number = favourite_contract.retrieve()
    print(f"The favourite number is: {favourite_number}")

    favourite_contract.store(22)
    favourite_number_updated = favourite_contract.retrieve()

    print(f"The updated favourite number is: {favourite_number_updated}")




if __name__ == "__main__":
    main()