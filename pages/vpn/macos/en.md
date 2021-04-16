@title = "RiseupVPN for macOS"
@toc = true
@this.alias = '/vpn/macos'

## Requirements

RiseupVPN is tested on High Sierra and latest versions.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.dmg"><i class="fa fa-download"></i> Download RiseupVPN for macOS</a>

Once you have saved the file, double click <code>RiseupVPN-OSX-latest.dmg</code> to install RiseupVPN.

## Troubleshooting

### Bug Reports and Feature Requests

RiseupVPN is built using a free software program called <b>bitmask-vpn</b>.

**Step 1:** [[Search to see => https://0xacab.org/leap/bitmask-vpn/issues]] if the bug has already been reported.

**Step 2:** [[Register an account => https://0xacab.org/users/sign_in]] with [[0xacab.org => https://0xacab.org]] and log in.

**Step 3:** Create a [[new bug report or feature request => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Please include the following information in your bug report:

* Steps to reproduce the bug
* What is the expected behaviour and what do you see
* A screenshot if is something visual
* Your macOS version
* The logs of the program

### Get the logs

There are three log files each for a different component of the client:

* The systray log: `/Users/<your user>/Library/Preferences/leap/systray.log`
* The priviledged helper: `/Applications/RiseupVPN/RiseupVPN.app/Contents/helper/helper.log`
* The openvpn process: `/Applications/RiseupVPN/RiseupVPN.app/Contents/helper/openvpn.log`

When reporting a bug it is very useful to include the log files.

## Source code
RiseupVPN's clients are based on the open source software Bitmask. The code for the macOS client can be found [[here => https://0xacab.org/leap/bitmask-vpn]].
