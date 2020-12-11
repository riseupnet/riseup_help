@title = "Clientes de XMPP"
@summary = "Configure clientes de XMPP para se conectar ao bate-papo do Riseup."

<p class=“alert alert-info”>Please help us update this page by trying out different clients.</p>

## Recursos a procurar

- **OTR?**  Se sim, o cliente implementa o protocolo OTR, que serve para criptografar, de ponta a ponta, mensagens de bate-papo, e oferece confidencialidade persistente ("perfect forward secrecy").
- **[OMEMO](https://conversations.im/omemo/)?** Se sim, o cliente oferece criptografia de ponta a ponta para múltiplos clientes e bate-papo off-line.
- ** <a href="https://en.wikipedia.org/wiki/Jingle_(protocol)">Jingle</a>?** Se sim, o cliente pode ser usado para bate-papo de voz e vídeo.
- **[Proxy](https://pt.wikipedia.org/wiki/Proxy)?** Se sim, o cliente pode se conectar via proxy e obedece às configurações de proxy.
- **[TLS](https://pt.wikipedia.org/wiki/Transport_Layer_Security)?** Se sim, o cliente pode se conectar de maneira segura ao provedor de bate-papo.
- **[[Tor]]?** Se sim, o cliente pode fazer a conexão através do Tor para contornar censura e acessar serviços anonimamente. Se não, o cliente *não deve ser usado com o Tor*.
- **[[MUC]]?** If yes, this client can be used for Multi-User Chat (chatrooms XEP-0045)

## Clientes recomendados

| Cliente                                          | Sistemas operacionais                     | OTR?  | OMEMO? | Jingle?       | Proxy? | TLS?  | Tor?  | MUC?  | Comentários                                                                                         |
|--------------------------------------------------|-------------------------------------------|-------|--------|---------------|--------|-------|-------|-------|-----------------------------------------------------------------------------------------------------|
| [Gajim](https://gajim.org)                        | GNU/Linux, Windows, FreeBSD               | Não   | *Sim*  | *Sim*         | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um bom cliente de bate-papo multiplataforma escrito em Python e GTK+.                |
| [Gajim 0.16.x](https://gajim.org)                | GNU/Linux, Windows, FreeBSD               | *Sim* | Não    | *Sim*         | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um bom cliente de bate-papo multiplataforma escrito em Python e GTK+.                |
| [Psi](https://psi-im.org)                        | GNU/Linux, Windows, macOS                 | *Sim* | *Sim*  | *Sim* (Linux) | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um bom cliente de bate-papo multiplataforma escrito em C ++ e Qt.                    |
| [Psi+](https://psi-plus.com)                     | GNU/Linux, Windows, macOS, Haiku, FreeBSD | *Sim* | *Sim*  | *Sim* (Linux) | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um bom cliente de bate-papo multiplataforma escrito em C ++ e Qt.                    |
| [CoyIM](https://coy.im)                          | GNU/Linux, Windows, macOS                 | *Sim* | Não    | Não           | *Sim*  | *Sim* | *Sim* | Não   | Código aberto. Cliente de bate-papo seguro por padrão para GNOME. Suporte nativo ao Tor, OTR e TLS. |
| [ChatSecure](https://chatsecure.org)             | Android, F-Droid, iOS                     | *Sim* | *Sim*  | Não           | *Sim*  | *Sim* | *Sim* | ?     | Código aberto. Um ótimo cliente para iOS. Suporte nativo ao Tor.                                    |
| [Conversations](https://conversations.im)        | Android                                   | Não   | *Sim*  | Não           | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um ótimo cliente para Android. Oferece criptografia para bate-papo em grupo!         |
| [Conversations Legacy](https://conversations.im) | Android                                   | *Sim* | Não    | Não           | *Sim*  | *Sim* | *Sim* | *Sim* | Código aberto. Um ótimo cliente para Android. Oferece criptografia para bate-papo em grupo!         |

## Outros clientes

| Cliente                                             | Sistemas operacionais     | OTR?           | OMEMO?         | Jingle?       | Proxy? | TLS?  | Tor?    | MUC? | Comentários                                                                               |
|-----------------------------------------------------|---------------------------|----------------|----------------|---------------|--------|-------|---------|------|------------------------------------------------------------------------------------------- |
| [[Adium]]                                               | macOS                     | *Sim*          | *Sim* (Plugin) | Não           | *Sim*  | *Sim* | Parcial | ?    | Código aberto. Inseguro por falta de atualização. Vazamento das informações de DNS e URL. |
| [Jitsi](https://jitsi.org)                          | GNU/Linux, Windows, macOS | *Sim*          | Não            | *Sim*         | ?      | *Sim* | ?       | ?    | Código aberto. Escrito em Java.                                                           |
| [Miranda](https://miranda-im.org)                   | Windows                   | *Sim*          | Não            | Não           | ?      | ?     | ?       | ?    | Código aberto. Cliente estável com muitas extensões.                                      |
| [Miranda NG](https://miranda-ng.org)                | Windows                   | *Sim*          | Não            | Não           | ?      | ?     | ?       | ?    | Código aberto. Cliente estável com muitas extensões.                                      |
| [[Pidgin]]                                              | GNU/Linux, Windows, macOS | *Sim* (Plugin) | *Sim* (Plugin) | *Sim* (Linux) | *Sim*  | *Sim* | *Sim*   | ?    | Código aberto. Estável e com muitas funções. Use a versão mais atual!                     |
| [Spark](https://igniterealtime.org/projects/spark/) | GNU/Linux, Windows, macOS | *Sim*          | Não            | *Sim*         | ?      | ?     | ?       | ?    | Código aberto. Escrito em Java.                                                           |

## Clientes para evitar

| Client                                    | OS supportés | OTR? | OMEMO? | Jingle? | Proxy?        | SSL/TLS?      | Tor? | MUC? | Comentários                                                                   |
|-------------------------------------------|--------------|------|--------|---------|---------------|---------------|------|------|-------------------------------------------------------------------------------|
| [Beem](https://beem-project.com)          | Android      | Não  | Não    | Não     | ?             | ?             | ?    | ?    | Código aberto. App estável nativo do Android. Não oferece bate-papo em grupo. |
| [Empathy](https://live.gnome.org/Empathy) | GNU/Linux    | Não  | Não    | *Sim*   | *Sim* (GNOME) | *Sim* (GNOME) | ?    | ?    | Código aberto. Estável e fácil de usar.                                       |
| [iChat](https://www.apple.com)            | macOS        | Não  | Não    | Não     | ?             | ?             | ?    | ?    | Este aplicativo da Apple conta com suporte limitado a XMPP.                   |
| [Pandion](https://pandion.im)             | Windows      | Não  | Não    | Não     | ?             | ?             | ?    | ?    | Código aberto. Um cliente de XMPP para Windows bom e estável.                 |
