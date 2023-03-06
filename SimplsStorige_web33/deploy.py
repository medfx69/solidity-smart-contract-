from solcx import compile_standard
import json
from web3 import Web3
with open("./SimpleStorage.sol", "r") as file:
	simple_storge_file = file.read()

compile_sol = compile_standard(
	{
		"language" : "Solidity",
		"sources" : {"SimpleStorage.sol": {"content": simple_storge_file}},
		"settings" : {
			"outputSelection":{
				"*" : {"*":["abi","metadata", "evm.bytecode", "evm.sourceMap"]}
			}
		},
	},
	solc_version="0.6.0",

)

with open("compiled_code.json", "w") as file:
	json.dump(compile_sol, file)

bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/0c894ee50246475a819c94d598a2706c"))
chain_id = 5
my_address = "0x0022c324Dadb55b6Fab9b05d37B6624102C3D9C7"
private_key = "0xa057e78cb4c290174717f17af5e07101c6c384541bd943f3471aac770a6896af"
SimpleStorge = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)
transaction = SimpleStorge.constructor().buildTransaction({
	"chainId":chain_id,
 	# "gasPrice": w3.eth.gas_price,
  	"from":my_address,
   	"nonce":nonce
})
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#working with the contract

simple_storge = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
store_transaction = simple_storge.functions.store(15).buildTransaction({
	"chainId":chain_id,
 	# "gasPrice": w3.eth.gas_price,
 	"from":my_address, "nonce":nonce +1
})

signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_stor_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print(simple_storge.functions.retrieve().call())