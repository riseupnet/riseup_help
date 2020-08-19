@title = 'Garantia do canário'
@nav_title = 'Canário'
@this.alias = '/canary'
@toc = false

![](canarypronounce.png)

#### _*substantivo*_

***1...*** Um pequeno pássaro canoro da família dos fringilídeos, _Serinus canaria domestica_, nativo de ilhas do Atlântico Norte.

***2...*** Um mecanismo para testar a segurança de alguma coisa, remontando ao uso de canários em minas de carvão para detectar gases venenosos e prever colapsos. Quando o canário morria, era hora de sair da mina. Mais recentemente, alguns provedores de serviços on-line têm empregado o termo para se referir a uma declaração, atualizada regularmente, de que o provedor não foi sujeitado a certos processos legais. Se a declaração não for atualizada no tempo esperado, pode-se inferir que a garantia do canário não é mais válida.

![](canaryimg.jpg)

<pre>
<%= render :file => 'canary-statement-signed.txt', :type => :raw %>
</pre>

## Instruções de verificação

Você deve [[baixar a chave GPG do Riseup e verificar o identificador da chave => network-security/certificates#complete-verification]]. Então, siga estes passos para conferir a declaração:

1. Baixe a [[garantia do canário => /about-us/canary/canary-statement-signed.txt]] assinada.
1. Execute este comando em um terminal:

	```
	gpg --auto-key-retrieve --verify canary-statement-signed.txt
	```

1. A saída deve ser parecida com o seguinte (lembrando que a data será diferente, dependendo de quando a garantia foi assinada):

	```
	gpg: Signature made Mon 27 Jul 2020 07:57:58 PM -03
	gpg:                using RSA key 4E0791268F7C67EABE88F1B03043E2B7139A768E
	gpg:                issuer "collective@riseup.net"
	gpg: Good signature from "Riseup Treasurer <treasurer@riseup.net>" [unknown]
	gpg:                 aka "Riseup Networks <collective@riseup.net>" [unknown]
	gpg: WARNING: This key is not certified with a trusted signature!
	gpg:          There is no indication that the signature belongs to the owner.
	Primary key fingerprint: 4E07 9126 8F7C 67EA BE88  F1B0 3043 E2B7 139A 768E
	```

Confirme se a saída diz "Good signature" e se o ID da chave é o mesmo que você verificou [[aqui, mais cedo. => network-security/certificates#complete-verification]] Se o texto estiver diferente, as informações não são confiáveis.

A não ser que você tenha tomado medidas explícitas para construir um caminho seguro à chave da Riseup Collective, você deve ver uma mensagem de aviso similar a:

	```
	gpg: WARNING: This key is not certified with a trusted signature!
	gpg:          There is no indication that the signature belongs to the owner.
	```

Mesmo assim você ainda deve ver "Good signature”.