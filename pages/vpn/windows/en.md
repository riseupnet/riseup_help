@title = "RiseupVPN for windows"
@toc = true
@this.alias = '/vpn/windows'

## Requirements

RiseupVPN is tested on windows 7 and windows 10.

## Installation

Currently RiseupVPN for Windows is not available while we investigate problems related to the download.

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
* Your windows version
* The logs of the program

### Get the logs

There are three log files each for a different component of the client:

* The systray log: `C:\Users\<your user>\AppData\Local\leap\systray.log`
* The priviledged helper: `C:\Program Files\RiseupVPN\helper.log`
* The openvpn process: `C:\Program Files\RiseupVPN\openvp.log`

When reporting a bug it is very useful to include the log files.

### DNS leaks

We believe there is no DNS or IP leaks in RiseupVPN on windows, but it is not battle tested. Unlike Mac or linux, there is no firewall on windows.

If you find any kind of leaks we are very interested in hearing about it.

### Test a pre-release version

If you want to help us test a development, pre-release version of RiseupVPN, you can download the [[nightly builds => https://0xacab.org/leap/bitmask-vpn/-/jobs/artifacts/master/download?job=vendorize]].
