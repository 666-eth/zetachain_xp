"""
  @ Author:   Mr.Hat
  @ Date:     2024/3/21 02:25
  @ Description: 
  @ History:
"""
pool_abi = [
    {
        "type": "function",
        "name": "addLiquidityETH",
        "inputs": [
            {"name": "_token", "type": "address"},
            {"name": "_amountTokenDesired", "type": "uint256"},
            {"name": "_amountTokenMin", "type": "uint256"},
            {"name": "_amountETHMin", "type": "uint256"},
            {"name": "_to", "type": "address"},
            {"name": "_deadline", "type": "uint256"},
        ],
        "outputs": [],
        "stateMutability": "payable",
        "constant": False,
    }
]

approve_abi = [
    {
        "type": "function",
        "name": "approve",
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_amount", "type": "uint256"},
        ],
        "outputs": [],
        "stateMutability": "nonpayable",
        "constant": False,
    },
    {"constant": True,
     "inputs": [
         {"name": "_owner", "type": "address"},
         {"name": "_spender", "type": "address"}
     ],
     "name": "allowance",
     "outputs": [
         {"name": "", "type": "uint256"}
     ],
     "payable": False,
     "stateMutability": "view",
     "type": "function"},

]

encoding_contract_abi = [
    {
        "inputs": [
            {
                "components": [
                    {"internalType": "bytes", "name": "path", "type": "bytes"},
                    {"internalType": "address", "name": "recipient", "type": "address"},
                    {"internalType": "uint128", "name": "amount", "type": "uint128"},
                    {"internalType": "uint256", "name": "minAcquired", "type": "uint256"},
                    {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                ],
                "internalType": "struct Swap.SwapAmountParams",
                "name": "params",
                "type": "tuple",
            }
        ],
        "name": "swapAmount",
        "outputs": [
            {"internalType": "uint256", "name": "cost", "type": "uint256"},
            {"internalType": "uint256", "name": "acquire", "type": "uint256"},
        ],
        "stateMutability": "payable",
        "type": "function",
    }
]

multicall_abi = [
    {
        "inputs": [{"internalType": "bytes[]", "name": "data", "type": "bytes[]"}],
        "name": "multicall",
        "outputs": [{"internalType": "bytes[]", "name": "results", "type": "bytes[]"}],
        "stateMutability": "payable",
        "type": "function",
    }
]

range_protocol_abi = [
    {
        "inputs": [
            {
                "internalType": "uint128",
                "name": "amountXMax",
                "type": "uint128"
            },
            {
                "internalType": "uint128",
                "name": "amountYMax",
                "type": "uint128"
            }
        ],
        "name": "getMintAmounts",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "amountX",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amountY",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "mintAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

ultiverse_abi = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "expireAt",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "eventId",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "signature",
                "type": "bytes"
            }
        ],
        "name": "buy",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
