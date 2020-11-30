@title = "XMPP Clients"
@summary = "Configuring XMPP clients for use with Riseup's chat service."

p(alert alert-info). Please help us update this page by trying out different clients.

h2. Features to look for

table(table).
| *OTR?* | If yes, this client has built in support for [[OTR]] which provides end-to-end encryption of chat messages and has perfect-forward-secrecy. |
| *[[OMEMO -> https://conversations.im/omemo/]]?* | If yes, this client has support for end-to-end encryption that supports multiple clients and offline chats. |
| *[[Jingle -> https://en.wikipedia.org/wiki/Jingle_(protocol)]]?* | If yes, this client can used for voice or video chat. |
| *[[Proxy -> https://en.wikipedia.org/wiki/Proxy_server]]?* | If yes, this client may connect through a proxy and that the client obeys the proxy settings. |
| *[[TLS -> https://en.wikipedia.org/wiki/Transport_Layer_Security]]?* | If yes, this client support secure connections with the chat provider. |
| *[[Tor]]?* | If yes, this client can correctly use Tor to circumvent censorship and to access services anonymously. If no, then the client *should not be used with Tor*. |
| *[[MUC]]?* | If yes, this client can be used for Multi-User Chat (chatrooms XEP-0045) |

h2. Recommended clients

table(table table-striped).
|_. Client |_. Supported OS |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. TLS? |_. Tor? |_. MUC? |_. Comments |
| [[Gajim -> https://gajim.org]] | GNU/Linux, Windows, FreeBSD | No | *Yes* | *Yes* | *Yes* | *Yes* | *Yes* | *Yes* | Open source. Nice cross-platform chat client written in Python and GTK+. |
| [[Gajim 0.16.x -> https://gajim.org]] | GNU/Linux, Windows, FreeBSD | *Yes* | No | *Yes* | *Yes* | *Yes* | *Yes* | *Yes* | Open source. Nice cross-platform chat client written in Python and GTK+. |
| [[Psi -> https://psi-im.org]] | GNU/Linux, Windows, macOS | *Yes* | *Yes* | *Yes* (Linux) | *Yes* | *Yes* | *Yes* | *Yes* | Open source. Nice cross-platform chat client written in C++ and Qt. |
| [[Psi+ -> https://psi-plus.com]] | GNU/Linux, Windows, macOS, Haiku, FreeBSD | *Yes* | *Yes* | *Yes* (Linux) | *Yes* | *Yes* | *Yes* | *Yes* | Open source. Nice cross-platform chat client written in C++ and Qt. Development version of Psi |
| [[CoyIM -> https://coy.im]] | GNU/Linux, Windows, macOS | *Yes* | No | No | *Yes* | *Yes* | *Yes* | No | Open source. Secure-by-default chat client for GNOME. Has built-in support for Tor, OTR and TLS. |
| [[ChatSecure -> https://chatsecure.org]] | Android, F-Droid, iOS | *Yes* | *Yes* | No | *Yes* | *Yes* | *Yes* | ? | Open source. A very good chat client for iOS. Native Tor support. |
| [[Conversations -> https://conversations.im]] | Android | No | *Yes* | No | *Yes* | *Yes* | *Yes* | *Yes* | Open source. A very good chat client for Android. Supports encrypted group chats! |
| [[Conversations Legacy -> https://conversations.im]] | Android | *Yes* | No | No | *Yes* | *Yes* | *Yes* | *Yes* | Open source. A very good chat client for Android. Supports encrypted group chats! |

h2. Other clients

table(table table-striped).
|_. Client |_. Supported OS |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. TLS? |_. Tor? |_. MUC? |_. Comments |
| [[Adium]] | macOS | *Yes* | *Yes* (Plugin) | No | *Yes* | *Yes* | Partial | ? | Open source. Lack of updates cause for security concern. DNS and URL hovering information leaks. |
| [[Jitsi -> https://jitsi.org]] | GNU/Linux, Windows, macOS | *Yes* | No | *Yes* | ? | *Yes* | ? | ? | Open source. Written in Java. |
| [[Miranda -> https://miranda-im.org]] | Windows | *Yes* | No | No | ? | ? | ? | ? | Open source. Stable client with many plugins. |
| [[Miranda NG -> https://miranda-ng.org]] | Windows | *Yes* | No | No | ? | ? | ? | ? | Open source. Stable client with many plugins. |
| [[Pidgin]] | GNU/Linux, Windows, macOS | *Yes* (Plugin) | *Yes* (Plugin) | *Yes* (Linux) | *Yes* | *Yes* | *Yes* | ? | Open source. Stable with many features. Make sure to use most the current version! |
| [[Spark -> https://igniterealtime.org/projects/spark/]] | GNU/Linux, Windows, macOS | *Yes* | No | *Yes* | ? | ? | ? | ? | Open source. Written in Java. |

h2. Clients to avoid

table(table table-striped).
|_. Client |_. OS supportés |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. SSL/TLS? |_. Tor? |_. MUC? |_. Comments |
| [[Beem -> https://beem-project.com]] | Android | No | No | No | ? | ? | ? | ? | Open source. Stable native android app. Does not support group chats. |
| [[Empathy -> https://live.gnome.org/Empathy]] | GNU/Linux | No | No | *Yes* | *Yes* (GNOME) | *Yes* (GNOME) | ? | ? | Open source. Stable and easy to use. |
| [[iChat -> https://www.apple.com]] | macOS | No | No | No | ? | ? | ? | ? | Apple's built-in chat application has limited XMPP support. |
| [[Pandion -> https://pandion.im]] | Windows | No | No | No | ? | ? | ? | ? | Open source. Nice stable windows XMPP client. |
