# Specialer

General, 500pts

> Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.

Time to see the file hierarchy... Well `ls` doesn't work, `cat` doesn't work, `where` doesn't work. `Tab` twice shows the commands. This is a barebones `bash` shell.

So to see the folder structure, I typed `cd`, then double-`Tab`bed, to see some folders:

```
Specialer$ cd 
.hushlogin  .profile    abra/       ala/        sim/
```

Inside each of the folders lay 2 text files. Now to see their contents without `cat`. Okay, use `echo` with redirectioning:

```
Specialer$ echo "$(<cadabra.txt)"
Nothing up my sleeve!
```

Doing this a few more times, and...

```
Specialer$ echo "$(<kazam.txt)"
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_811ae7e9}
```

No, I sure do not. Thanks for the pts though.
