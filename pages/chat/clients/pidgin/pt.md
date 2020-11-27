@title = 'Pidgin'

## Sobre o Pidgin

![logopidgin](logo.pidgin.png)

O Pidgin é o mensageiro instantâneo mais popular para GNU/Linux, Windows e macOS. Você pode baixar o Pidgin do site: https://pidgin.im/download. Para Mac, dê uma olhada no [[Adium]], a versão nativa do Pidgin para Mac.

## Configurando uma conta

Quando você executar o Pidgin pela primeira vez, pressione o botão `Adicionar...` para adicionar uma conta.

(1) Na aba `Básico`, acerte estas configurações:

![newaccountbasictab](new-account-basic-tab.png)

- `Protocolo`: XMPP.
- `Nome de usuário`: seu nome de usuário Riseup.
- `Domínio`: riseup.net.
- `Senha`: sua [[senha => riseup-password]].

Opcionalmente, use seu nome como alias local e escolha um ícone para a sua conta. Outras pessoas verão esse ícone nos clientes de XMPP delas.

## Usando OTR

Veja o tutorial sobre o protocolo [[otr]] para detalhes sobre a utilização da criptografia ponta a ponta com o Pidgin.

## Garantindo a segurança do Pidgin no GNU/Linux

Para ainda mais segurança em sistemas Linux, recomendamos que você faça o seguinte:

- Copie `usr.bin.pidgin` para `/etc/apparmor.d/usr.bin.pidgin`.
  * [usr.bin.pidgin for Ubuntu 14.04](https://bazaar.launchpad.net/~apparmor-dev/apparmor-profiles/master/view/head:/ubuntu/14.04/usr.bin.pidgin)
- Reinicie o AppArmor.
`sudo /etc/init.d/apparmor restart`
- Reinicie o Pidgin.

## Tor com o Pidgin

Para configurar o Pidgin para usar o Tor, você precisa alterar as suas configurações de conta:

Primeiro, selecione `Modificar configurações de conta`...

![pidginmodifyaccount](pidgin-modify-account.png)

Então, clique na aba `Avançado` e defina os seguintes valores:

- `Segurança de conexão`: Requerer criptografia
- `Conectar porta`: 5222
- `Conectar servidor`: 4cjw6cwpeaeppfqz.onion
- `Proxy de transferência de arquivos`: proxy.riseup.net

Em seguida, clique na aba `Proxy`...

![pidginmodifyaccountproxy](pidgin-modify-account-proxy.png)

Defina o tipo de proxy como `Socks5`, configure o hospedeiro e a porta como na imagem, e informe seu nome de usuário e senha.

