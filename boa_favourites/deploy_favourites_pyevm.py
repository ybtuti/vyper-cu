import boa

def main():
    print("Let's read in the vyper code and deploy it!")
    favourites_contract = boa.load("favourites.vy")
    print(type(favourites_contract))

    starting_favourite_number = favourites_contract.retrieve()
    print(f"Starting favourite number is: {starting_favourite_number}")

    favourites_contract.store(5) # sends a transaction
    ending_favourite_number = favourites_contract.retrieve()
    print(f"Ending favourite number is: {ending_favourite_number}")

if __name__ == "__main__":
    main()