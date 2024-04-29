@title = "RiseupVPN para Linux"

## Requisitos técnicos

Para usar o serviço de VPN da Riseup, você precisará instalar o programa chamado RiseupVPN. No Linux, ele está disponível ou como um `snap`, ou como um pacote no Debian Stable.

A RiseupVPN atualmente é testada no **Ubuntu LTS** (18.04) e no **Debian Stable**. Se você tiver um lançamento diferente, pode ou não funcionar.

## Instalação do Snap

Se você usa Ubuntu, o programa snap já está instalado. Caso contrário, execute:

```
sudo apt install snapd gnome-software-plugin-snap
```

Então, procure por **RiseupVPN** no **Software Center** ou clique nesse link:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Open RiseupVPN in Software Center
</a>

Se o link acima não funcionar, você também pode instalar pela linha de comando:

```
sudo snap install --classic riseup-vpn
```
Se você receber um erro dizendo que "python" está faltando em `/usr/bin/env`, você precisa instalar o Python. Esse é o caso, por exemplo, no Lubuntu, pelo menos desde a versão 19.04.

## Instalação do Pacote

Execute os seguintes comandos em um terminal para instalar o pacote Debian Stable:

       sudo apt install riseup-vpn

## Resolução de problemas

### Relatório de Erros e Solicitação de Ferramentas

A RiseupVPN é construída utilizando um programa de software livre chamado <b>bitmask-vpn</b>.

**Passo 1:** [[Pesquise para ver => https://0xacab.org/leap/bitmask-vpn/issues]] se o bug já foi relatado.

**Passo 2:** [[Registre uma conta => https://0xacab.org/users/sign_in]] em [[0xacab.org => https://0xacab.org]] e faça o login.

**Passo 3:** Crie um [[novo relatório de bug ou solicitação de ferramenta => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Por favor, inclua as seguintes informações em seu relatório de bug:

* Passos para reproduzir o bug
* Qual o comportamento esperado e o que você vê
* Uma captura de tela se for algo visual
* Sua distribuição do Linux e sua versão
* O registro do programa

### Pegue o registro

O registro da RiseupVPN está localizado em sua pasta home:

```
~/.config/leap/systray.log
```

Ao relatar um bug, é muito importante incluir o arquivo de registro.

### Encerramento forçado

Se algo parar de funcionar, execute esse comando e tente de novo    :

```
sudo pkill -e -f riseup-vpn
```

### Não inicializa

Caso o ícone do lançador não funcione, você pode rodar a RiseupVPN a partir da linha de comando e, assim, identificar o problema:

```
/snap/bin/riseup-vpn.launcher
```

Qualquer problema na inicialização será exibido no terminal.

### Teste uma versão de desenvolvimento

Para nos ajudar a testar uma versão de desenvolvimento e pré-lançamento da RiseupVPN, instale-a usando o seguinte comando:

```
sudo snap install --classic --beta riseup-vpn
```

### Remova o arquivo PID

Às vezes a RiseupVPN pode não conseguir iniciar se achar que outra versão já está rodando.

Se você receber esse erro, execute esses comandos:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

## Código-fonte
Os clientes da RiseupVPN são baseados no software de código aberto Bitmask. O código para o cliente de Linux pode ser encontrado [[aqui => https://0xacab.org/leap/bitmask-vpn]].
