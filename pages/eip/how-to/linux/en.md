@nav_title = "Linux"
@title = "How to: Linux"
@summary = "Getting, Installing and Configuring the Bitmask client"

To use Riseup's VPN Service you will need a LEAP Powered Riseup account. You can create one from the Bitmask or from https://black.riseup.net/signup. **It's recommended to register your account from the Bitmask application unless you are planning to only use the VPN from Android**.

## Getting and Installing Bitmask

Bitmask Application for Linux is delivered in two flavors. If you use Ubuntu or Debian you can add bitmask software repositories to keep your version up-to-date. Alternatively you can download the stand-alone bundle, which you can run from an external media like a thumb drive. Take note that the stand-alone bundle will be slower, will take more space and will be less integrated with the desktop than the Ubuntu/Debian package and it will need to be manually updated. **We recommend to use the Ubuntu/Debian packaged version**.

### Ubuntu

#### Install on Trusty Thar (14.04)

	sudo add-apt-repository "deb http://deb.bitmask.net/debian trusty main"
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Saucy Salamander (13.10)

	sudo echo "deb http://deb.bitmask.net/debian saucy main" >> /etc/apt/sources.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring


#### Install on Raring Ringtail (13.04)

	sudo echo "deb http://deb.bitmask.net/debian raring main" >> /etc/apt/sources.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

### Debian

#### Install on Wheezy (Debian 7)

	sudo echo "deb http://deb.bitmask.net/debian wheezy main" >> /etc/apt/sources.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Jessie (Debian 8)

	sudo echo "deb http://deb.bitmask.net/debian jessie main" >> /etc/apt/sources.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Install on Jessie using the Tor anonymizing network:

	sudo apt-get install apt-transport-tor
	sudo echo "deb tor://deb.bitmask.net/debian jessie main" >> /etc/apt/sources.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

### Stand-alone bundle

The stand-alone Bitmask bundle should work on recent versions of Debian derived linux distributions (Mint, Ubuntu, Elementary, etc). Remember that you are the person in charge to keep the software updated. 

To get the stand-alone bundle we need to know which kind of kernel do we have. That can be done with the following command: `uname -m`.

#### 64bits

If the output of that command was 'x86_64' then download the lastest version avaiable from [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc). You can download and verify the authenticity of the bundle using the following commands.

You can use the following commands to download and verify the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc
	gpg --verify Bitmask-linux64-latest.tar.bz2.asc Bitmask-linux64-latest.tar.bz2

If and only if you get 'Correct signature' in the output, uncompress.

	tar xfj https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2

#### 32bits

If the output of that command was 'i686' or 'i386' then download the lastest version avaiable from [https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2) and it's OpenPGP signature from [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc). You can download and verify the authenticity of the bundle using the following commands.

You can use the following commands to download and verify the bundle.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc
	gpg --verify Bitmask-linux32-latest.tar.bz2.asc Bitmask-linux32-latest.tar.bz2

If and only if you get 'Correct signature' in the output, uncompress.

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

![Step 6](linux/Bitmask-7.png)

Confirmation message. You can let Bitmask remember your username and password here, if you do please take note of them. Press *next* to continue!

![Step 7](linux/Bitmask-8.png)

Select Encrypted Internet and Connect. Welcome to the Riseup's VPN Service. Yay!
