@nav_title = "GNU/Linux"
@title = "How to: GNU/Linux"
@summary = "Getting, Installing and Configuring the Bitmask client"

To use Riseup's VPN Service you will need a LEAP Powered Riseup account. You can create one from Bitmask (the LEAP client) or from [https://black.riseup.net/signup](https://black.riseup.net/signup). **It's recommended to register your account from the Bitmask application unless you are planning to only use the VPN from Android**.

## Getting and Installing Bitmask

The Bitmask Application for GNU/Linux can be obtained two ways. If you use [Ubuntu](#ubuntu) or [Debian](#debian) you can add bitmask software repositories to keep your version up-to-date. Alternatively you can download the [stand-alone bundle](#stand-alone-bundle), which you can run from an external media like a thumb drive. Take note that the stand-alone bundle will be slower, will take more space and will be less integrated with the desktop than the Ubuntu/Debian package and it will need to be manually updated.

**We recommend to use the Ubuntu/Debian packaged version**. However, if the packaged version does not work for your distribution, you should use the stand-alone bundle.

### Ubuntu

The steps described below will add the Bitmask respositories for your system. These commands need to be run in a terminal, one by one as you will be prompted for your sudo password. The repository information will be stored at `/etc/apt/sources.list.d/bitmask.list`. 

#### Install on Trusty Thar (14.04)

	echo "deb http://deb.bitmask.net/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Uninstall

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### Debian

The steps described below will add the Bitmask respositories for your system. These commands need to be run in a terminal, one by one as you will prompted for your sudo password. The repository information will be stored at `/etc/apt/sources.list.d/bitmask.list`. 

#### Install on Wheezy (Debian 7)

You need to enable `wheezy-backports` as a software source. 

	echo "deb http://deb.bitmask.net/debian wheezy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Jessie (Debian 8)

	echo "deb http://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Jessie using the Tor anonymizing network:

	sudo apt-get install apt-transport-tor
	echo "deb tor://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Uninstall

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### Stand-alone bundle

The stand-alone Bitmask bundle should work on recent versions of Debian derived GNU/Linux distributions (Mint, Ubuntu, Elementary, etc). Remember that you are the person in charge to keep the software updated. 

To get the stand-alone bundle, first determine the type of kernel you have. This can be done with the following command: `uname -m`.

#### 64bits

If the output of that command was 'x86_64' or 'amd64' then download the lastest version avaiable from [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc). 

The following commands will download and verify the authenticity of the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2.asc
	gpg --verify Bitmask-GNU/Linux64-latest.tar.bz2.asc Bitmask-GNU/Linux64-latest.tar.bz2

If you get 'Correct signature' or 'Good signature' in the output, uncompress with the following command:

	tar xfj https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2

#### 32bits

If the output of that command was 'i686' or 'i386' then download the lastest version avaiable from [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc](https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc). 

The following commands will download and verify the authenticity of the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux32-latest.tar.bz2.asc
	gpg --verify Bitmask-GNU/Linux32-latest.tar.bz2.asc Bitmask-GNU/Linux32-latest.tar.bz2

If you get 'Correct signature' or 'Good signature' in the output, uncompress with the following command:

	tar xfj Bitmask-GNU/Linux32-latest.tar.bz2

## Using Bitmask for the first time

When you launch Bitmask for the first time we will need to setup Riseup as a LEAP Provider. These steps will guide you through that process.

### Create a LEAP powered Riseup account

![Step 1](Bitmask-1.png)

Select sign up for a new account and press *next* button.

![Step 2](Bitmask-2.png)

Select Configure a new provider and fill needed field with 'riseup.net'. Press the *check* button after that.

![Step 3](Bitmask-3.png)

Bitmask has to make sure that riseup.net is a valid provider. After that you can press *next* to continue. If there is any problem in this step, please check the troubleshooting section in this page.

![Step 4](Bitmask-4.png)

If everything went right you will see this screen. Press *next* after that.

![Step 5](Bitmask-5.png)

Bitmask has to make sure that it can connect securily with riseup.net. After that press *next* to continue. If there is any issues in this step, please check the [[troubleshooting]].

![Step 6](Bitmask-6.png)

The next step is to define an username and password for your account. Please make sure to remember them.

You will be not able to pick your current riseup.net username. This is to avoid possible issues between the current and the new systems. Don't worry, you will be able to recover your username later.

![Step 6](Bitmask-7.png)

Confirmation message. You can let Bitmask remember your username and password here, if you do please take note of them. Press *next* to continue!

![Step 7](Bitmask-8.png)

Select Encrypted Internet and Connect. Welcome to the Riseup's VPN Service. Yay!

## Troubleshooting

Please check the [[Troubleshooting section -> troubleshooting]].
