@title = "RiseupVPN for macOS"
@toc = true
@this.alias = '/vpn/macos'

## Requirements

RiseupVPN is tested on Sierra and High Sierra.

## Installation

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.pkg"><i class="fa fa-download"></i> Download RiseupVPN for macOS</a>

Once you have saved the file, double click <code>RiseupVPN.pkg</code> to install RiseupVPN.

## Troubleshooting

### Get the logs

There is three log files each for a different component of the client:
* The systray log: `/Users/<your user>/Library/Preferences/leap/systray.log`
* The priviledged helper: `/Applications/RiseupVPN.app/Contents/helper/helper.log`
* The openvpn process: `/Applications/RiseupVPN.app/Contents/helper/openvpn.log`
When reporting a bug is very useful to include the log files.
