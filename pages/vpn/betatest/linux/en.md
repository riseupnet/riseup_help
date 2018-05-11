@title = "RiseupVPN for Linux"

## Requirements

Currently, RiseupVPN is only packaged using snap. If you use Ubuntu, snap is already installed. Otherwise, run:

```
sudo apt install snapd
```

RiseupVPN is currently tested on the Ubuntu LTS and Debian Stable. If you have a different release, it may or may not work.

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

### Force quit

If RiseupVPN ever crashes or your network connections are blocked, you can force quit RiseupVPN and disable the firewall like so:

```
sudo pkill -e -f riseup-vpn
sudo riseup-vpn.bitmask-root firewall stop
```

### Won't start

If the launcher icon does not work, you can run RiseupVPN from the command line in order to identify the problem:

```
riseup-vpn.launcher
```

Any problem starting will be displayed on the terminal.