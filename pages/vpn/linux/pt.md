@title = "RiseupVPN para Linux"
@this.alias = '/vpn/linux'

## Requisitos técnicos

Atualmente, a RiseupVPN só está disponível para Linux com `snap`. Se você usa Ubuntu, o snap já está instalado. Senão, execute:

```
sudo apt install snapd
```

Até agora, a RiseupVPN foi testada no **Ubuntu LTS** e no **Debian Stable**. Se a sua versão for outra, talvez funcione, talvez não.

## Instalação

Busque por **RiseupVPN** no **Software Center** ou clique no link abaixo:

<a class="btn btn-default btn-lg" href="snap://riseup-vpn">
  <i class="fa fa-reply-all"></i>
  Abrir a RiseupVPN no Software Center
</a>

Se o link acima não funcionar, você também pode instalar pela linha de comando:

```
sudo snap install --classic riseup-vpn
```

## Resolução de problemas

### Encerramento forçado

Se a RiseupVPN travar ou sua conexão de rede estiver bloqueada, você pode forçar o encerramento do programa e desabilitar o firewall com os seguintes comandos:

```
sudo pkill -e -f riseup-vpn
sudo /snap/bin/riseup-vpn.bitmask-root firewall stop
```

### Não inicializa

Caso o ícone do lançador não funcione, você pode rodar a RiseupVPN a partir da linha de comando e, assim, identificar o problema:

```
/snap/bin/riseup-vpn.launcher
```

Qualquer problema na inicialização será exibido no terminal.

### Teste a versão de desenvolvimento

Para nos ajudar a testar uma versão de desenvolvimento, pré-lançamento, da RiseupVPN, instale-a usando o seguinte comando:

```
sudo snap install --classic --edge riseup-vpn
```
