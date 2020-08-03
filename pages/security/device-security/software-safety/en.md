@title = "Software Safety Best Practices"
@nav_title = "Software Safety"
@summary = "Best practices for installing and updating software"
@toc = true

# Keep your software up to date

Nearly every time an attacker is able to compromise a computer through a software vulnerability the attack could have been prevented if the software was up to date. This is because almost all vulnerabilities are known to the software developers and have already been fixed by the time attackers learn to take advantage of the flaws.

It is especially important to keep your operating system up to date, since the operating system has privileged access to everything that happens on your device.

How to turn on automatic updates:

* **macOS**: Select the **Apple** menu, then select **System Preferences** > **App Store** > **Automatically check for updates**.
* **Windows**: Select the **Start** button, then select **Settings** > **Update & security** > **Windows Update** > **Advanced options** and then under **Choose how updates are installed**, select **Automatic (recommended)**.

Caveats:

* You may need to restart your device for many updates to take effect, so allowing your device to restart after an update is required for the update to provide protection.
* If you have specific software requirements or custom software created for your organization, automatic updates can cause work disruption, as some OS updates may be incompatible with existing software.
* Keeping your software up to date does not help with Phishing or Malware attacks, which work by tricking the user into performing unsafe behavior.

# Use the application store

When possible, it is best to install software from the official application store for your operating system, for several reasons:

* **Authenticity**: Applications in the application store are signed by the developer and verified by the application store.
* **Updates**: The application store will help you keep your applications up to date.
* **Prevent Side Loading Attacks**: Installing an application outside the official application store is called "side loading". Side loading is currently disabled by default on Android, impossible on iOS, and is enabled by default on macOS and Windows. When side loading is enabled, your computer is more vulnerable to many different forms of malware attacks. For this reason, both macOS and Windows are trying to move to a model where side loading is disabled by default.

Note: You need to use caution with the official Android application store, Google Play, as there are often copycat applications designed to impersonate the real application.

# When in doubt, don't install

The proliferation of mobile apps, browser extensions and other free (as in zero-cost, not open source) programs has caused numerous security problems. Avoid software that hasn't been created by a company you already have a trust relationship with (i.e., any company whose tools you are already using at your organization).

Software that appears to have good intentions (like antivirus scanning) or beneficial features may be masking malicious activities in the background. In most browsers and mobile devices, an application will ask for certain permissions at installation--the information and hardware it can access on your device. These are worth looking at to make sure they at least vaguely reflect what is expected. For example, if a flashlight app asks for permissions to your contacts or to make phone calls, you probably don't want to install it. Permissions to be especially cautious around granting include access to your calls, contacts, camera, microphone, location services, or entire storage.

The way to look at permissions after installation depends on the context. In Chrome, go to chrome://extensions/ and click the permissions link for each one. On iOS devices, under Settings is a list of all permissions; under each permission is the list of apps that use it. On Android devices, go to Settings > Application Manager to view a list of apps; under each app is the list of permissions it uses.

Unfortunately most software installation systems on laptops and desktop computers will not ask for permission to access resources, so you should be extra careful about installation of software not from a mobile, browser or OS app store.

# Be careful when using pirated software

In order to run for free, pirated software usually have a modified version of the original source code from the original (paid) software. They also frequently come with extra files - the crack files - to bypass the original software's license verification. While this is sometimes harmless, most times we have no simple way of knowing if the modified code and the extra files contain some sort of malware that can infect and damage our computer.

Additionally, if you install pirated software on your work computer, it is very likely that your company will have to pay thousands of dollars in fines for your single device. When this happens, you might be fired for violating the security and privacy policies of your employer.

If there is an application you must have, and you don't want to obtain it through secure channels, consider using one of the free and open source software alternatives.

If you have no other option and need to use pirated software, **be specially careful** and try to scan the software files in an Antivirus or Malware Scanner you trust.

# Use free software

These free and open source applications are great alternatives to commonly used commercial products, available for Mac, Windows, and Linux:

* **[Gimp](https://www.gimp.org/)**: Raster graphics and photo editing program (alternative to Adobe Photoshop)
* **[Inkscape](https://inkscape.org/en/)**: Vector drawing program (alternative to Adobe Illustrator)
* **[LibreOffice](https://www.libreoffice.org/)**: Office productivity suite (alternative to Microsoft Office)
* **[Scribus](https://www.scribus.net)**: Desktop publishing application (alternative to Adobe InDesign)

# See also

* [Security Planner / Update Your Windows Computer](https://securityplanner.org/#/tool/update-your-windows-pc)
* [Security Planner / Keep Your Mac Updated](https://securityplanner.org/#/tool/update-your-mac)
* [Security Planner / Use Safe Apps](https://securityplanner.org/#/tool/use-safe-apps)
