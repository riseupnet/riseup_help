@title = 'Canary Statement'
@nav_title = 'Canary'
@this.alias = '/canary'
@toc = false

![](canarypronounce.png)

#### _*noun*_

***1...*** A small songbird in the finch family, _serinus canaria domestica,_ originally native to islands in the North Atlantic.

***2...*** A mechanism to test for unsafe conditions, originating from the use of canaries in coal mines to detect poisonous gases or cave-ins. If the canary died, it was time to get out of the mine. More recently, the term has been used by some online service providers to refer to an affirmative statement, updated regularly, that the provider has not been subjected to certain legal processes. If the statement is not updated in a timely fashion, users may infer that the canary statement may no longer be true.


![](canaryimg.jpg)

<pre>
<%= render :file => 'canary-statement-signed.txt', :type => :raw %>
</pre>

## Verification instructions

You should follow [[these instructions to download riseup's gpg key and verify the keyid => network-security/certificates#complete-verification]]. Then you may follow these steps to verify this statement:

1. Download the signed [[canary statement => /about-us/canary/canary-statement-signed.txt]]
1. Then run this command in a terminal:

	```
	gpg --auto-key-retrieve --verify canary-statement-signed.txt
	```

1. You should get output that is similar to the following (note the date will change, based on when the canary statement was signed):

	```
	gpg: Signature made Thu 31 Oct 2019 09:17:02 AM PDT
	gpg:                using RSA key 4E0791268F7C67EABE88F1B03043E2B7139A768E
	gpg: Good signature from "Riseup Networks <collective@riseup.net>"
	Primary key fingerprint: 4E07 9126 8F7C 67EA BE88  F1B0 3043 E2B7 139A 768E
	```

You should make sure that it says "Good signature" in the output and confirm that the keyid matches the one you verified [[here earlier. => network-security/certificates#complete-verification]] If this text has been altered, then this information should not be trusted.
