@title = 'May'


## Our Security Statement

If you would like updates on Riseup's interaction with the state surveillance apparatus, go to: 

https://help.riseup.net/canary

We will be updating it roughly quarterly. 

It currently states: 
 
As of April 21, 2014, Riseup has not received any National Security Letters or FISA court orders, and we have not been subject to any gag order by a FISA court. Riseup has never placed any back-doors in our software and have not received any requests to do so. Riseup has never disclosed any user communications to any third party.

Regarding server seizures, in a widely-reported incident, the FBI seized one of Riseup's servers in April 2012. This incident happened in New York. The machine was encrypted and contained no user data. The server was returned, but it was not placed back in service. Other than this incident, as of April 21, 2014, Riseup confirms that it has never had any hardware seized or taken by any third party.


## Yahoo and Lists

You may have been seeing some bounces from yahoo.com and aol.com. They are due to those corporation's changes in policy. They published a DMARC record (an anti-spam technology) which
effectively says "if any server other than our official servers sends
mail with a sender using a yahoo.com (or aol.com) address, assume the
mail is spam and reject it". The DMARC record is then used by other
sites (like hotmail.com, comcast.net, and many others) to decide what
to do when mail arrives.

The problem with this is that mailing list software, like
lists.riseup.net, retransmits messages to others. So when a yahoo.com
or aol.com user sends mail to a list and it gets redistributed (with
the yahoo.com/aol.com address still as the sender) then receiving mail
servers say "this message wasn't sent from one of yahoo/aol's servers,
it must be spam, reject!" and bounce the message. This is why you may be were
seeing lots of bounces, and not just from yahoo.com/aol.com but other
sites as well.

There is a full explanation at http://jrl.guru/Email/yahoobomb.html

The easiest thing that can fix this is yahoo/aol changing their policy.
But until then here is what riseup is doing:

* In order to limit the damage, we are now blocking all senders to
  lists.riseup.net that are using a yahoo.com or aol.com address.
  Upon sending, yahoo.com and aol.com senders will immediately get
  an error that explains things. This is bad for the senders, but it
  will prevent the mass bounces and bounce related unsubscriptions.
* We encourage everyone to move away from yahoo.com/aol.com to an
  email provider that protects your privacy and doesn't make it
  impossible to run mailing lists
* We're investigating other ways we can hack around this problem, we
  hope to have a fix soon.


## Money!

Money getting you down? Us too. If you can donate a bit to Riseup, every small amount goes a long way to supporters thousands of groups and activists around the world. 
https://help.riseup.net/donate

And, wepay, one of the ways people donate to Riseup, has stopped accepting donations. For anyone who had set up reoccurring donations with them, it would be mighty awesome if you could set up some other form of reoccurring payment. Thanks! 
