# who is it

Forensics, 100pts

> Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam. Can you help us identify whose mail server the email actually originated from?

The mail sender is `lpage@onionmail.otg`. A `strings` run on the file shows some interesting detail:

```
$ strings email-export.eml
[...]
spf=pass (google.com: domain of lpage@onionmail.org designates 173.249.33.206 as permitted sender) smtp.mailfrom=lpage@onionmail.org;
```

Bingo! Now to find some names:

```
$ whois 173.249.33.206
[...]
person:         Wilhelm Zwalina
address:        Contabo GmbH
```

Seems likely. Type the name in and +100pts!