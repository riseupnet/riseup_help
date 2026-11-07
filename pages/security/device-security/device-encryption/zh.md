@title = "设备加密"
@toc = true
@summary = "为什么要加密设备存储，以及怎么做"

# 为什么要使用设备加密？

启用设备加密后，设备存储中的内容——包括操作系统、你安装的程序和个人数据——会被打乱。设备关机或你注销登录时，这些内容就无法被读取。

如果不启用设备加密，那么一旦有人偷走你的设备、捡到你丢失的设备，或以其他方式接触你的硬件，他们就能轻易读取你的文件、进入你的在线账户，并冒充你。更糟的是，攻击者还可以安装恶意软件，远程监控你的一切活动。

# 如何启用设备加密

虽然有些移动设备默认启用了全盘加密，但所有笔记本电脑和台式机，以及许多手机和平板，都需要手动设置。

台式机和笔记本操作指南：

* **Windows**：[Security Planner / Windows 加密](https://securityplanner.org/#/tool/windows-encryption)
   * 重要：微软默认会把你的设备加密密钥备份到云端。这意味着微软以及任何与其合作的政府都能轻易解密你的设备。如果你担心国家政府可能获取你设备中的内容，应该立即关闭这个“功能”，并[[生成新的加密密钥 => https://theintercept.com/2015/12/28/recently-bought-a-windows-computer-microsoft-probably-has-your-encryption-key/]]。
* **macOS**：[Security Planner / Mac 加密](https://securityplanner.org/#/tool/mac-encryption)
* **Linux**：几乎所有 Linux 发行版都允许你在安装系统时启用设备加密。主要有两种类型：
   * “全盘”加密：这种方式会加密设备主存储上的所有内容，包括操作系统。设备开机时，系统会要求你输入一个单独的密码。
   * “主目录”加密：这种方式**不会**加密操作系统。它可以保护你的个人数据，但攻击者一旦能接触你的设备，就更容易安装恶意软件。

移动设备操作指南：

* **iOS**：[Security Planner / Apple iOS 加密](https://securityplanner.org/#/tool/apple-ios-encryption)
* **Android**：[Security Planner / Android 设备加密](https://securityplanner.org/#/tool/android-device-encryption)

# 设备加密的注意事项

**局限性**：设备加密并不总是有效！如果你的[[密码 => passwords]]不够复杂，电脑可以轻易猜出密码并解锁设备。另外，设备加密无法防范病毒和恶意软件。如果你的数据被复制到基于云的备份服务，而该服务被入侵或与政府合作，那么设备加密也保护不了这些数据（除非该服务明确支持“客户端”加密）。

**必须启用身份验证**：如果设备不要求身份验证就能使用，设备加密就不会生效。例如，使用笔记本电脑时必须登录，使用移动设备时必须输入 PIN 码。

**会让磁盘恢复变得不可能**：如果没有可靠的密码或 PIN 码管理习惯，全盘加密也可能增加你永久失去部分信息的风险。忘记密码或 PIN 码，或者存储加密密钥的那部分磁盘发生故障，通常就意味着你（以及其他人）无法恢复数据。请定期备份数据，把数据丢失的风险降到最低。

**设备必须关机或锁定**：设备加密只在你关机，或者开机但尚未输入密码启动时提供保护。一旦你登录，电脑内存里就有解密数据所需的密钥；因此即使屏幕已锁定，设备运行（甚至睡眠）时仍存在有人获取电脑内容的风险。不过一般来说，绕过这些控制属于技术含量很高的攻击，你不必因为这种风险就不敢在需要工作时让电脑保持开机或登录。但是，当你把设备留在敌对环境中、设备可能离开你身边时，最好把它关机。如果你担心自己可能成为攻击目标，最好让设备时刻不离身。

# 另见

* [Security In-a-box / 安全的文件存储](https://securityinabox.org/en/guide/secure-file-storage/)
* [Security Planner / Windows 加密](https://securityplanner.org/#/tool/windows-encryption)
* [Security Planner / Mac 加密](https://securityplanner.org/#/tool/mac-encryption)
* [Security Planner / Apple iOS 加密](https://securityplanner.org/#/tool/apple-ios-encryption)
* [Security Planner / Android 设备加密](https://securityplanner.org/#/tool/android-device-encryption)
* [《监视自卫指南》/ 如何加密你的 iPhone](https://ssd.eff.org/en/module/how-encrypt-your-iphone)
