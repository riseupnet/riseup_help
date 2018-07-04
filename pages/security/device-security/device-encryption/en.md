@title = "Device Encryption"
@toc = true
@summary = "The how and why of encrypting your device's storage"

# Why Use Device Encryption?

Device encryption means that the contents of your device's storage--the part that contains the operating system, programs you have installed, and your organizational data--are scrambled so that they cannot be easily accessed when the device is off.

Without this feature, someone who steals your device, finds your lost device, or otherwise accesses your hardware can easily read your files and possibly impersonate you to your systems. Even worse, an attacker can install malware that allows them to remotely access all your activities.

There are two types of device encryption:

* "Full Disk" Encryption: This approach encrypts everything on the device's primary storage, including the operating system.
* "Partial Disk" Encryption: This approach **does not** encrypt the operating system. This approach will protect your data, but makes it easier for an attacker with access to your device to install malware.

The default for Windows and macOS is full disk encryption. All Linux distributions also support full disk encryption, but you must choose to enable this when installing the OS (otherwise you will only have home directory encryption).

# How-to Enable Device Encryption

Although full disk encryption is enabled by default on some mobile devices, it must be manually set up on all laptop and desktop computers, and many phones and tablets.

Desktop How-to:

* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  * IMPORTANT: By default, Microsoft makes a cloud backup of your device encryption key and is able to decrypt your device. If you are concerned about the possibility of a national government gaining access to the contents of your device, you should disable this "feature" and [[generate new encryption keys => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]] now.
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)

Mobile How-to:

* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Device Encryption Caveats

**Authentication Must Be Enabled** Device encryption is not effective unless the device requires authentication to use. For example, you are required to log in when using your laptop or provide a PIN when using your mobile device.

**Makes Disk Recovery Impossible** Full disk encryption can also increase the risk of you losing access to some of your information if robust password- or PIN-management practices are not in place. A lost password or PIN as well as failure of the part of the disk where the encryption keys are stored will generally mean you (as well as anyone else) cannot recover your data. Ensure that you use syncing services and/or have regular backups of your data to minimize the risk of data loss.

**Device Must Be Off or Locked** Full disk encryption provides protection only when your computer is turned off, or turned on but awaiting a password to start up. Once you have logged in, the computer has the secret key needed for decrypting your data in its memory (so you can work!) and so even with the screen locked there is some risk of someone obtaining access to the contents of your computer while it is running or even sleeping. However, in general, surmounting those controls is a highly technical attack and that risk shouldn't stop you from keeping your computer turned on or logged in when you need to work. It is, however, best to to turn off your devices whenever your device will be away from you in a hostile environment. If you are concerned you may be a target of an attack, then it is best practice to keep your device physically in your presence at all times.

# See also

* [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
* [Security Self-defense / How to: Encrypt Your iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
