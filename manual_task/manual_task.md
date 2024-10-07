# Test Suit - Transaction History

## Transaction History of empty wallet
1. Open ChainPort App
2. Connect empty wallet
3. Open Transaction History

Expected results:
1. Tokens portes is 0
2. My total ports is 0
3. My ports volume is N/A
4. Participation rewards is "Coming soon"
5. My PORTX is 0
6. Transaction History list is empty

## Make new transaction
1. Open ChainPort App
2. Connect empty wallet
3. Open Transaction History -> Transaction History is empty
3. Add X tokens to wallet -> My PORTX is X
4. Make transaction
5. Open Transaction History

Expected results:
1. Tokens portes is 2
2. My total ports is 1
3. My ports volume is Y
4. Participation rewards is "Coming soon"
5. My PORTX is Z
6. Transaction History list contain transaction info
7. Transaction info is correct (date, token, from, to, port fee)

## Transaction History of wallet with >10000 transactions
1. Open ChainPort App
2. Connect wallet with >10000 transactions
3. Open Transaction History

Expected results:
1. Tokens portes is X
2. My total ports is Y
3. My ports volume is N
4. Participation rewards is "Coming soon"
5. My PORTX is Z
6. Transaction info is correct (date, token, from, to, port fee)

## Download Transaction History as .csv file
1. Open ChainPort App
2. Connect empty wallet
3. Open Transaction History
4. Download Transaction History -> .csv file is empty
5. Connect NOT empty wallet
6. Open Transaction History
7. Download Transaction History -> .csv file contain all information, information is correct

## Transaction History tooltips
1. Open ChainPort App
2. Open Transaction History
3. Hover "Token ported" tooltip -> tooltip is appeared, info is correct
4. Hover "My total ports" tooltip -> tooltip is appeared, info is correct
5. Hover "My ports volume" tooltip -> tooltip is appeared, info is correct
6. Hover "My PORTX" tooltip -> tooltip is appeared, info is correct

## Transaction History links
1. Open ChainPort App
2. Connect wallet with transaction
3. Open Transaction History
4. Click "From" link -> link works
5. Click "To" link -> link works
6. Click "Port fee" link -> link works