@title = 'Garantia do canário'
@nav_title = 'Canário'
@this.alias = '/canary'
@toc = false

![](canarypronounce.png)

#### _*noun*_

***_*1...*** Um pequeno pássaro canoro da família dos fringilídeos, _Serinus canaria domestica_, nativo de ilhas do Atlântico Norte.

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
	gpg: Assinatura feita Seg 30 Abr 2018 09:23:59 BRT 
	gpg:                  usando RSA chave ID 139A768E
	gpg: Assinatura correta de "Riseup Networks <collective@riseup.net>"
	```


Confirme se a saída diz "Assinatura correta" e se o ID da chave é o mesmo que você verificou [[aqui, mais cedo. => network-security/certificates#complete-verification]] Se o texto estiver diferente, as informações não são confiáveis.
