@nav_title = "Resolução de problemas"
@title = "RiseupVPN: resolução de problemas"
@summary = "Como resolver problemas da VPN de tecnologia LEAP"

## Conta

Os seguintes problemas com contas foram observados durante o período de teste Beta.

### Não consigo registrar meu nome de usuário / Alguém pegou meu nome de usuário.

Nossos novos serviços, de segurança reforçada, são baseados na plataforma [LEAP Encryption Access Project](https://leap.se). Esta tem uma insfraestrutura completamente nova e não é diretamente vinculada aos nossos serviços atuais de e-mail e listas. Você pode acessar esses novos serviços no endereço https://black.riseup.net.

Isso significa que você precisará criar uma nova conta para usar a VPN e outros futuros serviços. Mas para evitar possíveis colisões de nomes de usuário, "reservamos" todos os nomes de usuário atuais. Não se preocupe, mais tarde este ano você poderá migrar sua conta atual (inclusive seu nome de usuário) para nossos novos e muito mais seguros serviços. 

### Meu nome de usuário ou senha não funciona!

Veja a pergunta acima.

## Bitmask

Os seguintes problemas foram identificados em alguns ambientes.

### Não uso Debian ou Ubuntu. Como posso instalar o Bitmask?

Se você usa uma distribuição baseada no Debian (como CrunchBang) ou no Ubuntu (como Mint), instale o [pacote independente](#stand-alone-bundle) e conte-nos sua experiência ao instalar o Bitmask! Existe uma miríade de distribuições do GNU/Linux por aí, e não podemos testá-las todas. Se você conseguir instalá-lo, conte-nos, por favor... e se não conseguir, aguardamos ansiosamente seu feedback. De qualquer maneira, **o Bitmask deve funcionar em qualquer sistema GNU/Linux moderno**.

### Não consigo me conectar a nenhum/vários/alguns sites

Execute os seguintes comandos e dê uma olhada nas possíveis soluções.

#### Rode `sudo ip route` e procure pela linha começando com 'default'; 'tun0' é o valor após a palavra 'dev'

Há um defeito no pacote Network-Manager do Debian (versão de testes e instável). Se você usa esse pacote, provavelmente vai encontrar esse problema. Leia mais sobre ele em [Debian Bug #23755015 (em inglês)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=%23755015).

Uma gambiarra possível é

    sudo ip route del default
    sudo ip route add default via 10.42.0.1 dev tun0

#### Meu problema não está na lista acima... Que devo fazer agora?

A primeira coisa a fazer é descobrir a causa do problema; para conseguir essa informação, abra o terminal e execute o comando `bitmask --debug --logfile /tmp/bitmask.log`. Isso vai rodar o Bitmask em modo de depuração e armazenar a saída em um arquivo de texto, `/tmp/bitmask.log`. Se você tiver experiência, talvez consiga delimitar um pouco mais o problema. Se não, preencha um tíquete com o conteúdo do arquivo `/tmp/bitmask.log` e informe também qual é seu sistema operacional (Debian Wheezy, Mint 17, Ubuntu Trusty, etc.).

## Outros problemas

### Uma janela "_Configure Bitmask email Account_" aparece todas as vezes que abro o Thunderbird/Icedove

O pacote `xul-ext-bitmask` foi instalado. Ele não é uma dependência, mas um pacote sugerido, que contém uma extensão do Thunderbird/Icedove de suporte do LEAP como provedor de e-mail. Sinta-se livre para removê-lo; basta executar `sudo apt-get remove xul-ext-bitmask` e reiniciar seu cliente de e-mail Thunderbird/Icedove.

....
