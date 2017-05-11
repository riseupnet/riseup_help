@title = 'Encrypted Email with OpenPGP'
@nav_title = 'Encrypted Email'

h2. O que é um email encriptado?

Usar emails encriptados é uma boa maneira de manter o conteúdo do seu email a salvo, mesmo que ele seja interceptado enquanto circula pela internet. Uma forma comum de encriptação é usando o OpenPGP (OpenPGP é uma especificação livre. PGP significa "Pretty Good Privacy" e é um programa proprietário; GPG significa "GNU Privacy Guard" e é um software livre). Existem muitos materiais na internet que podem te oferecer uma explicação detalhada sobre como a criptografia funciona. Para os nossos propósitos, temos três componentes que valem a pena serem entendidos; *chave pública*, *chave privada* e *senha* (ou frase-chave). 

Sua *chave pública* é, como diz o nome, disponível publicamente. As vezes as pessoas usam servidores de chaves para compartilhar chaves públicas e tornar o envio de emails usando criptografia mais fácil. Sempre que você quiser mandar um email encriptado você precisa ter a chave pública da destinatária. Similarmente, quando alguém quiser te mandar um email encriptado precisará ter sua chave pública.

Uma *chave privada* é conectada exatamente a uma chave pública. Sem uma chave privada, o conteúdo de uma mensagem criptografada é extremamente difícil de ser extraído. Na era dos supercomputadores nada é impossível, mas descriptografar uma mensagem sem ter a chave privada continua sendo extraordinariamente difícil! Sua chave privada é extremamente importante e deve sempre ser mantida em um local seguro.

Não entendeu como funciona? Temos as duas chaves: a pública e a privada. Imagine a mensagem como uma maleta com dois buracos para chaves: um buraco que só tranca e um que só destranca. A chave pública serve apenas para trancar e a chave privada apenas para destrancar. Assim, se a Maria quiser te mandar uma mensagem, ela pega a maleta, usa a sua chave privada para trancá-la e depois te envia a maleta trancada. Depois que ela trancou, só a sua chave privada consegue abrí-la! Sendo assim, só você vai conseguir destrancar e ver o que tem lá dentro. 

