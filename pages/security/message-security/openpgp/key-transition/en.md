@title = "Key Transition"
@summary = "An example key transition statement for you to use"

Here is an example "key transition statement", to be used when you need to notify people about a change in your primary key.

NOTE: Be sure to change the below to match your details, when satisfied,
sign the document with your old and new keys.

````
Date: <Put the current date here>

For a number of reasons[0], I have recently set up a new OpenPGP key,
and will be transitioning away from my old one.

The old key will continue to be valid for some time, but I prefer all
future correspondence to come to the new one. I would also like this
new key to be re-integrated into the web of trust.  This message is
signed by both keys to certify the transition.

The old key was:

pub   1024D/<your old keyid> 2000-05-07
      Key fingerprint = <your old fingerprint here>

And the new key is:

pub   4096R/<your keyid> 2009-05-08 [expires: 2010-05-08]
      Key fingerprint = <your fingerprint here>

To fetch the full key from a public key server, you can simply do:

  gpg --keyserver keys.riseup.net --recv-key '<your fingerprint>'

If you already know my old key, you can now verify that the new key is
signed by the old one:

  gpg --check-sigs '<your fingerprint>'

If you don't already know my old key, or you just want to be double
extra paranoid, you can check the fingerprint against the one above:

  gpg --fingerprint '<your fingerprint>'

If you are satisfied that you've got the right key, and the UIDs match
what you expect, I'd appreciate it if you would sign my key. You can
do that by issuing the following command:

**
NOTE: if you have previously signed my key but did a local-only
signature (lsign), you will not want to issue the following, instead
you will want to use --lsign-key, and not send the signatures to the
keyserver
**

  gpg --sign-key '<your fingerprint>'

I'd like to receive your signatures on my key. You can either send me
an e-mail with the new signatures (if you have a functional MTA on
your system):

  gpg --export '<your fingerprint>' | gpg --encrypt -r '<your fingerprint>' --armor | mail -s 'OpenPGP Signatures' <your@email.here>


Additionally, I highly recommend that you implement a mechanism to keep your key
material up-to-date so that you obtain the latest revocations, and other updates
in a timely manner. You can do regular key updates by using parcimonie[1] to
refresh your keyring. Parcimonie is a daemon that slowly refreshes your keyring
from a keyserver over Tor. It uses a randomized sleep, and fresh tor circuits
for each key. The purpose is to make it hard for an attacker to correlate the
key updates with your keyring.

I also highly recommend checking out:

https://riseup.net/openpgp/best-practices

Please let me know if you have any questions, or problems, and sorry
for the inconvenience.

<Your Name Here>

0. https://www.debian-administration.org/users/dkg/weblog/48
1. https://gaffer.ptitcanardnoir.org/intrigeri/code/parcimonie/
````