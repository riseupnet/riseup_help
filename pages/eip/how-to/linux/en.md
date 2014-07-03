@nav_title = "Linux"
@title = "How to: Linux"
@summary = "Getting, Installing and Configuring the Bitmask client"

To use Riseup's VPN Service you will need a LEAP Powered Riseup account. You can create one from Bitmask (the LEAP client) or from [https://black.riseup.net/signup](https://black.riseup.net/signup). **It's recommended to register your account from the Bitmask application unless you are planning to only use the VPN from Android**.

## Getting and Installing Bitmask

Bitmask Application for Linux is delivered in two flavors. If you use Ubuntu or Debian you can add bitmask software repositories to keep your version up-to-date. Alternatively you can download the stand-alone bundle, which you can run from an external media like a thumb drive. Take note that the stand-alone bundle will be slower, will take more space and will be less integrated with the desktop than the Ubuntu/Debian package and it will need to be manually updated. **We recommend to use the Ubuntu/Debian packaged version**.

### Ubuntu

The steps described bellow will add the Bitmask respositories for your system. These commands need to be run in a terminal, one by one as you will be promt for your sudo password. The repository information will be stored at `/etc/apt/sources.list.d/bitmask.list`. 

#### Install on Trusty Thar (14.04)

	echo "deb http://deb.bitmask.net/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Saucy Salamander (13.10)

	echo "deb http://deb.bitmask.net/debian saucy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring


#### Install on Raring Ringtail (13.04)

	echo "deb http://deb.bitmask.net/debian raring main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Uninstall

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list

### Debian

The steps described bellow will add the Bitmask respositories for your system. These commands need to be run in a terminal, one by one as you will be promt for your sudo password. The repository information will be stored at `/etc/apt/sources.list.d/bitmask.list`. 

#### Install on Wheezy (Debian 7)

You need to enable `wheezy-backports` as a software source. 

	echo "deb http://http.debian.net/debian wheezy-backports main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
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

### Stand-alone bundle

The stand-alone Bitmask bundle should work on recent versions of Debian derived linux distributions (Mint, Ubuntu, Elementary, etc). Remember that you are the person in charge to keep the software updated. 

To get the stand-alone bundle, first determine the type of kernel you have. This can be done with the following command: `uname -m`.

#### 64bits

If the output of that command was 'x86_64' or 'amd64' then download the lastest version avaiable from [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc). 

The following commands will download and verify the authenticity of the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc
	gpg --verify Bitmask-linux64-latest.tar.bz2.asc Bitmask-linux64-latest.tar.bz2

If you get 'Correct signature' or 'Good signature' in the output, uncompress with the following command:

	tar xfj https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2

#### 32bits

If the output of that command was 'i686' or 'i386' then download the lastest version avaiable from [https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc). 

The following commands will download and verify the authenticity of the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc
	gpg --verify Bitmask-linux32-latest.tar.bz2.asc Bitmask-linux32-latest.tar.bz2

If you get 'Correct signature' or 'Good signature' in the output, uncompress with the following command:

	tar xfj Bitmask-linux32-latest.tar.bz2

## Using Bitmask for the first time

When you launch Bitmask for the first time we will need to setup Riseup as a LEAP Provider. This steps will guide you on that.

h3. Create a LEAP powered Riseup account

![Step 1](linux/Bitmask-1.png)

Select sign up for a new account and press *next* button.

![Step 2](linux/Bitmask-2.png)

Select Configure a new provider and fill needed field with 'riseup.net'. Press the *check* button after that.

![Step 3](linux/Bitmask-3.png)

Bitmask has to make sure that riseup.net is a valid provider. After that you can press *next* to continue. If there is any problem in this step, please check the troubleshooting section in this page.

![Step 4](linux/Bitmask-4.png)

If everything went right you will see this screen. Press *next* after that.

![Step 5](linux/Bitmask-5.png)

Bitmask has to make sure that it can connect securily with riseup.net. After that press *next* to continue. If there is any issues in this step, please check the troubleshooting section in this page.

![Step 6](linux/Bitmask-6.png)

The next step is to define an username and password for your account. Please make sure to remember them.

Please notice that at this stage of the beta the current riseup usernames are reserved and can't be used. You will need to create a new one, don't worry it's going to be only used for this service and during this beta.

![Step 6](linux/Bitmask-7.png)

Confirmation message. You can let Bitmask remember your username and password here, if you do please take note of them. Press *next* to continue!

![Step 7](linux/Bitmask-8.png)

Select Encrypted Internet and Connect. Welcome to the Riseup's VPN Service. Yay!

## Troubleshooting

Ok, you found a bug? Let us know about it so we can fix all the stuff before open this service to everyone!

### Something is not working... What do I do now?

The first thing is to know what is causing the issue, for this open your terminal application and run the command `bitmask --debug --logfile /tmp/bitmask.log`. This will run Bitmask in debug mode and store the output to a text file at `/tmp/bitmask.log`. If you are an advanced user, maybe you can trace the issue a little more. If not please file a ticket with the contents of `/tmp/bitmask.log` file and the system you use (Debian Wheezy, Mint 17, Ubuntu Trusty, etc).

To file a ticket, please visit [https://black.riseup.net/tickets/new](https://black.riseup.net/tickets/new). Thanks for your invaluable help!

### My Riseup username and password are not working!

At this stage of the beta, all the current riseup usernames are reserved and can't be used. You will need to create a new one using the Bitmask application or at [https://black.riseup.net](https://black.riseup.net). Don't worry, these accounts will be only used for this beta period and will not be used in any other service. Feel free to user whatever username you want.