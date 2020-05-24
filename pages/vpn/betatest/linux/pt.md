@title = "RiseupVPN para Linux"
@this.alias = '/vpn/linux'

## Requisitos técnicos

Atualmente, a RiseupVPN só está disponível para Linux com `snap`. Se você usa Ubuntu, esse programa já vem instalado. Senão, execute:

```
sudo apt install snapd
```

Até agora, a RiseupVPN foi testada no **Ubuntu LTS** e no **Debian Stable**. Se a sua versão for outra, talvez funcione, talvez não.

## Instalação

Busque por **RiseupVPN** em **Programas** ou clique no link abaixo:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Abrir a RiseupVPN em Programas
</a>

Se o link acima não funcionar, você também pode instalar a VPN pela linha de comando:

```
sudo snap install --classic riseup-vpn
```

## Resolução de problemas

### Encerramento forçado

Se algo parar de funcionar, use os seguintes comandos e tente novamente:

```
sudo pkill -e -f riseup-vpn
sudo riseup-vpn.bitmask-root firewall stop
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```

Esses comandos garantem o encerramento de todos os processos da RiseupVPN, a remoção de todas as regras de saída do firewall e a limpeza do arquivo PID.

### Não inicializa

Caso o ícone do lançador não funcione, você pode iniciar a RiseupVPN a partir da linha de comando e, assim, identificar o problema:

```
riseup-vpn.launcher
```

Qualquer erro na inicialização será exibido no terminal.

### Experimente a versão de desenvolvimento

Para nos ajudar a testar uma versão de desenvolvimento, pré-lançamento, da RiseupVPN, instale-a usando o comando abaixo:

```
sudo snap install --classic --edge riseup-vpn
```

### Apague o arquivo PID

Pode ser que a RiseupVPN não consiga iniciar por ter detectado outra versão já em execução.

Se encontrar esse erro, use os seguintes comandos:

```
sudo pkill -e -f riseup-vpn
test -f ~/.config/leap/systray.pid && rm -v ~/.config/leap/systray.pid
```
