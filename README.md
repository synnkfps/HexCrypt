## HexCrypt
simple algorithm to encrypt strings as it was their own hex value

## Output
`hello, world! : 74bbe, 16e11b3!` (or `0x70x40xb0xb0xe, 0x160xe0x110xb0x3!`)

## How it works
1. read your string
2. counts its alphabet index and transforms it into a hex
3. remove the 0x and tada!!!

### possible algorithm to decrypt
alphabet[int(i)] for i in encrypt2, so:
```py
# step by step
alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabet[int(0xa)] should be alphabet[10] that should be 'k'
```
#### other stuff
```txt
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas ac congue ligula, non tristique erat. Vivamus pretium luctus erat, et laoreet dui posuere sed. Nulla arcu lorem, pretium vel sagittis faucibus, rutrum sit amet leo. Sed congue egestas tempus. Nunc eget efficitur quam. Donec ultricies sodales velit sed placerat. Integer accumsan eleifend tristique. Quisque non tempus tellus, semper fringilla dolor. Pellentesque finibus augue porttitor, feugiat diam id, maximus odio. Donec et justo nulla. Fusce luctus nunc vel tristique viverra. Curabitur ante sem, eleifend vitae ullamcorper ac, hendrerit vitae metus. Integer sed erat nec urna facilisis bibendum non vel tortor.
``` 
turns into 
```txt
be114c 8f1214c 3ebe11 12813 0c413, 2ed1242134131411 038f81228d6 4b813. c0424d012 02 2ed6144 b8614b0, ded 131181213810144 411013. 158150c1412 f11413814c b142131412 411013, 413 b0e114413 3148 fe12144114 1243. d14bb0 011214 be114c, f11413814c 154b 120681313812 50142811412, 1114131114c 12813 0c413 b4e. 1243 2ed6144 4641213012 134cf1412. d14d2 46413 455828131411 10140c. 3ed42 14b1311828412 12e30b412 154b813 1243 fb02411013. 8d1346411 02214c120d 4b4854d3 131181213810144. 101481210144 ded 134cf1412 134bb1412, 124cf411 5118d68bb0 3ebe11. f4bb4d1341210144 58d811412 0146144 fe111313813e11, 541468013 380c 83, c0178c1412 e38e. 3ed42 413 9141213e d14bb0. 5141224 b142131412 d14d2 154b 131181213810144 15815411110. 21411018131411 0d134 124c, 4b4854d3 1581304 14bb0c2e11f411 02, 74d311411813 1581304 c4131412. 8d1346411 1243 411013 d42 1411d0 5028b812812 1814d314c ded 154b 13e1113e11.```
