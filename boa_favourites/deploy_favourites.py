import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account


load_dotenv()


def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favourites_contract = boa.load("favourites.vy")
    print(f"Starting favourite number is: {favourites_contract.retrieve()}")

    print("Storing Number ...")
    favourites_contract.store(5)

    ending_favourite_number = favourites_contract.retrieve()
    print(f"Ending favourite number is: {ending_favourite_number}")


if __name__ == "__main__":
    main()