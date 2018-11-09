@title = "RiseupVPN for Linux"
@this.alias = '/vpn/linux'

## Requirements

Currently, RiseupVPN is only packaged for Linux using `snap`. If you use Ubuntu, snap is already installed. Otherwise, run:

```
sudo apt install snapd
```

RiseupVPN is currently tested on the **Ubuntu LTS** and **Debian Stable**. If you have a different release, it may or may not work.

## Installation

Just search for **RiseupVPN** in the **Software Center** or click on this link:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Open RiseupVPN in Software Center
</a>

If the link above does not work for you, you can also install via the command line:

```
sudo snap install --classic riseup-vpn
```

## Troubleshooting

### Get the logs

The log of RiseupVPN is located in your home folder:
```
~/.config/leap/systray.log
```
When reporting a bug is very useful to include the log file.

### Force quit

If anything stops working, run these commands and then try again:

```
sudo pkill -e -f riseup-vpn
sudo /snap/bin/riseup-vpn.bitmask-root firewall stop
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

These commands will ensure that all RiseupVPN processes are killed, the egress firewall rules are removed, and the PID file is cleaned up.

### Won't start

If the launcher icon does not work, you can run RiseupVPN from the command line in order to identify the problem:

```
/snap/bin/riseup-vpn.launcher
```

Any problem starting will be displayed on the terminal.

### Test a pre-release version

If you want to help us test a development, pre-release version of RiseupVPN, you can install it using this command:

```
sudo snap install --classic --edge riseup-vpn
```

### Remove PID file

Sometimes RiseupVPN will fail to start if it thinks another version is already running.

If you get this error, run these commands:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```
