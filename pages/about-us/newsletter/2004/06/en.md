@title = 'June'

## lists.riseup.net downtime

On June 1-2, lists were either totally down or hopelessly delayed. During this period, most list subscribers with riseup.net addresses did not get any messages from lists.riseup.net. If you have a riseup.net mail account, you should check the list archives.

This debacle was caused by a combination of our own error, a hardware failure, and AOL deciding to block us entirely.

On the one hand, we are tired of apologizing. Maybe people can go a day without email and the world will not come to an end (any faster than it already is).

On the other hand, we are acutely aware of how frustrating it is to be cut off from the ability to communicate, even over the fickle and troublesome medium of email. Outages disrupt our own organizing too, and it really sucks. We have made the promise to be a true alternative, and this can only happen if we are reliable. We are really really really really sorry.

We take downtime seriously. The good news is that we are making incremental progress, learning a lot along the way, and acquiring much better hardware (you should have seen how sketchy lists were two years ago!).

## sent-mail auto deletions after three months

riseup.net mail account users who use web-mail or IMAP have a folder called 'sent-mail.' If configured correctly, a copy of all sent mail should get copied into that folder.

Unfortunately, email put in 'sent-mail' stays there forever unless you delete the entire folder or manually delete the contents.

So, we are implementing an automatic deletion of sent mail older than three months. The last time we said we were going to do this, we backed off because a bunch of people wanted to keep all their sent mail. However, this is creating a big problem. Tons of people are now going over quota because their 'sent-mail' is filling up. They don't realize it, and they don't understand why they stop receiving mail.

If you want to keep all your sent mail, you have one week to archive it yourself (hint: in squirrelmail, select 'sent-mail' folder, click 'show all', then click the 'archive' button at the bottom).

## mail migration

We are in the process of growing from a one machine mail system to a two machine mail system. Now that the user database is on the new machine, the ongoing problems with logging in for mail users should be a thing of the past. Also, the new machine will have encrypted mail storage. While there is no such thing as absolute security, this change will help us sleep much easier at night.

NOTE: geekiness ahead, ignore if this doesn't make sense.

We would like help testing the new mail machine. If you use POP or IMAP to check your mail, create a new profile in your mail client using these test port numbers: 1100 for pop3; 9950 for pop3s; 1430 for imap4; and 9930 for imap4s (the host name, mail.riseup.net, remains the same). These are temporary port numbers just for use to test the new machine. The mail on the new machine will be up to 24 hours behind your current mail. Changes you make to your mailbox on the new machine will be regularly overwritten during updates from the current machine. When using SSL, your mail client will probably give you a little warning that the certificate is not signed by a known certificate authority. If you discover other problems, let us know at helpdesk@riseup.net.
