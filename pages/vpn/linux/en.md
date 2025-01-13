@title = "RiseupVPN for Linux"

## Requirements

To use Riseup's VPN service, you will need to install the program called RiseupVPN. 

## Snap

Unfortunately the Snap package is currently out of support. Please don't install `riseup-vpn` from the Snap store, as it is an out of date version. We would like to get it working again, [but we need some help from the community](https://0xacab.org/leap/bitmask-vpn/-/issues/848#note_1205365).

## Debian

There is a `riseup-vpn` package in the official Debian repositories beginning with [Debian Bookworm](https://packages.debian.org/bookworm/riseup-vpn). For a newer version, please install from `backports` or `unstable`. Install it by running the following command in a terminal, or look for the `riseup-vpn` package in your favorite package manager:

    sudo apt install riseup-vpn

## Ubuntu

The two latest Ubuntu LTS versions are supported. Please install from the [LEAP ppa](https://launchpad.net/~leapcodes/+archive/ubuntu/riseup-vpn) using:

``` 
sudo add-apt-repository ppa:leapcodes/riseup-vpn
sudo apt update
sudo apt install riseup-vpn
```

## Arch Linux / Manjaro

The are AUR (Arch User Repo) [packages](https://aur.archlinux.org/packages?O=0&SeB=nd&K=riseup-vpn) for Arch Linux and Manjaro. The version with the `-git` suffix builds the latest developer version. To install, run:

```
yay riseup-vpn
yay riseup-vpn-git
```

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

### Debug logs

Please run `riseup-vpn` with a proper `LOG_LEVEL` environment variable.

```
LOG_LEVEL=TRACE riseup-vpn
```

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
