## HexCrypt
simple algorithm to encrypt strings as it was their own hex value

## Output
`hello, world! : 74bbe, 16e11b3!` (or `0x70x40xb0xb0xe, 0x160xe0x110xb0x3!`)

## How it works
1. read your string
2. counts its alphabet index and transforms it into a hex
3. remove the 0x and tada!!!

### possible algorithm to decrypt
1. alphabet[int(i)] for i in encrypt2, so:
```py
# step by step
alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet[int(0xa)] should be alphabet[10] that should be 'k'
```
