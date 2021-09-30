@title = 'Onion Service configuration'

Our Onion Services provide access to IMAP, POP3 and SMTP without leaving the Tor Network while also providing encryption. These are the settings for configuring those protocols in your e-mail client. How you connect those clients to the Tor Network it depends on the Software you use, please check their documentation for this.

## IMAP Settings

- **Server**: `5gdvpfoh6kb2iqbizb37lzk2ddzrwa47m6rpdueg2m656fovmbhoptqd.onion`
- **Login or User Name**: your riseup.net login name.
For example, if your email address was joe_hill@riseup.net, your login is @joe_hill@. This is *required*. 
- **SSL**: `No`
This is *required*. Onion Services provide encryption, there is no reason to use SSL/TLS here.
- **Port**: `143`

Note: It's possible to use SSL/TLS with the Onion Service, for that you need to enable it and switch the Port to `993`. But you will get warnings when the certificates change, this will happen frequently.

## POP3 Settings

- **Server**: `5gdvpfoh6kb2iqbizb37lzk2ddzrwa47m6rpdueg2m656fovmbhoptqd.onion`
- **Login or User Name**: your riseup.net login name.
For example, if your email address was joe_hill@riseup.net, your login is @joe_hill@. This is *required*. 
- **SSL**: `No`
This is *required*. Onion Services provide encryption, there is no reason to use SSL/TLS here.
- **Port**: `110`

Note: It's possible to use SSL/TLS with the Onion Service, for that you need to enable it and switch the Port to `995`. But you will get warnings when the certificates change, this will happen frequently.

## SMTP Settings

- **Server**: `5gdvpfoh6kb2iqbizb37lzk2ddzrwa47m6rpdueg2m656fovmbhoptqd.onion`
- **Login or User Name**: your riseup.net login name.
For example, if your email address was joe_hill@riseup.net, your login is @joe_hill@. This is *required*. 
- **SSL**: `No`
This is *required*. Onion Services provide encryption, there is no reason to use SSL/TLS here.
- **Port**: `25`

Note: It's possible to use SSL/TLS with the Onion Service, for that you need to enable it and switch the Port to `465`. But you will get warnings when the certificates change, this that will happen frequently.
