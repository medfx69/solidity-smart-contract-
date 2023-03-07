from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    print(f">>>  {stored_value}")
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    up_stored_value = simple_storage.retrieve()
    print(f">>>  {up_stored_value}")
def get_account():
    if network.show_active() == "development":
            return accounts[0]
    if network.shoew_active() == "Goerli":
        account = accounts.add(config["wallets"]["from_key"])
        return account


def main():
    deploy_simple_storage()
