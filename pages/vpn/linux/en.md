@title = "RiseupVPN for Linux"

## Requirements

To use Riseup's VPN service, you will need to install the program called RiseupVPN. On Linux, it is available either as a `snap`, or as a package in Debian Stable.

RiseupVPN is currently tested on **Ubuntu LTS** (18.04) and **Debian Stable**. If you have a different release, it may or may not work.

## Snap Installation

If you use Ubuntu, snap is already installed. Otherwise, run:

```
sudo apt install snapd gnome-software-plugin-snap
```

Then, search for **RiseupVPN** in the **Software Center** or click on this link:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Open RiseupVPN in Software Center
</a>

If the link above does not work for you, you can also install via the command line:

```
sudo snap install --classic riseup-vpn
```

If you get an error stating that "python" is missing from /usr/bin/env, you need to install python. This is the case for instance in Lubuntu, at least since version 19.04.

## Package Installation

The VPN is packaged in Debian bookworm and later, install it by running the following command in a terminal, or look for the `riseup-vpn` package in your favorite package manager:

       sudo apt install riseup-vpn

Older releases are not currently supported (but you can use the snap method above).

## Troubleshooting

### Bug Reports and Feature Requests

RiseupVPN is built using a free software program called <b>bitmask-vpn</b>.

**Step 1:** [[Search to see => https://0xacab.org/leap/bitmask-vpn/issues]] if the bug has already been reported.

**Step 2:** [[Register an account => https://0xacab.org/users/sign_in]] with [[0xacab.org => https://0xacab.org]] and log in.

**Step 3:** Create a [[new bug report or feature request => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Please include the following information in your bug report:

* Steps to reproduce the bug
* What is the expected behaviour and what do you see
* A screenshot if it is something visual
* Your linux distribution and its version
* The log of the program

### Get the logs

The log of RiseupVPN is located in your home folder:

```
~/.config/leap/systray.log
```

When reporting a bug it is very useful to include the log file.

### Force quit

If anything stops working, run this command and then try again:

```
sudo pkill -e -f riseup-vpn
```

### Won't start

If the launcher icon does not work, you can run RiseupVPN from the command line in order to identify the problem:

```
/snap/bin/riseup-vpn.launcher
```

Any problem starting will be displayed on the terminal.

### Have the tray icon visible on GNOME

In recent GNOME versions, tray icons are not shown by default, or are shown in a tiny tray in the bottom right of
the screen. In order to have RiseupVPN's icon visible in the top-right corner of the screen, you can install the `AppIndicator`
GNOME extension and enable it:

For Debian-based distributions (only tested on Debian Buster):
* Install package `gnome-shell-extension-appindicator`, from the package manager or using this command line in a terminal: `sudo apt install gnome-shell-extension-appindicator`
* Close your session and reopen it, or restart the computer
* Open the `Tweaks` application, and in the left pane, select Extensions
* Enable "Kstatusnotifieritem/appindicator support"
* Enjoy :)

### RiseupVPN on Linux Mint

On Linux Mint, Snap is sometimes disabled by default, so you have to enable it first, by running the following command:

```
sudo mv /etc/apt/preferences.d/nosnap.pref /etc/apt/preferences.d/nosnap.pref.disabled
```

Then install Snap:

```
sudo apt install snapd
```

Install RiseupVPN from Snap:

```
sudo snap install --classic riseup-vpn
```

Create RiseupVPN entry in Linux Mint menu:

```
cp /var/lib/snapd/desktop/applications/riseup-vpn_riseup-vpn.desktop /usr/share/applications/
```


### Test a pre-release version

If you want to help us test a development, pre-release version of RiseupVPN, you can install it using this command:

```
sudo snap install --classic --beta riseup-vpn
```

### Remove PID file

Sometimes RiseupVPN will fail to start if it thinks another version is already running.

If you get this error, run these commands:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

## Source code
RiseupVPN's clients are based on the open source software Bitmask. The code for the Linux client can be found [[here => https://0xacab.org/leap/bitmask-vpn]].
