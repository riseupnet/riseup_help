@title = "Higiene de mensagens"
@toc = true
@summary = "Dicas simples para enviar e-mails e mensagens com mais segurança"

# Nunca confie no endereço remetente

A principal razão pela qual e-mails são a maior fonte de ataques a organizações é que não há como verificar a identidade do endereço remetente.

Repetindo: qualquer pessoa pode falsificar o endereço remetente e fazer parecer que uma mensagem tem outra origem qualquer.

Com remetentes difíceis de verificar, sua caixa de entrada torna-se uma fonte comum de **ataques de phishing** e **ataques de malware**.

* Um **ataque de phishing** ocorre quando uma pessoa envia um e-mail dizendo ser alguém que não é, ou de alguma entidade à qual não pertence, com o objetivo de obter informações suas. São informações sigilosas como CPFs, dados bancários, senhas.
* Um **ataque de malware** ocorre quando tentam enganar você para instalar programas maliciosos no seu computador, abrindo um anexo ou um link.

Geralmente, qualquer atividade inesperada no seu e-mail deve ser encarada com desconfiança. Suspeite de mensagens que pedem para você tomar alguma ação, como clicar em um link, abrir um anexo ou responder à mensagem com informações pessoais - mesmo que o endereço remetente seja conhecido!

Se alguém invadiu sua conta, você talvez veja mensagens de resposta estranhas, itens enviados a mais, novas pastas e filtros sendo criados ou outras mudanças de configuração. E-mails ou atividade de conta suspeitos devem ser relatados à assistência técnica, caso em que sua senha deve ser alterada.

# Fuja de links em e-mails

Links, normalmente de aparência inocente ou mesmo ocultos na mensagem, são a principal estratégia de ataque para roubo de dados e sequestro de dispositivos.

A melhor atitude é nunca clicar em links contidos em e-mails. Se você tiver que abrir um link, verifique se:

* Você esperava esse e-mail? Mesmo que o endereço remetente pareça pertencer a uma pessoa conhecida, é preciso ter muito cuidado com e-mails inesperados.
* É possível digitar o link manualmente em vez de clicar? O que você vê escrito pode não ser o destino verdadeiro. Nomes de domínio podem conter "homógrafos", isto é, caracteres distintos, mas semelhantes (p.ex. o número "0" e o "O" maiúsculo, ou letras correspondentes entre os conjuntos de caracteres latino e cirílico). Aquele link que parece ser <https://riseup.net> pode apontar, na verdade, para um site forjado <%= '<a href="https://riseuρ.net">https://riseuρ.net</a>' %> (o segundo link contém a letra grega equivalente a "p"). O jeito mais garantido de evitar esse ataque é nunca copiar URLs de fontes inseguras e sempre digitá-los diretamente na barra de endereços.
* Você reconhece o domínio? Na maioria dos programas de e-mail, assim como na web, passar o cursor sobre um link exibe o URL-destino. Se for um endereço inesperado ou desconhecido, confira com a pessoa que enviou a mensagem se ela é legítima. Um link deve sempre começar com "https://"; se começar com "data://", então com certeza se trata de um ataque de phishing.

Nunca abra links ou arquivos em e-mails suspeitos ou de origem desconhecida. Ao contrário de pessoas que você conhece, gente desconhecida jamais mandaria um arquivo que você realmente precise. Se um link de origem desconhecida realmente contém informação útil, você poderá acessá-lo por um método mais confiável (por exemplo, buscando na internet).

# Nunca faça login após abrir um link

Se você de fato clicar em um link recebido via e-mail, é de suma importância não iniciar uma sessão no site aberto. Se o site pedir as suas credenciais, faça o seguinte:

1. Abra uma nova aba no navegador e digite o endereço do site manualmente.
2. Nessa nova aba, faça login.
3. Volte para o seu e-mail e clique novamente no link.
4. Quando ele carregar, você não deve precisar entrar de novo. Se precisar, provavelmente é porque a mensagem se trata de um ataque de phishing.

Esse cuidado protegerá você da maioria dos ataques de phishing.

# Fuja de anexos

Anexos em e-mails apresentam diversos riscos, inclusive de phishing. Não são protegidos contra visualização e edição entre recipientes, então não dá para ter certeza de que o documento que você envia é o mesmo que é recebido. Um servidor malicioso entre você e alguém que enviou um e-mail para você pode substituí-lo pelo programa ou arquivo que quiser, inclusive vírus ou outro tipo de malware. Além disso, anexos tendem a ser esquecidos nas caixas de entrada de quem recebe a mensagem, onde é mais difícil controlá-los. Por exemplo, se você preenchesse um formulário de compra usando seu cartão de crédito e o enviasse para uma loja em PDF, alguém que invadisse a sua conta de e-mail teria acesso aos dados do seu cartão de crédito enquanto o documento não fosse apagado do servidor.

Melhor que usar anexos é armazenar arquivos em um servidor e mandar links para os documentos em vez dos documentos em si. Idealmente, esses links levariam a locais protegidos por senha ou outra forma de autenticação, ou seriam temporários e expirariam logo após serem usados. Esses links podem ser facilmente gerados em quase todos os sistemas de armazenamento de arquivos, sejam hospedados em servidores do seu escritório (como um servidor de arquivos Windows) ou na web (como Google Drive, Box ou Dropbox).

Para maior segurança, compartilhe arquivos criptografados via links temporários fazendo upload para <https://share.riseup.net>.

# Veja também

* [Surveillance Self-Defense / Como evitar ataques de Pesca (Phishing)](https://ssd.eff.org/pt-br/module/como-evitar-ataques-de-pesca-phishing)
* [Security Education Companion / Phishing and Malware](https://sec.eff.org/topics/phishing-and-malware)
* [Security in-a-Box / Protect your device from malware and phishing attacks](https://securityinabox.org/en/guide/malware/)
* [Security in-a-Box / Keep your digital communication private](https://securityinabox.org/en/guide/secure-communication/)
* [Security Planner / Spot Suspicious Emails](https://securityplanner.org/#/tool/spot-suspicious-emails)
