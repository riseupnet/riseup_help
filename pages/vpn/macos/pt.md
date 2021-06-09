@title = "RiseupVPN para macOS"
@toc = true
@this.alias = '/vpn/macos'

## Requisitos técnicos

A RiseupVPN foi testada no Sierra e no High Sierra.

## Instalação

<a class="btn btn-default btn-lg" href="https://downloads.leap.se/RiseupVPN/osx/RiseupVPN-OSX-latest.dmg"><i class="fa fa-download"></i> Baixe a RiseupVPN para macOS</a>

Após salvar o arquivo, dê um duplo clique em <code>RiseupVPN-OSX-latest.dmg</code> para instalar a RiseupVPN.

## Resolução de Problemas

### Relatório de Erros e Solicitação de Ferramentas

A RiseupVPN é construída utilizando um programa de software livre chamado <b>bitmask-vpn</b>.

**Passo 1:** [[Pesquise para ver => https://0xacab.org/leap/bitmask-vpn/issues]] se o bug já foi relatado.

**Passo 2:** [[Registre uma conta => https://0xacab.org/users/sign_in]] em [[0xacab.org => https://0xacab.org]] e faça o login.

**Passo 3:** Crie um [[novo relatório de bug ou solicitação de ferramenta => https://0xacab.org/leap/bitmask-vpn/issues/new]].

Por favor, inclua as seguintes informações em seu relatório de bug:

* Passos para reproduzir o bug
* Qual o comportamento esperado e o que você vê
* Uma captura de tela se for algo visual
* Sua versão do macOS
* Os registros do programa

### Pegue os registros

Existem três arquivos de registro, cada um para um diferente componente do cliente:

* O registro systray: `/Users/<your user>/Library/Preferences/leap/systray.log`
* O helper privilegiado: `/Applications/RiseupVPN.app/Contents/helper/helper.log`
* O processo openvpn: `/Applications/RiseupVPN.app/Contents/helper/openvpn.log`

Ao relatar um bug, é muito importante incluir os arquivos de registro.

### Teste uma versão de desenvolvimento

Se você quer nos ajudar a testar uma versão de desenvolvimento e pré-lançamento da RiseupVPN, você pode fazer o download das [[nightly builds => https://0xacab.org/leap/bitmask-vpn/-/jobs/artifacts/master/download?job=vendorize]].

## Código-fonte
Os clientes da RiseupVPN são baseados no software de código aberto Bitmask. O código para o cliente de macOS pode ser encontrado [[aqui => https://0xacab.org/leap/bitmask-vpn]].
