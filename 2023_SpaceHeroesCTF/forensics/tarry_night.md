# tarry_night

Forensics, 250- pts

> I compressed my favorite painting for transport, but I got a little too curious and started playing around with it, and now I can't get my image back! Can you help me out?

## Analysis

When using `file` on the downloaded `tarry_night.tar.gz`, the output shows that this is NOT a `.tar.gz` file, but rather just data. This could possibly mean a few things:

* The data had been XOR'ed with a key, in which case we can use `xortool`
* The file header is corrupted, in which case use a hex editor like `ImHex`
* The file might not even be a `.tar.gz` file

## The archive

When opening the file with ImHex, I see the `tarry_night.tar` filename near the header, which means this is a normal, un-XOR'ed `.tar.gz` file, poosibly with a corrupted header.

According to [this page](docs.fileformat.com/compression/gz), the magic number `1f 8b` is missing. So to add them, now `file` reads the archive correctly. But extracting the file still fails, because the flag `FNAME` is not properly set. In fact, the header is still missing the compression method byte. So after the magic number, I added byte `08`. Now I extract it and get the `tarry_night.tar` file.

## The file

Using `file` on `tarry_night.tar` shows this is again data. With a hex editor, I see that there are a bunch of `0c` bytes. This means that this file has been XOR'ed with byte `0c`. Using `xortool-xor`, we can un-XOR the file:

```
$ xortool-xor -f ./tarry-night.tar -s '\x0c' > unxored.tar
```

Extract the image to find the flag.

```
shctf{w0w_0xc_b34ut1ful_t4rs!!!}
```