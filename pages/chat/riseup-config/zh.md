@title = "Riseup Chat"
@nav_title = "Riseup config"

## 什么是XMPP？

XMPP是一种开放标准，用于即时消息以及语音和视频聊天。使用 XMPP，你可以给在上千个不同的聊天提供商的用户发送和接收消息。

## 使用 Riseup's XMPP服务

您的 riseup.net 电子邮箱地址同时也是您的 XMPP地址。给你发送 XMPP信息或者好友请求，只需要把他发送到 `username@riseup.net`.

为了配置 [[XMPP client => chat/clients]]，你需要一下信息：

- **protocol**: "xmpp"
- **account**: `username@riseup.net`
- **password**: your [[riseup-password]]

没有比你配置你的客户端*总是需要加密*更重要的了。有些客户端有一个设置“加密（如果可用）”。尽管riseup.net服务器需要加密，如果您的客户端被配置为使用“加密（如果可用）”，攻击者可以很容易地获取您的密码。

一些 XMPP客户端会单独询问您的用户名和域名，在这种情况下，您应该指定：

- **username**: `username`
- **domain**: `riseup.net`

有关特定客户端的手册，查看我们的 [[XMPP client => chat/clients]]页面。

## 连接到多用户聊天室

当在Riseup的“XMPP network”连接或者创建聊天室，语法应该是：

- `your-room-name@conference.riseup.net`

如果您需要分别指定房间，这样做：

- chatroom: `your-room-name`
- domain: `conference.riseup.net`

不要这样:

- `your-room-name@riseup.net`

### 在 Pidgin使用聊天室

如果您通过 [[pidgin]]连接、加入或者创建一个聊天室，在 @Buddy@菜单点击  `Add room`

- Room: `your-room-name`
- Server: `conference.riseup.net`
- Handle: `your-nick`
- Password: [optional]
- Alias: [optional]
- Group: [optional]

点击 `Ok`查看好友列表。在您的聊天室，您会看到一个 `Chat` 组。
右击它并选择 `join`。

为了测试，您可以选择 `riseup.net` 作为房间名称并加入。

## 增加安全性

为了增加安全性，通过 [[Riseup VPN => vpn]]或者 ["Tor hidden service"](https://www.torproject.org/docs/hidden-services.html.en): [[Riseup's hidden Tor services->tor#riseups-tor-hidden-services]] 访问我们的 XMPP服务器 。
