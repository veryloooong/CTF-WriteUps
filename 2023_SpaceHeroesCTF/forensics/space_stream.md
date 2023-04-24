# Space Stream

Forensics, 500- pts

> Our recon troops gathered information about the enemy territory and reported back to our Planetary Fortress. However, Zerg's Red team hackers infiltraded our database and hid all information about where their main Lair is located. Can you recover the missing image for us?

The `starstream.vhd` file is a virtual hard disk file used in VMs. Initially I did the basics for reading a disk image file with `mmls`:

```
$ mmls starstream.vhd

GUID Partition Table (EFI)
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Safety Table
001:  -------   0000000000   0000000127   0000000128   Unallocated
002:  Meta      0000000001   0000000001   0000000001   GPT Header
003:  Meta      0000000002   0000000033   0000000032   Partition Table
004:  000       0000000128   0000036991   0000036864   Basic data partition
005:  -------   0000036992   0000040960   0000003969   Unallocated
```

Usually, data partitions are what we're interested in. Let's learn more about partition 4 with `fsstat`:

```
$ fsstat -o 128 starstream.vhd

FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: NTFS
Volume Serial Number: FA9EAF5F9EAF12E5
OEM Name: NTFS    
Volume Name: New Volume
Version: Windows XP

[...]
```

This is an NTFS partition, which utilises alternate data streams, hence the name of the challenge. To see the file structure in this folder, I use `fls`:

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

Many images and text files, which can be extracted using `icat`. I used the `-f ntfs` flag for NTFS data stream support. When it's done I also unzipped the `stream5.zip` file, which contained a password-protected PDF. Looking into the `sarah_kerrigan` text file, it says:

```
I should stop using my name as password. Maybe I can just hide my file, they will never find it.
```

So I tried `sarah_kerrigan` as the password of the PDF, which unlocked it, and revealed the flag.

`shctf{r1ver_styx}`
