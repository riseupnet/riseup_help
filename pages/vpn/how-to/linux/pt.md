@nav_title = "GNU/Linux"
@title = "Manual: GNU/Linux"
@summary = "Bitmask para Linux: baixe, instale e configure"

Para usar o serviço de VPN do Riseup, você precisa de uma conta Riseup com tecnologia LEAP. Você pode criá-la usando o Bitmask (cliente LEAP) ou acessando [https://black.riseup.net/signup](https://black.riseup.net/signup). **É recomendável registrar sua conta usando o aplicativo Bitmask, a não ser que você pretenda usar apenas a VPN para Android**.

## Baixe e instale o Bitmask

O aplicativo Bitmask para GNU/Linux pode ser obtido de duas maneiras. Se você usa [Ubuntu](#ubuntu) ou [Debian](#debian), adicione os repositórios do Bitmask para manter sua versão atualizada. Uma alternativa é baixar o [pacote independente](#stand-alone-bundle), que pode ser executado a partir de mídia removível, como um pen-drive. Lembre-se que o pacote independente será mais lento, tomará mais espaço e será menos integrado ao sistema que o pacote próprio do Ubuntu ou Debian, além de precisar ser atualizado manualmente.

**Recomendamos a versão em pacote próprio do Ubuntu ou Debian**. Porém, se a versão em pacote não der certo na sua distribuição, você deverá usar o pacote independente.

### Ubuntu

Os passos abaixo tratam de adicionar os repositórios do Bitmask ao seu sistema. Estes comandos precisam ser executados em um terminal, um por um, conforme for pedida a sua senha _sudo_. As informações do repositório serão armazenadas em `/etc/apt/sources.list.d/bitmask.list`.

#### Instale no Trusty Thar (14.04)

	echo "deb http://deb.bitmask.net/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Desinstale

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### Debian

Os passos abaixo tratam de adicionar os repositórios do Bitmask ao seu sistema. Estes comandos precisam ser executados em um terminal, um por um, conforme for pedida a sua senha _sudo_. As informações do repositório serão armazenadas em `/etc/apt/sources.list.d/bitmask.list`.

#### Instale no Wheezy (Debian 7)

Habilite `wheezy-backports` como fonte do software. 

	echo "deb http://deb.bitmask.net/debian wheezy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Instale no Jessie (Debian 8)

	echo "deb http://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Instale no Jessie usando a rede de anonimato Tor:

	sudo apt-get install apt-transport-tor
	echo "deb tor://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
	curl https://dl.bitmask.net/apt.key | sudo apt-key add -
	sudo apt-get update
	sudo apt-get install bitmask leap-keyring

#### Desinstale

	sudo apt-get remove bitmask leap-keyring
	sudo apt-key del 0x1E34A1828E207901
	sudo rm /etc/apt/sources.list.d/bitmask.list
	sudo apt-get update

### Pacote independente

O pacote independente do Bitmask deve funcionar em versões recentes das distribuições do GNU/Linux derivadas do Debian (Mint, Ubuntu, Elementary, etc.). Lembre-se que você é quem deve se encarregar de manter o software atualizado. 

Para obter o pacote independente, determine o tipo de núcleo do seu sistema operacional. Isso pode ser feito com o comando: `uname -m`.

#### 64 bits

Se a saída desse comando for 'x86_64' ou 'amd64', baixe a versão mais recente disponível em [https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.gz](https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.gz) e a assinatura OpenPGP de [https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.gz.asc](https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.gz.asc). 

Os seguintes comandos vão baixar e verificar a autenticidade do pacote.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc
	gpg --verify Bitmask-linux64-latest.tar.bz2.asc Bitmask-linux64-latest.tar.bz2

Se na saída estiver escrito "Assinatura correta", descompacte o pacote com este comando:

	tar xfj https://dl.bitmask.net/client/GNU/Linux/Bitmask-GNU/Linux64-latest.tar.bz2

#### 32 bits

Se a saída desse comando for 'i686' ou 'i386', baixe a versão mais recente disponível em [https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.gz](https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.gz) and its OpenPGP signature from [https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.gz.asc](https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.gz.asc). 

Os seguintes comandos vão baixar e verificar a autenticidade do pacote.

	gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2
	curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc
	gpg --verify Bitmask-linux32-latest.tar.bz2.asc Bitmask-linux32-latest.tar.bz2

Se na saída estiver escrito "Assinatura correta", descompacte o pacote com este comando:

	tar xfj Bitmask-GNU/Linux32-latest.tar.bz2

## Usando Bitmask pela primeira vez

Quando iniciar o Bitmask pela primeira vez, você terá que configurar Riseup como seu provedor de LEAP. Estes passos serão seu guia ao longo do processo.

### Crie uma conta Riseup baseada no LEAP

![1º passo](Bitmask-1.png)

Selecione _Sign up for a new account_ e aperte *Next*.

![2º passo](Bitmask-2.png)

Selecione _Configure a new provider_ e preencha "riseup.net". Depois, aperte *Check*.

![3º passo](Bitmask-3.png)

O Bitmask precisa se certificar que riseup.net é um provedor válido. Depois, aperte *Next* para continuar. Se houver algum problema neste passo, consulte a seção de resolução de problemas desta página.

![4º passo](Bitmask-4.png)

Se tudo correr bem, você verá essa tela. Aperte *Next* em seguida.

![5º passo](Bitmask-5.png)

O Bitmask precisa se certificar que pode se conectar com seguraça a riseup.net. Depois, aperte *Next* para continuar. Se houver algum problema neste passo, consulte a página de [[troubleshooting]].

![6º passo](Bitmask-6.png)

O próximo passo é definir um nome de usuário e senha para sua conta. Não os perca por nada.

Você não vai poder escolher seu nome de usuário riseup.net atual. Assim, evitam-se possíveis conflitos entre o sistema atual e o nome. Não se preocupe, você poderá recuperar seu nome de usuário mais tarde.

![7º passo](Bitmask-7.png)

Mensagem de confirmação. Aqui você pode fazer o Bitmask memorizar seu nome de usuário e senha; se o fizer, anote-os também. Aperte *Next* para continuar!

![8º passo](Bitmask-8.png)

Marque _Encrypted Internet_ e aperte _Connect_. Aproveite o serviço de VPN do Riseup. Oba!

## Resolução de problemas

Consulte a [[seção de _Resolução de problemas_ -> troubleshooting]].
