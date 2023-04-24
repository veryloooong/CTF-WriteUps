# Crypto

## Bynary Encoding (250- pts)

> Starfleet has received a transmission from Bynaus. However, the message apears to be blank. Is there some kind of hidden message here?

The title explains itself. Just use search and replace to change the spaces to `0` and the arrows to `1`, then convert to plain text.

`shctf{a_bl1nd_m4n_t3aching_an_4ndr0id_h0w_to_pa1nt}`

## I've got the same combination on my luggage! (250- pts)

> During the Battle for Druidia, the Spaceballs were able to obtain the code for the Druidia shield gate: 12345. Fortuantely, the Spaceballs had lost that battle, and Druidia lived to breathe another day. However, these security breaches were concerning and so Druidia decided to up their security. This is where you, Spaceballs' top mathematician, comes into play. We are making yet another ploy for Druidia's fresh air, and we need your help figuring out their password. We have obtained the hash of the new combination as well as the algorithm which generated the hash, which we have supplied to you. Find that combination, the fate of Planet Spaceball rests in your hands!

This is XOR arithmetic. Knowing that `x ^ x == 0` for all `x`, and that `x ^ 0 == x`, we can isolate `key1 = A ^ C`, `key2 = A ^ B`, `p = A ^ B ^ C`. Then translating `p` from hex to plaintext is simple.

`shctf{on3_e1GHt_hUnDR3d_D-R-U-I-D-I-A__}`

## Welcome to the World of Tomorrow (500- pts)

> Good news everyone! We have been tasked with deciphering a secret message from a less than friendly group of aliens! We know that they use the results of the popular "Alien Wordle" game as a key for their daily encryption method, that they love old human ciphers, and we got a copy of their game in progress. The bad news is, none of us can read alienese. Can you figure out the message?

The ciphertext looks like Caesar or some derivative. The quote is from Futurama, which features an alien alphabet that matches the one in the alien Wordle. The correct letters are `STAR??S?`. Clever guessing tells me the key is `STARDUST`, which means this is a Vigenere cipher.

`shctf{byt3_my_sh1ny_metal_f1ag}`
