from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os

MY_ADDRESS = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

def main():
    print("Lets read in the vyper code and deploy it!")
    with open("favourites.vy", "r") as favourites_file:
        favourites_code = favourites_file.read()
        compliation_details = compile_code(favourites_code, output_formats=["bytecode", "abi"])
        print(compliation_details)

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    favourites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], abi=compliation_details["abi"])
    # print(favourites_contract)

    print("Building a transaction")

    nonce = w3.eth.get_transaction_count(MY_ADDRESS)

    transaction = favourites_contract.constructor().build_transaction(
        {
        "nonce": nonce,
        "from": MY_ADDRESS,
        "gasPrice": w3.eth.gas_price,

    }
    )
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    print(signed_transaction)

    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"My Tx hash is {tx_hash}")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Done Contract deployed to {tx_receipt.contractAddress}")
    # transaction = {
    #     # from
    #     # to
    #     # gas
    #     # 
    # }
   

    

if __name__ == "__main__":
    main()