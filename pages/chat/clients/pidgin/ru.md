@title = 'Pidgin'

## О Pidgin

![logopidgin](logo.pidgin.png)

Pidgin - самый популярный IM клиент для GNU/Linux, Windows and  macOS. Вы можете скачать Pidgin с официального сайта https://pidgin.im/download. Для macOS, ознакомьтесь с [[Adium]], нативной сборкой Pidgin для macOS.

## Настройка учётной записи

При первом запуске Pidgin, нажмите `Добавить...` для того, чтобы добавить аккаунт.

(1) Во вкладке `Основные`, установите следующие значения:

![newaccountbasictab](new-account-basic-tab.png)

- `Протокол`: XMPP
- `Имя пользователя`: ваш Riseup юзернейм
- `Домен`: riseup.net
- `Пароль`: ваш [[riseup-password]]

При желании вы можете указать локальный псевдоним в качестве своего имени, при желании вы можете выбрать значок для себя. Другие люди увидят это в своем списке контактов и при общении с ними.

## Использование OTR

Подробнее об использовании end-to-end шифрования с помощью Pidgin смотрите в разделе [[otr]].

## Обеспечение безопасности в GNU/Linux с помощью ["AppArmor"](https://gitlab.com/apparmor/apparmor/wikis/home/)

Для дополнительной безопасности в системе GNU/Linux, мы рекомендуем защитить ваш Pidgin, выполнив следующие шаги:

- скопируйте usr.bin.pidgin в `/etc/apparmor.d/usr.bin.pidgin`
  * [usr.bin.pidgin for Ubuntu 14.04](https://bazaar.launchpad.net/~apparmor-dev/apparmor-profiles/master/view/head:/ubuntu/14.04/usr.bin.pidgin)
- перезапустите apparmor
`sudo /etc/init.d/apparmor restart`
- перезапустите Pidgin

## Использование Tor

(1) Меню `Учётные записи` > выбираете тебуемый аккаунт > `Изменить учётную запись`.

![pidginmodifyaccount](pidgin-modify-account.png)

(2) Перейдите на вкладку `Дополнительно` и установите следующие значения:

- `Безопасность соединения`: `Требовать шифрование`
- `Соединяться на порт*: `5222`
- `Соединяться с сервером`: в [[списке Riseups .onion services->tor#riseups-tor-hidden-services]] найдите `xmpp.*.onion`
- `Прокси передачи файлов`: `proxy.riseup.net`

(3) Перейдите на вкладку `Прокси`.

![pidginmodifyaccountproxy](pidgin-modify-account-proxy.png)

Установите следующие значения:

- `Тип прокси`: `Tor/Конфиденциальность (SOCKS5)`
- `Узел`: `127.0.0.1`
- `Порт`: `9050`
- `Имя пользователя`: `ваше-имя-пользователя`
- `Пароль`: ваш [[riseup-password]]
