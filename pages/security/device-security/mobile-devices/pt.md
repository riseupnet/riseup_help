@title = "Segurança de aparelhos móveis"
@nav_title = "Aparelhos móveis"
@toc = true

Qual aparelho móvel é melhor para mim?
==============================================

O dispositivo móvel ideal para você depende da sua situação:

* **Alto risco**: Você suspeita que pode ser alvo de um governo ou empresa de vigilância profissional.
* **Médio risco**: Você não é ativamente alvo de perseguição, mas preferiria um dispositivo que não fosse fácil de invadir tendo-se acesso físico a ele.
* **Baixo risco**: Você não usa seu aparelho móvel para trocar informações confidenciais.

Alto risco
-----------------------------------------------

Se você pertencer à faixa de alto risco, **não use seu telefone para assuntos confidenciais**. Isso porque todos os telefones celulares possuem um "modem de banda-base", que se conecta à rede da operadora ("dados móveis"). Esses modems são proprietários e repletos de falhas de segurança que podem ser exploradas remotamente. Se comprometido, o modem de banda-base pode ser usado para monitorar sua comunicação e extrair seus dados pessoais.

Como alternativa a um telefone celular, você pode comprar um tablet que tenha apenas suporte a Wi-Fi e não possa se conectar à rede celular. Esses dispositivos não possuem um modem de banda-base e são muito mais difíceis de atacar remotamente. Tendo um aparelho com somente Wi-Fi, você ainda poderá se conectar à rede celular comprando um "hotspot móvel" separadamente.

ATENÇÃO: Modo avião não é suficiente. Dependendo do dispositivo, o modem de banda-base provavelmente continua a receber energia em modo avião, ficando aberto a ataques.

São alguns dos dispositivos de apenas Wi-Fi recomendados:

