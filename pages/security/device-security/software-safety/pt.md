@title = "Boas Práticas de Segurança de Software"
@nav_title = "Segurança de Software"
@summary = "Boas práticas para instalar e atualizar software"
@toc = true

# Mantenha seu software atualizado

Quase toda vez que um atacante consegue compremeter um computador através de uma vulnerabilidade no software, o ataque poderia ter sido prevenido se o software estivesse atualizado. Isso é porque quase todas as vulnerabilidades são conhecidas pelos desenvolvedores do software e já foram consertadas no momento em que o atacante aprende a se aproveitar das falhas.

É especialmente importante manter seu sistema operacional atualizado, já que o sistema operacional tem acesso privilegiado a tudo que acontece em seu dispositivo.

Como ativar atualizações automáticas:

* **macOS**: A partir do menu **Apple**, selecione **Preferências do Sistema** > **App Store** > **Baixar novas atualizações quando disponíveis**.
* **Windows**: Clique no botão **Iniciar**, selecione **Configurações** > **Atualização e Segurança** > **Windows Update** > **Opções avançadas** e em **Escolha como as atualizações serão instaladas**, selecione **Automático (recomendado)**.

Observações:

* Você pode precisar reiniciar seu dispositivo para que diversas atualizações sejam aplicadas, então permitir que seu dispositivo reinicie automaticamente após uma atualização é necessário para que a atualização possa prover proteção.
* Se você tem requisitos específicos para softwares ou softwares customizados para sua organização, atualizações automáticas podem causar interrupções em seu trabalho, já que algumas atualizações do sistema operacional podem ser incompatíveis com os softwares existentes.
* Manter seu software atualizado não ajuda com ataques de Phishing ou Malware, que funcionam enganando o usuário a realizar certo comportamento inseguro.

# Use a loja oficial de aplicativos

Quando possível, é melhor instalar software pela loja oficial de aplicativos do seu sistema operacional, por várias razões:

* **Autenticidade**: Os apps na loja oficial de aplicativos são assinados pelo desenvolvedor e verificadps pela loja de aplicativos.
* **Atualizações**: A loja de apicativos vai te ajudar a manter seus apps atualizados.
* **Prevenção de Ataques de Side Loading**: Instalar um app por fora da loja oficial de aplicativos é chamado de "side loading". Side loading é atualmente desabilitado por padrão no Android, impossível no iOS, e é habilitado por padrão no macOS e Windows. Quando o side loading está habilitado, seu computador fica mais vulnerável a diferentes formas de ataque de malware. Por essa razão, ambos macOS e Windows estão tentando migrar para um modelo em que side loading esteja desabilitado por padrão.

Nota: Você precisa de cuidado com a loja oficial de aplicativos do Android, Google Play, já que é comum a existência de aplicativos falsos que imitam e tentam se passar por um determinado aplicativo verdadeiro.

# Quando em dúvida, não instale

A proliferação de aplicativos móveis, extensões de navegador e outros programas gratuitos causou numerosos problemas de seguranças. Evite softwares que não foram criados por uma companhia com a qual você já tem estabelecida uma relação de confiança (por exemplo, qualquer companhia cujas ferramentas você já esteja usando em sua organização).

Softwares que aparentam ter boas intenções (como um antivírus) ou ferramentes benéficas podem estar mascarando atividades maliciosas em segundo plano. Na maioria dos navegadores e dispositivos móveis, uma aplicação vai solicitar certas permissões durante a instalação - as informações e hardware que ela pode acessar em seu dispositivo. É importante prestar atenção nisso para garantir que a ação da aplicação no mínimo vagamente reflita o que é esperado. Por exemplo, se um aplicativo de lanterna pede permissão para acessar seus contatos ou fazer ligações, você provavelmente não quer instalá-lo. Permissões a se prestar atenção especial antes de aceitar incluem acesso a suas chamadas, seus contatos, à câmera, ao microfone, aos serviços de localização, ou ao armazenamento completo.

A maneira de olhar as permissões após a instalação depende do contexto. No Chrome, vá para chrome://extensions/ e clique no link de permissões para cada extensão. Em dispositivos iOS, há uma lista de todas as permissões nas Configurações; para cada permissão há uma lista dos aplicativos que a usam. Em dispositivos Android, isso no geral se encontra em Configurações > Apps > Gerenciar apps; onde há uma lista dos aplicativos instalados, e para cada aplicativo há uma lista das permissões utilizadas.

Infelizmente, a maioria dos sistemas de instalação de software em laptops e computadores desktop não vão pedir permissão para acessar recursos, então você precisa ter cuidado extra ao instalar software que não seja em um navegador, um dispositivo móvel ou da loja de aplicações oficial do sistema operacional.

# Evite usar software pirateado

Instalar software pirateado pode infectar seu computador com um vírus ou outro tipo de malware.

Além disso, se você instalar software pirateado em seu computador de trabalho, é possível que sua empresa te faça pagar milhares de reais em multas para seu dispositivo único. Quando isso acontece, você pode acabar demitido por violar as políticas de segurança e privacidade de seu empregador.

Se há uma aplicação que você precisa ter, e você não pode obter por meios seguros, considere usar uma alternativa gratuita e de código aberto.

# Use software livre

Essas aplicações gratuitas e de código aberto são ótimas alternativas a produtos comerciais comumente usados, disponíveis para Mac, Windows e Linux:

* **[Gimp](https://www.gimp.org/)**: Programa de edição de imagens bitmap e de fotos (alternativa ao Adobe Photoshop)
* **[Inkscape](https://inkscape.org/en/)**: Programa de edição de vetores (alternativa ao Adobe Illustrator)
* **[LibreOffice](https://www.libreoffice.org/)**: Conjunto de produtividade Office (alternativa ao Microsoft Office)
* **[Scribus](https://www.scribus.net)**: Programa de editoração eletrônica (alternativa ao Adobe InDesign)

# Veja também

* [Security Planner / Update Your Windows Computer](https://securityplanner.org/#/tool/update-your-windows-pc) (em inglês) 
* [Security Planner / Keep Your Mac Updated](https://securityplanner.org/#/tool/update-your-mac) (em inglês)
* [Security Planner / Use Safe Apps](https://securityplanner.org/#/tool/use-safe-apps) (em inglês)
