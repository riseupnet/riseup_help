@title = "RiseupVPN para windows"
@toc = true
@this.alias = '/vpn/windows'

## Dependências

A RiseupVPN foi testada no windows 7 e windows 10.

## Instalação

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/windows/RiseupVPN-win-latest.exe"><i class="fa fa-download"></i> Baixe a RiseupVPN para windows</a>


Com o arquivo salvo, dê dois cliques em <code>RiseupVPN-win-latest.exe</code> para instalar a RiseupVPN.

## Resolução de problemas

### Relatos de falha e Pedidos de funcionalidade

RiseupVPN é construído sobre um programa de código aberto chamado <b>bitmask-vpn</b>.

**1º Passo:** [[Veja => https://0xacab.org/leap/bitmask-vpn/issues]] se o bug já foi reportado.

**2º passo** [[Registre uma conta => https://0xacab.org/users/sign_in]] with [[0xacab.org => https://0xacab.org]] e faça login.

**3º passo** Crie um [[relato de falha (bug report) ou pedido de funcionalidade (feature request) => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Por favor inclua as seguintes informações no seu relato de falha:

* Passos para reproduzir o bug
* O que é o comportamento esperado e o que você constata
* Uma imagem da tela se for algo visual
* Sua versão do windows
* Os logs do programa

### Ache os logs

Há três arquivos de log, cada um para um componente diferente do cliente:

* O log systray: `C:\Users\<your user>\AppData\Local\leap\systray.log`
* O helper privilegiado: `C:\Program Files\RiseupVPN\helper.log`
* O processo openvpn: `C:\Program Files\RiseupVPN\openvp.log`

Ao reportar uma falha é muito útil incluir os arquivos de log.

### Vazamentos de DNS

Acreditamos que não há vazamentos de IP ou de DNS na RiseupVPN para
windows, mas isso ainda não foi extensamente testado em prática.
Diferente do Mac ou linux, não há firewall no windows.

Se você achar qualquer tipo de vazamento, estamos muito interessados em
ouvir sobre isso.

### Teste uma versão pré-lançamento

Se você quiser nos ajudar a testar uma versão pré-lançamento em
desenvolvimento da RiseupVPN, pode baixar as [[nightly builds => https://0xacab.org/leap/bitmask-vpn/-/jobs/artifacts/master/download?job=vendorize]].

## Código-fonte

Os clientes da RiseupVPN são baseados no software de código aberto Bitmask. O código para o cliente de Windows pode ser encontrado [[aqui => https://0xacab.org/leap/bitmask-vpn]].
