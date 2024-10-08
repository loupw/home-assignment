# Home Assignment

### ETA
* Manual Task 1 hour
* Automation Task 3.5 hours

## Some main Crypto concepts

**Blockchain** is a sequential distributed database with growing lists of records (blocks) that are securely linked together via cryptographic hashes.

**Smart Contract** is a computer program or a transaction protocol that is intended to automatically execute, control or document events and actions according to the terms of a contract or an agreement.

**GAS token** is a token used to pay for transaction fees on a blockchain network.

**ERC-20 token** is a standard for creating and issuing smart contracts on the Ethereum blockchain.

**Wallet** is a device, program or an online service which stores the public and/or private keys for cryptocurrency transactions.

**ChainPort bridge** is a full Cross-chain bridge portal that facilitate communication and value exchange between distinct blockchain ecosystems.

## Manual Task

Files are in manual_task folder.

#### (!)
- Test Cases are written based on screenshots.
- X, Y, Z and N means that we know expected results and verify that they are correct.

## Automation Task

Files are in automation_task folder.

#### Setup
```
cd %path to automation_task%
%install allure%
pip install -r requirements.txt
```

#### Run
```
python -m pytest --alluredir allure-results --clean-alluredir
allure serve allure-results
```
#### (!)

- Site from Task 1 sometimes doesn't load at all.
- Tested in Chrome only.
- Tests sometimes unstable.
