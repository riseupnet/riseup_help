@title = "RiseupVPN for macOS"
@toc = true
@this.alias = '/vpn/macos'

## Requirements

RiseupVPN is tested on Sierra and High Sierra.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.pkg"><i class="fa fa-download"></i> Download RiseupVPN for macOS</a>

Once you have saved the file, double click <code>RiseupVPN.pkg</code> to install RiseupVPN.

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
* The priviledged helper: `/Applications/RiseupVPN.app/Contents/helper/helper.log`
* The openvpn process: `/Applications/RiseupVPN.app/Contents/helper/openvpn.log`

When reporting a bug it is very useful to include the log files.

### Test a pre-release version

If you want to help us test a development, pre-release version of RiseupVPN, you can download the [[nightly builds => https://0xacab.org/leap/bitmask-vpn/-/jobs/artifacts/master/download?job=vendorize]].