Sua *senha* não deve ser inventada por você mesma. O principal motivo para você não inventar suas próprias senhas é que você não conseguirá ser aleatória, por mais que tente (e isso não é culpa sua), tornando sua senha fácil para um computador adivinhar. [[Esta tirinha -> https://caioau.keybase.pub/senhas/xkcdptbr.png]] explica bem o caso. Para criar senhas fortes e aleatórias, use um método como o [[Dadoware -> https://github.com/thoughtworks/dadoware]]. Tudo o que você precisa para gerar senhas extremamente seguras é de um lápis e de pelo menos um dado, só isso. [[Aqui -> https://github.com/thoughtworks/dadoware/blob/master/livreto/dadoware-intro.pdf]] você encontra o guia de como usar e [[aqui -> https://github.com/thoughtworks/dadoware/blob/master/livreto/dadoware-lista.pdf]] a lista das palavras. Uma dica: use pelo menos 6 palavras na sua senha. Caso tenha problemas para memorizá-la, bole uma frase que use todas palavras ou anote as palavras num papel seguro até decorá-las (depois queime, rasgue e jogue fora).

h2. Como eu uso criptografia de email?

Existem três funções básicas que você pode executar usando GPG: *assinar*, *encriptar* e *verificar*.

*Assinar*: Quando você assina algo, você usa sua chave privada e sua senha para gerar um *bloco de assinatura* que é anexado ao item que você está assinando. Esse bloco de assinatura é gerado a partir de duas coisas: (1) um valor numérico computado a partir dos conteúdos da mensagem e (2) da sua chave privada.

*Verificar*: Quando uma pessoa recebe algo que foi assinado, ela pode verificar o arquivo (ou mensagem) que recebeu usando a chave pública com a qual ele foi encriptado. A chave pública pode ser baixada de um servidor de chaves ou enviada pelo remetente. Verificar uma chave nos garante duas coisas --> (1) a mensagem foi assinada por alguém que tem acesso à chave privada associada e (2) os conteúdos da mensagem não foram alterados durante o trajeto remetente-destinatário.

*Encriptando*: Para encriptar uma mensagem, você precisa da chave pública do destinatário. Você não precisa de uma senha nem mesmo de uma chave GPG própria para criptografar algo. Contudo, a maioria dos programas também irá encriptar qualquer coisa que você for enviar com sua própria chave pública. Se não fosse assim, ao encriptar uma mensagem, você não poderia mais lê-la. Uma vez encriptada, os conteúdos de um email não são mais disponíveis durante o tráfego. *Contudo, assunto, remetente e destinatário ainda são visíveis.*


h2. Posso enviar e receber emails criptografados usando a interface web do email do riseup?

É muito melhor para usuárias do riseup que queiram usar emails criptografados que utilizem um [[email/client]] (como o [[Thunderbird]] para enviar e receber emails, enquanto mantém sua chave privada armazenada localmente de forma segura. Entretanto, é possível fazer uso da extensão de navegador [[Mailvelope -> https://www.mailvelope.com/]], que possibilita a criptografia de emails com GPG no webmail.


h2. Quais são algumas limitações dos emails criptografados?

Comunicações criptografadas não te protegem de *vigilância das relações*, ou seja, o monitoramente das associações entre pessoas. Por exemplo, se o fimdoestado@riseup.net está mandando emails regularmente para a mariasilva@riseup.net, alguém que esteja interceptando a comunicação entre essas duas pessoas pode não saber *o que* estão discutindo, mas o simples fato de que essas duas pessoas estão se comunicando regularmente já é por si só uma informação muito útil. Além disso, o assunto da mensagem *não é criptografado* (não coloque "reunião secreta na casa da Maria sexta feira" como assunto!).

Assinar e verificar não garantem que o email foi de fato enviado pelo email associado à chave. Imitar o email de resposta (spoofing) é muito fácil. Então, alguém com o email agentedapf@yahoo.com.br poderia: (1) criar uma chave para mariasilva@riseup.net, (2) subir essa chave para um servidor de chaves públicos e (3) enviar um email a partir do agentedapf@yahoo.com.br que pareça que veio da mariasilva@riseup.net e que está assinado. Se você simplesmente baixar a chave pública e verificar a mensagem, aparecerá "boa assinatura de mariasilva@riseup.net" mesmo que a mensagem tenha vindo da agentedapf! É por isso que uma "rede de confiança" é tão importante (veja abaixo).


h2. Como posso verificar a identidade da dona da chave? 

Agora você já configurou sua criptografia para emails e está muito contente enviando e recebendo emails seguros. Mas como você sabe se está realmente se comunicando com a pessoa que pensa que está? É aí que as *impressões digitais das chaves* entram no jogo.

Cada chave pública tem uma *impressão digital* única. Essa impressão digital é gerada através de uma função de hash, que funciona como uma espécie de portal só de ida. Para uma entrada específica, existe *uma e apenas uma* saída correspondente. Assim como suas impressões digitais são únicas, também são as de qualquer chave pública específica. Por que isso é útil? Porque para termos certeza da integridade do processo, você precisa ter certeza de que quando recebe um email assinado da sua amiga mariasilva@riseup.net você está realmente recebendo um email da sua amiga Maria Silva. Existem dois (ou possivelmente três) jeitos de verificar isso:

	1. Você e Maria se encontram pessoalmente e Maria te dá uma cópia eletrônica da sua chave pública.
	2. Você e Maria se encontram pessoalmente e Maria te dá uma cópia da impressão digital da sua chave e você verifica se essa impressão digital confere com a da chave pública dela.
	3. (menos segura) Se você e Maria se conhecem muito bem e você reconhece a voz dela, Maria pode ler a impressão digital dela no telefone para você.

A impressão digital não é uma informação secreta -- qualquer pessoa pode gerar a impressão digital usando a chave pública.

h2. Como posso assinar uma chave e por que eu faria isso?

Indo para o próximo passo, digamos que você trocou suas chaves com Maria de um jeito seguro. Agora você está pronta e pode mandar emails para Maria de forma segura, sabendo que você está de fato trocando emails com ela (porque ela está assinando seus emails) e sabendo que os conteúdos da comunicação entre vocês estão a salvo de bisbilhoteiros (porque você está criptografando seus emails usando a cahve pública da Maria). Mas digamos que a Maria conhece a Rita numa atividade e Maria e Rita trocam suas chaves de maneira segura. Você conhece e confia na Maria, mas não conhece a Rita. Como você pode verificar que a chave da Rita é verdadeira sem ter que encontrá-la pessoalmente?

Entre no mundo da rede de confiança e na assinatura de chaves!

Uma vez que Maria verificou a chave da Rita de maneira segura, Maria pode *assinar a chave pública da Rita*. Assim, garantimos que a dona do email é a dona da chave. Se você confia na Maria para verificar com atenção chaves individualmente, então você pode ajustar no seu chaveiro (coleção das chaves públicas que você tem salvas) um nível de confiança na chave da Maria. Assim, se você não conheceu alguém pessoalmente para verificar sua chave mas a Maria sim, você pode estabelecer um nível de confiança para uma chave baseado no fato de que a Maria assinou essa chave.

Além disso, você pode organizar uma *festa de assinatura de chaves* para encorajar suas amigas e colegas a criar, trocas e assinar suas chaves. Essa é uma ótima oportunidade para verificar a identidade das pessoas que você não se encontrou mas que pessoas de sua confiança se encontraram. Uma dica para essa festa de assinatura de chaves é você ou alguma amiga fazer uma mini oficina para ajudar as pessoas que ainda não têm suas chaves, promovendo assim a autonomia das pessoas. É uma experiência muito gratificante e que traz muito aprendizado a todas envolvidas, experimente fazer!

h2. Vocês têm mais alguma dica sobre criptografia de emails?

Que bom que você perguntou!

* *SALVE* sua chave privada num disco rígido criptografado -- Isso protege a integridade da chave no caso do seu computador ser roubado, perdido ou confiscado.
* *NÃO* compartilhe sua chave privada com nenhuma pessoa nem a salve num computador público.
* *USE UMA SENHA FORTE* - Sua senha é sua última defesa contra o uso não-autorizado da sua chave. Não estrague todo esse trabalho usando uma senha fraca, por favor. Use um gerador de senhas como o KeePassX ou um método como o Dadoware e evita inventar suas próprias senhas.
* *USE ASSUNTOS GENÉRICOS* - Os assuntos dos emails não são encriptados. Assim, você sempre deve usar um assunto bem genérico nas suas comunicações criptografadas. 
* *ORGANIZE UMA FESTA DE ASSINATURA DE CHAVES* - Encorage suas amigas a criar chaves GPG e assinar as chaves umas das outras.
* *MANDE EMAILS CRIPTOGRAFADOS MESMO QUANDO OS ASSUNTOS NÃO FOREM TÃO IMPORTANTES* - Isso é essencial! Se você só usar emails encriptados para conversas que envolvam conteúdo sensível, será gerada uma quantidade muito pequena de tráfego para ser analisada. Se todo mundo usasse emails criptografados para todas comunicações, mesmo quando decidinco sobre qual sabor de pizza pedir, a quantidade de tráfego para ser analisada seria muito maior, seria até difícil saber por onde começar! Além disso, encriptando tudo você levantará menos suspeitas do que se encriptar apenas esporadicamente suas mensagens, pois dará a entender que está tratando de algo mais sensível.

h2. Como eu configuro a criptografia de emails com OpenPGP no meu computador?

Por favor, leia:

* [[LEIA ISSO PRIMEIRO -> gpg-best-practices]]
* [[Gerenciando chaves OpenPGP -> gpg-keys]]
* [[Usando Enigmail+Thunderbird -> enigmail]]
