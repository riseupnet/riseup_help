@nav_title = "Troubleshooting"
@title = "RiseupVPN: Troubleshooting"
@summary = "LEAP Powered VPN Troubleshooting Instructions"

## Account

The following about Accounts were noticed during the beta period.

### I cannot register my username / Somebody took my username

Our new security enhanced services are built upon the [LEAP Encryption Access Project](https://leap.se) platform. This is a whole different infrastructure and is not directly linked with our current e-mail or lists services. You can access these services under the https://black.riseup.net address.

This also means you will need to create a new account to use the VPN and other future services. But to avoid possible usernames collisions, we put all the current riseup.net usernames in "reserved" status. But don't worry, later this year you will be able to migrate your current account (including your username) to our new, way more secure services.

### My username or password is not working!

Please, check the question above.

## Bitmask

The following problems have been identified as issues in some environments.

### I don't use Debian and/or Ubuntu. How can I install Bitmask?

If you use a Debian based distribution (such as CrunchBang) or an Ubuntu based one (such as Mint) you should be installing the [stand-alone bundle](#stand-alone-bundle) and we really would love to hear your experiences installing Bitmask!. There is a huge number of GNU/Linux distributions around and there is no way to test all possible environments. If you were able to install it, please let us know... and if you weren't able, we really look forward your feedback. Anyway, **Bitmask should work on any modern GNU/Linux system**. 

### I can't connect to any/some/several sites

Please run the following commands and check the possible possible solutions.

#### Run `sudo ip route`, look for the line starting with 'default' and that 'tun0' is the value after the word 'dev'

There is a bug in Debian's Network-Manager package (in testing and unstable). If you are using this package, you probably will face this problem. You can read more about it at [Debian Bug #23755015](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23755015). 

A possible workaround is

    sudo ip route del default
    sudo ip route add default via 10.42.0.1 dev tun0

#### My problem is not listed above... What do I do now?

The first thing is to know what is causing the issue, to get us this information open your terminal application and run the command `bitmask --debug --logfile /tmp/bitmask.log`. This will run Bitmask in debug mode and store the output to a text file at `/tmp/bitmask.log`. If you are an advanced user, maybe you can trace the issue a little more. If not please file a ticket with the contents of `/tmp/bitmask.log` file and the system you use (Debian Wheezy, Mint 17, Ubuntu Trusty, etc).

Please [file a ticket](https://black.riseup.net/tickets/new)) with the contents of `/tmp/bitmask.log` file and the system you use (Debian Wheezy, Mint 17, Ubuntu Trusty, etc).

## Other issues.

### A "Configure Bitmask email Account" window shows up everytime I launch Thunderbird/Icedove

The `xul-ext-bitmask` package was installed. This is not a dependence, but a suggested package that contains the Thunderbird/Icedove extension to support LEAP as a Mail provider. Feel free to remove it, just run `sudo apt-get remove xul-ext-bitmask` and restart your Thunderbird/Icedove email client.

....

