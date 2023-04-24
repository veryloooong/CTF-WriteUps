# Forensics

## Time Leap (250- pts)

> You've just been hired as one of SERN's "Rounders". We've been studying time travel technology, but we're having an issue generating Kerr Black Holes. We can't figure out how to configure our ionic lifter properly. We've discovered that a certain man in Tokyo managed to figure it out. After raiding his lab, you found a USB drive that probably has some useful information on it.

This is a disk image. Running `file` shows that this is a FAT sector. Using `fls`, we find the file hierarchy with a deleted `flag.gif` file:

```
$ fls convergence.img

r/r * 4:        flag.gif
r/r 6:  D-Mail.txt
r/r 8:  okabe.gif
```

Recovering this is as simple as `icat -r convergence.img 4 > flag.gif`. The file is not corrupted, so viewing the image shows the flag.

`shctf{th1s_i5_the_wi11_0f_St3in5_G4te}`

## A New Hope (250- pts)

> Princess Leia has been kidnapped! She managed to send a message to this droid we have recovered. It was damaged while we were recovering it however. It seems that sometimes you have to tear something down, in order to build them back up.

PowerPoint presentation files can actually be unpacked using `binwalk`. After unpacking and looking at the contents, I find 3 images, with `image1.png` being unopenable.

By opening the image with a hex editor (like ImHex), I see a `JFIF` signature, which means this is a `jpeg` file with a broken [header](https://github.com/corkami/formats/blob/master/image/jpeg.md). By fixing it and viewing the image again, the flag reveals itself:

`shctf{help_m3_ob1_y0u're_my_0n1y_hope}`

# Félicette (250- pts)

> a cat in space, eating a croissant, while starting a revolution.

The packet capture file is full of ICMP pings. Let's see the data in the pings...

```
ff d8 ff e0 00 10 4a 46 49 46 ...
```

Wait, this is clearly a JPEG header! Makes sense why the file name ends with `.jpg.pcap`. Now to extract these bytes using `tshark`:

```
$ tshark -r chall.jpg.pcap -T fields -e data.data > image
```

then convert them to a proper file to find an image, with the flag:

`shctf{look_at_da_kitty}`

## i OFTen see star wars (500- pts)

> Whoops... I accidentally overwrote the magicNumber & achVendID in this font file. Can you help me retrieve them?

Since they actually gave big hints on what have been overwritten, it's likely they just wrote hints of the flag into these positions. Using a hex editor, in offsets `0x14B` and `0x1F2 - 0x1F5` we can actually find part of the flag. Opening files 1-8 and connecting the pieces, the flag reveals.

`shctf{th3r3_1s_always_s0me_h0p3_4r0und}`

## space_stream (500- pts)

> Our recon troops gathered information about the enemy territory and reported back to our Planetary Fortress. However, Zerg's Red team hackers infiltraded our database and hid all information about where their main Lair is located. Can you recover the missing image for us?

This is a `.vhd` file, so clearly a disk image. `mmls` shows the data partition is at offset 128. `fsstat` shows that this is an NTFS partition, hence the "stream" (NTFS utilises alternate data streams). Now to see the file hierarchy:

```
$ fls -o 128 -r starstream.vhd

[...]
d/r 38-128-4:   data_streams:stream5.zip
d/d 38-144-1:   data_streams
+ d/r 38-128-4: .:stream5.zip
+ r/r 39-128-3: stream1.jpg
+ r/r 39-128-5: stream1.jpg:sarah_kerrigan
+ r/r 40-128-3: stream2.jpg
+ r/r 40-128-5: stream2.jpg:hint1.txt
+ r/r 41-128-3: stream3.jpg
+ r/r 41-128-5: stream3.jpg:hint2.txt
+ r/r 42-128-3: stream4.jpg
+ r/r 42-128-5: stream4.jpg:hint3.txt
```

Interesting files, so I extracted these (add the `-f ntfs` flag to `icat` for NTFS streams support).

Many images, and a text file with the name `sarah_kerrigan`, that says: 

```
I should stop using my name as password. Maybe I can just hide my file, they will never find it.
```

The zip file contains a password-protected PDF. Thanks to the above message, the password is `sarah_kerrigan`, and the flag hides within.

`shctf{r1ver_styx}`

## My God, it's full of .- ... -.-. .. .. (1000- pts)

> If sound can't travel in a vacuum then how did a microphone pick this up in space unless space is a made up concept designed to make us fear leaving Earth and joining with Xenu and the Galactic Confederacy?

Okay, title in Morse, translates to `ASCII`, and a `.wav` file. Most likely this is a Morse code sound message. So I opened Audacity, and used the spectrogram, to see... 8 signal long Morse?

Ah, it says ASCII. This is just binary encoding. Transcribing them with dots as `0` and dashes as `1` shows 

```
01110011 01101000 01100011 01110100
01100110 01111011 01001110 00110000
00100000 00110001 00100000 01100011
00110100 01101110 00100000 01001000
00110011 00110100 01110010 00100000
01110101 00100000 00111000 00110011
00110011 01010000 01011111 00111000
00110000 00110000 01110000 00101000
01001001 01101110 00101001 00100000
00111100 00100000 00101111 01100100
01100101 01110110 00101111 01101110
01110101 01101100 01101100 01110011
01110000 01100001 01100011 01100101
01111101
```

`shctf{N0 1 c4n H34r u 833P_800p(In) < /dev/nullspace}`
