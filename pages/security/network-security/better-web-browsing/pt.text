@title = 'Melhore sua navegação na rede'

h2. Escolhendo um navegador

Todos os quatro maiores navegadores da web -- Firefox, Chrome, Internet Explorer e Safari -- têm apresentado graves falhas de segurança nos últimos tempos, então você deve se certificar de que está usando a versão mais recente, qualquer que seja a sua escolha.

Todos esses quatro principais navegadores receberam notas ruins na nossa avaliação (confira em [[browser-score-card]]). Eles podem, porém, funcionar bem melhor se algumas extensões forem instaladas (ver abaixo).

Como alternativa, o projeto Tor oferece uma versão modificada do Firefox, adaptada para maior segurança e anonimato, chamada [[Tor Browser => https://www.torproject.org/download/download-easy.html]].

h2. Ajuste suas configurações

h3. Desative cookies de terceiros

Cookies de terceiros são identificadores de rastreamento usados por redes de publicidade para traçar seu comportamento enquanto você navega de site em site. Eles são uma abominação e não servem a propósitos legítimos.

* Firefox: Preferências > Privacidade e segurança > Bloqueio de conteúdo > Cookies de terceiros > Todos os cookies de terceiros.
* Chrome: Configurações > Avançado > Privacidade e segurança > Configurações de conteúdo > Cookies > Bloquear cookies de terceiros.

h3. Limpe os cookies ao sair

A maioria dos navegadores guarda cookies por muito mais tempo do que o necessário. É melhor configurar seu navegador para limpá-los quando for fechado.

* Firefox: Preferências > Privacidade e segurança > Cookies e dados de sites > Manter até Firefox ser fechado. 
* Chrome: Configurações > Avançado > Privacidade e segurança > Configurações de conteúdo > Cookies > Manter os dados locais só até você sair do navegador.

h3. Desative o Flash

Flash é um plug-in da Adobe que tem sido fonte de uma enxurrada de problemas de segurança. Recomendamos veementemente que você o remova ou desabilite.

* Firefox: Extensões > Plugins > Flash > Nunca ativar.
* Chrome: Configurações > Avançado > Configurações de conteúdo > Perguntar primeiro.

h3. Desative o Java

Java também apresenta muitos problemas de segurança, e é provável que você nunca sequer tenha precisado usá-lo. Remova-o ou desabilite-o sem demora.

* Firefox: Extensões > Plugins > Java > Nunca ativar.

h3. Altere a ferramenta de busca padrão

Já que está arrumando suas configurações, aproveite para mudar sua ferramenta de busca padrão para [[duckduckgo.com => https://duckduckgo.com]]. O DuckDuckGo é a recomendação do Riseup dentre as opções de ferramenta de busca que respeitam a sua privacidade. Confira as instruções de uso para [[navegadores desktop => https://duck.co/help/desktop/adding-duckduckgo-to-your-browser]] e [[navegadores móveis => https://duck.co/help/mobile]].

h2. Extensões de navegador

As extensões desta lista funcionam tanto no Firefox quanto no Chrome, exceto onde indicado.

h3. Extensões essenciais

Estas são extensões de navegação absolutamente essenciais que deveriam ser usadas sempre. Elas são estáveis, de código aberto e raramente causam travamentos.

<table class="table">
<tr>
  <td>
    !img/ublock-64.png!
  </td>
  <td>
    [*[[uBlock Origin -> https://github.com/gorhill/uBlock]]*] ([[Chrome => https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm]], [[Firefox => https://addons.mozilla.org/pt-BR/firefox/addon/ublock-origin/]]) evita a maioria das redes de publicidade e rastreamento. É similar ao Adblock Plus e ao Disconnect, mas funciona melhor e é bem mais rápido.
  </td>
</tr>
<tr>
  <td>
    !img/https-64.png!
  </td>
  <td>
    [*[[HTTPS Everywhere => https://www.eff.org/https-everywhere]]*] estabelece automaticamente uma conexão segura usando TLS quando há disponibilidade. Isso ajuda a proteger o conteúdo da sua navegação de vigilância, apesar de não ocultar o endereço da página acessada (a não ser que você também use [[Tor]] ou uma [[VPN]]).
  </td>
</tr>
<tr>
  <td>
    !img/badger-64.png!
  </td>
  <td>
    [*[[Privacy Badger => https://www.eff.org/privacybadger]]*] detecta de forma dinâmica tentativas de rastrear seu comportamento de navegação e bloqueia conteúdos desses rastreadores. O Privacy Badger não é projetado para bloquear propagandas, então não é um substituto do uBlock, porém conta com algumas funções de segurança que este não tem (em modo padrão).
  </td>
</tr>
</table>

Observações:

* Vazamento de endereços IP: todo navegador vaza seu endereço IP verdadeiro durante conferências de áudio ou vídeo. Quando usar uma VPN ou Tor durante um bate-papo de áudio ou vídeo, acesse as configurações do uBlock e habilite a opção que impede a WebRTC de vazar seu endereço IP verdadeiro.
* Modo avançado do uBlock: antes de executar o uBlock [[em modo avançado => https://github.com/gorhill/uBlock/wiki/Advanced-user-features]], desligue o Privacy Badger.

h3. Extensões avançadas

Estas extensões são recomendadas para quem tem conhecimento avançado, seja porque são complicadas de usar ou porque podem prejudicar o funcionamento de vários sites.

Estas extensões tentam contornar falhas básicas de privacidade em como operam os navegadores da web. Entretanto, a estrutura básica de muitos sites depende dessas falhas de privacidade, ou seja, eles deixam de funcionar quando são feitas tentativas de consertá-las.

São algumas dessas falhas de privacidade:

* *HTTP Referrer:* quando você clica em um link, seu navegador envia para a página aberta a localização da anterior. Informações de identificação pessoal podem estar inclusas no URL de uma página em particular, por isso o HTTP Referrer deve ser desativado. Você só consegue fazer isso com uma extensão.
* *HTTP User-Agent:* seu navegador envia uma cadeia de caracteres especial de "User-Agent" (agente utilizador) para toda página que você acessa. Essa cadeia contém uma grande quantidade de informações incomuns que podem ser usadas, junto com outros dados, para identificar exclusivamente o seu tráfego na rede. Essa string não tem muita utilidade hoje em dia, portanto é melhor usar um valor genérico, como o do Tor Browser.
* *HTML5 Canvas:* muitos sites estão começando a usar o elemento canvas do HTML5 para identificar sua navegação e rastrear seu comportamento. Atualmente não há como desativá-lo, embora algumas novas extensões estejam fazendo tentativas rudimentares.
* *JavaScript:* JavaScript é essencial para a maioria dos sites atualmente, mas pode ser que você queira desabilitá-lo algum dia. Quando está habilitado, é mais fácil para um site identificar o seu navegador e rastrear seu comportamento. Além disso, a maioria das vulnerabilidades de segurança dos navegadores é causada por JavaScript.

Para Firefox:

* [[Self Destructing Cookies => https://addons.mozilla.org/pt-BR/firefox/addon/self-destructing-cookies/]] limpa os cookies de um site quando todas as abas dele são fechadas (e não apenas quando o navegador é fechado).
* [[µMatrix => https://addons.mozilla.org/pt-BR/firefox/addon/umatrix/]] permite bloquear seletivamente JavaScript, plug-ins e outros recursos, além de controlar recursos de terceiros. Ele também inclui várias funcionalidades de privacidade, como camuflagem do user-agent, bloqueio do rastreamento de sites de origem e muito mais. Ele substitui o NoScript e o RequestPolicy.
* [[User-Agent Switcher => https://addons.mozilla.org/pt-BR/firefox/addon/user-agent-switcher/]] pode ser usado para alterar o user-agent de HTTP.
* [[Canvas Fingerprint Blocker => https://addons.mozilla.org/pt-BR/firefox/addon/canvasblocker/]] permite que você desabilite o elemento canvas do HTML5 em sites específicos. 

Para Chrome:

* [[µMatrix => https://chrome.google.com/webstore/detail/%C2%B5matrix/ogfcmafjalglgifnmanfmnieipoejdcf]] permite que você bloqueie seletivamente o JavaScript, plug-ins e outros recursos, além de controlar recursos de terceiros. Ele inclui várias funcionalidades de proteção à privacidade, como camuflagem do user-agent, bloqueio do rastreamento de sites de origem e muito mais. Ele substitui o NoScript e o RequestPolicy.
* [[User-Agent Switcher => https://chrome.google.com/webstore/detail/user-agent-switcher/ffhkkpnppgnfaobgihpdblnhmmbodake]] permite que você modifique o user-agent de HTTP.
* [[CanvasFingerPrintBlock => https://chrome.google.com/webstore/detail/canvasfingerprintblock/ipmjngkmngdcdpmgmiebdmfbkcecdndc]] bloqueia a maior parte do rastreamento de pegadas digitais através do elemento canvas do HTML5 (código não aberto).

h3. Perigosas ou não recomendáveis

Apesar de sua popularidade, recomendamos que você evite as seguinte extensões:

* [[Adblock Plus => https://adblockplus.org/]] costumava ser a melhor extensão para bloquear propaganda e rastreamento. Porém, agora eles tem um esquema no qual anunciantes podem pagar suborno para passar pelos seus filtros. Sem contar que o uBlock tem uma tecnologia melhor. 
* [[Disconnect => https://disconnect.me/disconnect]] funciona como o uBlock e é de código aberto. Para quem usa o uBlock, o Disconnect é desnecessário, embora tenha algumas opções de visualização que aquele não tem. 
* [[Ghostery => https://www.ghostery.com]] funciona como o uBlock, mas suas configurações padrão são péssimas e permitem a maioria dos rastreamentos, além do que seu código é proprietário.
* Flash Block (Firefox) é uma extensão que permite que você "clique para ativar" o Flash. É preferível desinstalar o Flash. Além disso, essa opção agora é integrada ao Firefox.
* [[Better Privacy => https://addons.mozilla.org/pt-BR/firefox/addon/betterprivacy/]] já foi útil para remover objetos locais compartilhados, ou "cookies do Flash", mas desde a chegada da API [[ClearSiteData => https://en.wikipedia.org/wiki/Local_shared_object#Browser_control]], essa extensão não é mais necessária.
* TrackMeNot gera tráfegos de busca falsos. É uma ideia interessante, mas é muito melhor apenas usar DuckDuckGo.

h2. Verifique a validação do certificado de Riseup 

Na internet, certificados são necessários para verificar a identidade de pessoas e computadores. Esses certificados também são chamados de certificados SSL ou certificados digitais. Vamos nos referir a eles só como "certificados" aqui. 

Em particular, certificados são necessários para estabelecer conexões seguras. Sem eles, você pode ter certeza de que uma terceira pessoa não está bisbilhotando suas conversas, mas não que está se comunicando com o computador certo! Todos os servidores e serviços de riseup.net permitem ou requerem conexões seguras.

Para se certificar da segurança de sua comunicação com o Riseup, veja [[como verificar os nossos certificados => /security/certificates]].
