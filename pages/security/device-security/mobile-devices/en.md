@title = "Mobile Device Security"
@nav_title = "Mobile Devices"
@toc = true

What mobile device is best for me?
==============================================

The ideal mobile device for you depends on your situation:

* **High Risk**: You suspect you might be the target of a government or professional surveillance company.
* **Moderate Risk**: You not being actively targeted, but would prefer a device that was not easy for an attacker to compromise when they have physical access.
* **Low Risk**: You do not use your mobile device for sensitive information.

High Risk
-----------------------------------------------

If you are a high risk user, **do not use your phone for anything sensitive**. The reason for this is that all phones have what is called a "baseband modem" that connects to the wireless telephone network ("cellular data"). These modems are proprietary and full of security holes that can be exploited remotely. Once compromised, the baseband modem can be used to monitor your communication and extract your personal data.

As an alternative to a mobile phone, you can purchase a tablet that only has Wi-Fi support and cannot connect to the wireless telephone network. These devices do not have a baseband modem and are much more difficult to attack remotely. With a WiFi-only device, you can still connect to the wireless telephone network by purchasing a separate "mobile hotspot".

NOTE: Airplane mode is not enough. Depending on your device, airplane mode probably still provides power to the baseband modem, leaving it open to attack.

Recommended Wi-Fi-only devices include:

* [[Pixel C => https://en.wikipedia.org/wiki/Pixel_C]] or [[Pixelbook => https://en.wikipedia.org/wiki/Google_Pixelbook]] by Google.
* [[iPad => https://en.wikipedia.org/wiki/IPad]] by Apple, but only those models **without support for cellular data**.

Moderate Risk
-----------------------------------------------

Do you have sensitive information on your mobile device that you would really prefer is not stolen by criminals or governments or noisy peers? Of course you do, everyone does.

In this case, you want to make it hard for someone to break into your device when they find it or steal it. 

Your best option, sadly, is to purchase either a device made by Google or Apple. These devices have much better hardware security than other manufacturers and are kept more up to date. However, even these devices can usually be broken into if the attacker is sophisticated enough or the device is unlocked.

Recommended devices include:

* [[Pixel => https://en.wikipedia.org/wiki/Google_Pixel]] by Google
* [[iPhone or iPad => https://en.wikipedia.org/wiki/IPhone]] by Apple (iPhone 4S or later is required to benefit from device encryption)

Low Risk
------------------------------------------------

Do you leave your phone lying around, totally unlocked? Congratulations, you are embracing the reality that mobile hardware is not very secure.

However, there will still be a lot of benefit to you, and people you communicate with, if you follow the other mobile security tips on this page.

Keep your device with you
===============================================

It is a good idea to always keep your device in your physical presence. Otherwise, there are many ways that an attacker can break into it, capture your data, and install software to monitor future your activity. 

The vulnerability of you device to depends on if you are running "recommended hardware," if you have [[device encryption => device-encryption]] enabled, and if you have your device locked with a password or PIN.

**The likelihood an attacker will be able to break into your device:**

<table class="table">
<tr>
  <th>Your Device</th>
  <th>Sophisticated Attacker</th>
  <th>Skilled Attacker</th>
  <th>Casual Attacker</th>
</tr>
<tr>
  <td>Recommended hardware + Encrypted + Locked</td>
  <td>LOW</td>
  <td>VERY LOW</td>
  <td>NONE</td>
</tr>
<tr>
  <td>Recommended hardware + Locked</td>
  <td>MEDIUM</td>
  <td>LOW</td>
  <td>VERY LOW</td>
</tr>
<tr>
  <td>Normal hardware + Encrypted + Locked</td>
  <td>HIGH</td>
  <td>MEDIUM</td>
  <td>LOW</td>
</tr>
<tr>
  <td>Normal hardware + Locked</td>
  <td>VERY HIGH</td>
  <td>HIGH</td>
  <td>MEDIUM</td>
</tr>
<tr>
  <td>Unlocked</td>
  <td>CERTAIN</td>
  <td>CERTAIN</td>
  <td>CERTAIN</td>
</tr>
</table>

Types of attackers:

* **Sophisticated attackers** include large governments and international companies that specialize in breaking into locked phones.
* **Skilled attackers** include local police and local phone-unlocking companies.
* **Casual Attackers** include skilled technologists without specialized equipment.

If your device leaves your presence and you suspect that there is a possibility it was broken into, you should back up your data and do a clean factory reset (or consider purchasing a new device).

Use Signal
================================================

Get Signal for:

<%= render partial: 'signal_android' %> <%= render partial: 'signal_ios' %>

**Signal** is a free software messaging app that can be used as a secure alternative to normal text messaging that comes with your device. It works similar to WhatsApp or Telegram, but has much better security.

Why should you use Signal?

* Your phone carrier keeps a record of every text message you send. With Signal, the phone carrier has no access to your messages or the pattern of your communication.
* It is relatively easy for an attacker to take over your phone number. With Signal, you are alerted to this possibility with a notification that someone's "security number" has changed. This also happens whenever someone gets a new phone.
* Signal can also be used for highly secure voice conversations. Your phone carrier keeps records of who you call, who you receive calls from, and the duration of all of your phone calls. With Signal, your phone carrier has none of this information. So long as your device is not compromised, the content of your call is also confidential.
* Other "secure" messaging apps, like WhatsApp, Telegram, or Wire, have a lot of problems when compared to Signal.

For more information, see [[Security Planner / Signal => https://securityplanner.org/#/tool/signal]].

Enable Find My Device
=====================================================

Consider enabling "Find My Device." This will allow you to remotely find, lock, or erase your personal information when your device is lost or stolen.

For more information, see:

* [[Security Planner / Find My Device (Android) => https://securityplanner.org/#/tool/find-my-device
]].
  * NOTE: This feature requires that you link a Google account with your device. Also, if you enable "Find My Device" then Google will retain more information about you, such as your location history.
* [[Security Planner / Find My iPhone (iOS) => https://securityplanner.org/#/tool/find-my-iphone]]

Take photos securely
======================================================

Your phone's camera includes lots of potentially sensitive information embedded in every photograph you take. Because you never know how something you post online might be used, it is a good practice to always erase personal information from a photo before sharing it.

To prevent photo "geotagging," open the settings of your camera app and look for the option to turn off saving location data in your photos.

Even with geotagging off, your camera app will save the model of your device and other potentially sensitive information. The only way to get rid of this is to use an separate application to remove "EXIF" data from the image files. These apps can also be used to remove location data from past photos you took.

For more information, see: [[3 ways to remove EXIF metadata from photos => https://www.makeuseof.com/tag/3-ways-to-remove-exif-metadata-from-photos-and-why-you-might-want-to/]].

Other tips
==================================================

* Require a passphrase, or at least a PIN, to unlock your phone. Do not use the fingerprint or face unlock features of your phone. These features are not secure.
* Configure your phone not to show detailed notifications on the lock screen.
* Know what your phone syncs with the cloud. For example, even if you delete a picture off of your phone, it may already be backed up to one or more cloud services such as iCloud or Dropbox.
