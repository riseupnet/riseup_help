@title = "XMPP клиенты"
@summary = "Настройка XMPP клиентов для работы с чат-сервером Riseup."

p(alert alert-info). Please help us update this page by trying out different clients.

h2. Ключевые возможности

table(table).
| *OTR?* | Если да, клиент поддерживает [[OTR]] (Off-the-Record Messaging) протокол, который обеспечивает [[end-to-end шифрование -> https://en.wikipedia.org/wiki/End-to-end_encryption]] сообщений и обладает абсолютной прямой секретностью ([[Perfect forward secrecy -> https://ru.wikipedia.org/wiki/Perfect_forward_secrecy]]). |
| *[[OMEMO -> https://conversations.im/omemo/]]?* | Если да, клиент поддерживает многоклиентное [[end-to-end шифрование -> https://ru.wikipedia.org/wiki/Off-the-Record_Messaging]]. В отличии от OTR, OMEMO также подджерживает end-to-end шифрование оффлайн чатов. |
| *[[Jingle -> https://ru.wikipedia.org/wiki/Jingle_(протокол)]]?* | Если да, клиент может использоваться для аудио- и видеочата. |
| *[[Proxy -> https://ru.wikipedia.org/wiki/Прокси-сервер]]?* | Если да, клиент может подключаться через прокси-сервер. |
| *[[TLS -> https://ru.wikipedia.org/wiki/TLS]]?* | Если да, клиент поддерживает защищенное соединение с сервером. |
| *[[Tor]]?* | Если да, клиент может корректно использовать Tor для обхода цензуры и анонимного доступа к сервисам. Если нет, то клиент *не должен использоваться с Tor*. |
| *[[MUC]]?* | If yes, this client can be used for Multi-User Chat (chatrooms XEP-0045) |

h2. Рекомендуемые клиенты

table(table table-striped).
|_. Клиент |_. Поддерживаемые ОС |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. TLS? |_. Tor? |_. MUC? |_. Комментарии |
| [[Gajim -> https://gajim.org]] | GNU/Linux, Windows, FreeBSD | Нет | *Да* | *Да* | *Да* | *Да* | *Да* | *Да* | Open source. Кроссплатформенный мессенджер написанный на Python и использующий GTK+. |
| [[Gajim 0.16.x -> https://gajim.org]] | GNU/Linux, Windows, FreeBSD | *Да* | Нет | *Да* | *Да* | *Да* | *Да* | *Да* | Open source. Кроссплатформенный мессенджер написанный на Python и использующий GTK+. |
| [[Psi -> https://psi-im.org]] | GNU/Linux, Windows, macOS | *Да* | *Да* | *Да* (Linux) | *Да* | *Да* | *Да* | *Да* | Кроссплатформенный мессенджер написанный на С++ и Qt. |
| [[Psi+ -> https://psi-plus.com]] | GNU/Linux, Windows, macOS, Haiku, FreeBSD | *Да* | *Да* | *Да* (Linux) | *Да* | *Да* | *Да* | *Да* | Кроссплатформенный мессенджер написанный на С++ и Qt. |
| [[CoyIM -> https://coy.im]] | GNU/Linux, Windows, macOS | *Да* | Нет | Нет | *Да* | *Да* | *Да* | Нет | Open source. Безопасный-по-умолчанию мессенджер: по умолчанию включен OTR и используется Tor. Написан на Go. |
| [[ChatSecure -> https://chatsecure.org]] | Android, F-Droid, iOS | *Да* | *Да* | Нет | *Да* | *Да* | *Да* | ? | Open source. Хороший мессенджер для iOS. Интегрирована поддержка Tor. |
| [[Conversations -> https://conversations.im]] | Android | Нет | *Да* | Нет | *Да* | *Да* | *Да* | *Да* | Open source. Хороший мессенджер для Android. Поддерживает защищенные групповые чаты! |
| [[Conversations Legacy -> https://conversations.im]] | Android | *Да* | Нет | Нет | *Да* | *Да* | *Да* | *Да* | Open source. Хороший мессенджер для Android. Поддерживает защищенные групповые чаты! |

h2. Другие клиенты

table(table table-striped).
|_. Клиент |_. Поддерживаемые ОС |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. TLS? |_. Tor? |_. MUC? |_. Комментарии |
| [[Adium]] | macOS | *Да* | *Да* (Plugin) | Нет | *Да* | *Да* | Частично | ? | Open source. Lack of updates cause for security concern. DNS and URL hovering information leaks. |
| [[Jitsi -> https://jitsi.org]] | GNU/Linux, Windows, macOS | *Да* | Нет | *Да* | ? | *Да* | ? | ? | Open source. Написан на Java. |
| [[Miranda -> https://miranda-im.org]] | Windows | *Да* | Нет | Нет | ? | ? | ? | ? | Open source. Стабильный клиент со множеством плагинов. |
| [[Miranda NG -> https://miranda-ng.org]] | Windows | *Да* | Нет | Нет | ? | ? | ? | ? | Open source. Стабильный клиент со множеством плагинов. |
| [[Pidgin]] | GNU/Linux, Windows, macOS | *Да* (Plugin) | *Да* (Plugin) | *Да* (Linux) | *Да* | *Да* | *Да* | ? | Open source. Стабильный мессенджер со множеством функций. *Обязательно используйте самую свежую версию!* |
| [[Spark -> https://igniterealtime.org/projects/spark/]] | GNU/Linux, Windows, macOS | *Да* | Нет | *Да* | ? | ? | ? | ? | Open source. Написан на Java. |

h2. Клиенты, которых стоит избегать

table(table table-striped).
|_. Client |_. OS supportés |_. OTR? |_. OMEMO? |_. Jingle? |_. Proxy? |_. SSL/TLS? |_. Tor? |_. MUC? |_. Комментарии |
| [[Beem -> https://beem-project.com]] | Android | Нет | Нет | Нет | ? | ? | ? | ? | Open source. Не поддерживает групповые чаты. |
| [[Empathy -> https://wiki.gnome.org/Apps/Empathy]] | GNU/Linux | Нет | Нет | *Да* | *Да* (GNOME) | *Да* (GNOME) | ? | ? | Open source. Стабильный и простой в использовании. |
| [[iChat -> https://www.apple.com]] | macOS | No | No | No | ? | ? | ? | ? | Apple's built-in chat application has limited XMPP support. |
| [[Pandion -> https://pandion.im]] | Windows | Нет | Нет | Нет | ? | ? | ? | ? | Open source. Продолжительное время нет новых обновлений. |
