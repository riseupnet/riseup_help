@title = 'Maio'

## Nossa Declaração sobre Segurança

Se quiser atualizações sobre a interação de Riseup quanto aos aparatos de vigilância do Estado, vá para:
https://help.riseup.net/pt/canary

Nós o estaremos atualizando a cada três meses, em média.

Atualmente, ele afirma:
 
Até o dia 21 de abril de 2014, Riseup não recebeu Cartas de Segurança Nacional ou ordens judiciais FISA, e não fomos sujeitos a qualquer ordem de silêncio por um tribunal FISA. Riseup nunca colocou "portas dos fundos" em nossos programas e não recebeu nenhuma requisição para fazer isto. Riseup nunca revelou qualquer comunicação de quem das pessoas que usam nossos serviços a terceiros.

Em relação às apreensões de servidores, houve um incidente amplamente relatado, onde o FBI apreendeu um dos servidores de Riseup em abril de 2012. Isto aconteceu em Nova Iorque. A máquina era criptografada e não continha dados de usuárias. O servidor foi devolvido, mas não foi colocado para funcionar de novo. Além do que aconteceu, no dia 21 de abril de 2014, Riseup afirma que não teve nenhum hardware apreendido ou levado por terceiros.


## Yahoo e listas

Você deve ter visto algumas rejeições de yahoo.com e aol.com. Isso se deve às mudanças na política destas empresas. Eles publicaram um registro DMARC (uma tecnologia anti-spam) que efetivamente diz "se algum servidor que não seja o nosso servidor oficila enviar um email com um remetente usando um endereço yahoo.com (ou aol.com), assume-se que o email é spam e ele é rejeitado". O registro DMARC é também usado por outros sites (como hotmail.com, comcast.net e muitos outros) para decidir o que fazer quando um email chega.

O problema aqui é que softwares de listas de emails, como lists.riseup.net, retransmitem mensagens para outros. Então quando um usuário de yahoo.com ou aol.com manda um email para a lista e este é redistribuído (com o endereço yahoo.com ou aol.com ainda como o remetente), o que ocorre é que os servidores que recebem emails entendem que "esta mensagem não foi enviada por um servidor do yahoo ou aol, é um spam e deve ser rejeitado!" e retornam a mensagem. Este é o motivo pelo qual você deve ter visto muitas mensagens retornadas, não só de yahoo.com ou aol.com mas de outros sites também.

Se quiser uma explicação completa, veja este link em inglês http://jrl.guru/Email/yahoobomb.html

A coisa mais fácil para arrumar isto é yahoo e aol mudarem sua política.

Mas enquanto isso não ocrre, isto é o que Riseup está fazendo:

* Visando diminuir o estrago, estamos bloqueando todos os remetentes para lists.riseup.net que usam endereços de yahoo.com ou aol.com. Quando enviarem, os remetentes de yahoo.com e aol.com receberão imediatamente uma mensagem de erro explicando o problema. Isto é ruim para os remetentes, mas vai prevenir que haja devoluções em massa e saídas de listas por causa dessas devoluções.
* Nós recomendamos a todos que mudem de yahoo.com e aol.com para um provedor de emails que proteja sua privacidade e não impossibilite o uso de listas de emails.
* Estamos investigando outras maneiras para contornar este problema, esperamos resolvê-lo o quanto antes.


## Dinheiro!

O dinheiro o está deixando para baixo? Nós também. Se puder doar um pouco para Riseup, qualquer pequena quantia percorre um longo caminho para apoiar milhares de grupos e ativistas ao redor do mundo.
https://help.riseup.net/pt/donate

E, wepay, uma das formas pelas quais as pessoas podem doar para Riseup, parou de aceitar doações. Aqueles que tinham programado doações recorrentes com eles, seria incrível se pudessem programar outra forma de pagamentos recorrentes. Gratidão!