* [[Pixel C => https://en.wikipedia.org/wiki/Pixel_C]] ou [[Pixelbook => https://en.wikipedia.org/wiki/Google_Pixelbook]], do Google.
* [[iPad => https://en.wikipedia.org/wiki/IPad]], da Apple, mas apenas os modelos **sem suporte a dados móveis**.

Médio risco
-----------------------------------------------

Você guarda informações confidenciais no seu aparelho que preferiria que não fossem roubadas por criminosos, governos ou fofoqueiros? Claro que sim, todo mundo.

Nesse caso, você precisa dificultar uma possível invasão ao seu dispositivo caso ele seja roubado.

A melhor opção, infelizmente, é comprar um dispositivo do Google ou da Apple. O hardware fabricado por essas empresas é muito mais seguro do que de outras e são atualizados mais frequentemente. Entretanto, mesmo esses aparelhos podem ser invadidos se estiverem desbloqueados ou se o ataque perpetrado for sofisticado.

São alguns dos dispositivos recomendados:

* [[Pixel => https://en.wikipedia.org/wiki/Google_Pixel]], do Google.
* [[iPhone or iPad => https://en.wikipedia.org/wiki/IPhone]], da Apple (iPhone 4S ou posterior é requerido para que o dispositivo seja criptografado)

Baixo risco
------------------------------------------------

Você deixa seu celular por aí, completamente desbloqueado? Meus parabéns, você está aceitando a realidade de que hardware móvel não é muito seguro.

Entretanto, você e as pessoas com quem se comunica ainda terão muitos benefícios se seguirem as demais dicas de segurança móvel nesta página.

Mantenha seu aparelho junto de você
===============================================

É uma boa ideia manter seu dispositivo sempre fisicamente próximo. De outro modo, há várias maneiras em que ele poderá ser invadido, ter seus dados roubados e software instalado para monitorar suas atividades futuras.

A vulnerabilidade do seu dispositivo depende se ele tem o "hardware recomendado", se a [[criptografia do aparelho => device-encryption]] está ativada e se ele está protegido com senha ou PIN.

**Probabilidade de um ataque ao seu aparelho ser bem-sucedido:**

<table class="table">
<tr>
  <th>Seu dispositivo</th>
  <th>Ataque sofisticado</th>
  <th>Ataque hábil</th>
  <th>Ataque casual</th>
</tr>
<tr>
  <td>Hardware recomendado + criptografia + senha</td>
  <td>BAIXA</td>
  <td>MUITO BAIXA</td>
  <td>NENHUMA</td>
</tr>
<tr>
  <td>Hardware recomendado + senha</td>
  <td>MÉDIA</td>
  <td>BAIXA</td>
  <td>MUITO BAIXA</td>
</tr>
<tr>
  <td>Hardware normal + criptografia + senha</td>
  <td>ALTA</td>
  <td>MÉDIA</td>
  <td>BAIXA</td>
</tr>
<tr>
  <td>Hardware normal + senha</td>
  <td>MUITO ALTA</td>
  <td>ALTA</td>
  <td>MÉDIA</td>
</tr>
<tr>
  <td>Desbloqueado</td>
  <td>INEVITÁVEL</td>
  <td>INEVITÁVEL</td>
  <td>INEVITÁVEL</td>
</tr>
</table>

Tipos de ataque:

* **Ataques sofisticados** são perpetrados por grandes governos e multinacionais especializadas em invasão de celulares protegidos por senha.
* **Ataques hábeis** são realizados pela polícia e empresas de desbloqueio de celulares locais.
* **Ataques casuais** são feitos por especialistas em tecnologia habilidosos, sem equipamento especializado.

Se você tiver se afastado do dispositivo e suspeitar que ele possa ter sido invadido, faça um backup dos seus dados e restaure os padrões de fábrica (ou considere comprar um novo aparelho).

Use o Signal
================================================

Baixe o Signal para:

<%= render partial: 'signal_android' %> <%= render partial: 'signal_ios' %>

O **Signal** é um aplicativo de mensagens livre que se pode usar como alternativa segura ao app de mensagens padrão, que vem instalado no seu dispositivo. Funciona de maneira similar ao WhatsApp ou Telegram, mas com muito mais segurança.

Por que usar o Signal?

* Sua operadora mantém registros de todos os SMS que você envia. Com o Signal, ela não tem acesso às suas mensagens ou padrão de comunicação.
* É relativamente fácil invadir um celular e roubar o número do telefone. Com o Signal, você recebe um alerta para essa possibilidade com uma notificação de que o "número de segurança" de alguém mudou. Isso também acontece quando uma pessoa compra um novo aparelho.
* Também se pode fazer com o Signal ligações altamente seguras. Sua operadora mantém registros dos números para os quais você liga, dos quais recebe ligações e da duração de cada chamada. Com o Signal, ela não tem nenhuma dessas informações. Desde que seu dispositivo não seja comprometido, o conteúdo das ligações também permanece confidencial.
* Outros mensageiros "seguros", como WhatsApp, Telegram ou Wire, apresentam muitos problemas se comparados ao Signal.

Para mais informações, veja [[Security Planner / Signal => https://securityplanner.org/#/tool/signal]].

Ative o Encontre meu Dispositivo
=====================================================

Considere ativar a função "Encontre meu Dispositivo", no Android, ou "Buscar iPhone", no iOS. Ela permitirá que você encontre, bloqueie ou apague as informações do seu aparelho remotamente caso ele seja perdido ou roubado.

Para mais informações, veja:

* [[Security Planner / Find My Device (Android) => https://securityplanner.org/#/tool/find-my-device
]].
  * OBSERVAÇÃO: Este recurso requer que você vincule uma conta Google ao seu dispositivo. Além disso, se habilitado, o Google terá mais informações sobre você, inclusive seu histórico de localização.
* [[Security Planner / Find My iPhone (iOS) => https://securityplanner.org/#/tool/find-my-iphone]]

Fotografe com segurança
======================================================

A câmera do seu celular inclui muitas informações potencialmente confidenciais nos metadados de cada foto tirada. Já que você não tem como saber como algo que publica on-line será usado, vale a pena sempre apagar informações pessoais de fotos antes de compartilhar.

Para evitar que uma foto seja "geolocalizada", abra as configurações do seu aplicativo de câmera e procure a opção de desligar a inclusão de dados de localização nas fotos.

Mesmo com a geolocalização desligada, sua câmera salvará o modelo do dispositivo e outras informações potencialmente confidenciais. O único jeito de se livrar disso é usar um aplicativo separado para remover os dados "EXIF" dos arquivos de imagem. Esses apps também podem ser usados para remover dados de localização de fotos tiradas anteriormente.

Para mais informações, veja: [[3 ways to remove EXIF metadata from photos => https://www.makeuseof.com/tag/3-ways-to-remove-exif-metadata-from-photos-and-why-you-might-want-to/]].

Outras dicas
==================================================

* Proteja seu celular com senha. Não use a impressão digital para desbloquear seu aparelho. Esse recurso não é seguro.
* Configure seu telefone para não mostrar notificações detalhadas na tela de bloqueio.
* Saiba que seu aparelho se sincroniza com a nuvem. Por exemplo, mesmo que você apague uma foto do celular, talvez ela já tenha sido salva por um ou mais serviços de nuvem, como iCloud ou Dropbox.
