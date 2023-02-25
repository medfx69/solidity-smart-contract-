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
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address = "0xD1Ddab48e4208ba9931e88d4dA5D39eED24fB86F"
private_key = "0x4b2c59339260a6f95a86b049aec5ad966ca2d24e8b2266cdda425d3dd8625158"
SimpleStorge = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorge)