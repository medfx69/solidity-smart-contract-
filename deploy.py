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

bytcode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))