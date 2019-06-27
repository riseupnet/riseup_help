@title = "Criptografia de dispositivo"
@toc = true
@summary = "Como e por que criptografar a memória do seu dispositivo"

# Por que criptografar meu dispositivo?

Com seu dispositivo criptografado, o conteúdo da memória -- a parte que contém sistema operacional, programas instalados e seus dados pessoais -- é embaralhado para que não possa ser acessado enquanto o aparelho estiver desligado ou bloqueado.

Sem criptografia, se alguém roubar, encontrar ou de alguma outra forma acessar seu equipamento, poderá facilmente abrir seus arquivos, entrar nas suas contas on-line e se fazer passar por você. Pior ainda, pode instalar um programa malicioso que permita acessar remotamente todas as suas atividades.

# Como ativar a criptografia de dispositivo

Embora criptografia de disco inteiro seja padrão em alguns aparelhos móveis, ela deve ser ativada manualmente em computadores, bem como em vários modelos de telefone e tablet.

Passo a passo para computadores:

* **Windows**: [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
  * IMPORTANTE: Por padrão, a Microsoft salva na nuvem uma cópia de segurança da chave criptográfica do seu computador. Isto é, a empresa, além de qualquer governo com o qual ela coopere, pode facilmente decriptografar o seu PC. Se você se preocupa com a possibilidade de um governo obter acesso ao conteúdo do seu dispositivo, é uma boa ideia desativar esse "recurso" e [[gerar novas chaves criptográficas => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]] agora.
* **macOS**: [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* **Linux**: Praticamente todas as distribuições do Linux permitem criptografar o computador durante a instalação do sistema operacional. Pode-se fazer isso de duas formas:
  * "Criptografia de disco inteiro: Neste método, tudo na memória primária é criptografado, inclusive o sistema operacional. Uma senha separada será requisitada quando o computador ligar.
  * "Criptografia da pasta Home: Neste método, o sistema operacional **não** é criptografado. Seus dados pessoais são protegidos, mas é mais fácil para alguém com acesso ao hardware instalar software malicioso.

Passo a passo para dispositivos móveis:

* **iOS**: [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* **Android**: [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)

# Contras da criptografia de dispositivo

**Desvantagens** A criptografia de dispositivo não funciona sempre! Se a sua [[senha => passwords]] não for complexa, é fácil para um computador adivinhá-la e desbloquear o seu equipamento. Além disso, a criptografia de dispositivo não oferece proteção contra vírus e programas maliciosos. Se os seus dados forem copiados para um serviço de backup em nuvem que seja comprometido ou coopere com o governo, a criptografia de dispositivo não vai protegê-los - a não ser que se use um serviço que contemple, especificamente, criptografia do lado do cliente.

**A autenticação deve estar ativa** A criptografia de dispositivo só é eficaz se requerer autenticação - por exemplo, com a exigência de senha para iniciar uma sessão no seu laptop ou para desbloquear o seu celular.

**Impossibilita a recuperação de disco** A criptografia de disco inteiro também pode aumentar o seu risco de perda do acesso a algumas das suas informações se você não tiver um cuidado especial com a administração das suas senhas. Uma senha perdida ou uma falha na parte do disco que armazena as chaves criptográficas implica, geralmente, que você - ou qualquer outra pessoa - não poderá recuperar seus dados. Certifique-se de fazer backups periódicos para minimizar o risco de perda de dados.

**O dispositivo deve estar desligado ou bloqueado** Criptografar um dispositivo garante proteção apenas quando ele estiver desligado, ou ligado, mas à espera de uma senha para iniciar. Depois que você se autenticar, o computador passa a ter a chave secreta necessária para decriptografar os seus dados na memória, então mesmo com a tela bloqueada existe o risco de alguém obter acesso ao conteúdo do PC enquanto ele estiver ligado (ou até hibernando). Em geral, porém, passar por esses controles requer conhecimento altamente técnico, então isso não deve impedir você de manter seu computador ligado e desbloqueado quando precisar trabalhar. No entanto, é melhor desligá-lo sempre que for se afastar dele, estando em meio hostil. Se você se preocupa com a possibilidade de ser alvo de um ataque cibernético, é uma boa ideia manter seu equipamento sempre fisicamente próximo.

# Veja também

* [Security In-a-box / Secure File Storage](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows Encryption](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac Encryption](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS Encryption](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android Device Encryption](https://securityplanner.org/#/tool/android-device-encryption)
* [Security Self-defense / How to: Encrypt Your iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
