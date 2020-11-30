@title = 'Pidgin'

## Acerca de Pidgin

![logopidgin](logo.pidgin.png)

Pidgin es el cliente de mensajeria instantanea mas popular para GNU/Linux, Windows y macOS. Tu puedes descargar Pidgin desde  https://pidgin.im/download. Para Mac utiliza [[Adium]], la compilación nativa de pidgin para Mac.

## Configurando una cuenta

Cuando inicias por primera vez pidgin, dale click en el botón `Añadir...` para agregar una cuenta.

(1) En la pestaña `básica`, escribe estos valores:

![newaccountbasictab](new-account-basic-tab.png)

- `Protocolo`: XMPP
- `Nombre de usuario`: tu nombre de usuario de Riseup
- `Dominio`: riseup.net
- `Contraseña`: tu [[riseup-password]]

Opcionalmente, escribe un apodo local para que sea tu nombre, y añade un icono para ti. Otras personas veran este icono en su cliente XMPP.

## Usando OTR

Mira el tutorial [[otr]] para detalles sobre usar cifrado punto a punto con Pidgin.

## Asegurando pidgin en GNU/Linux con ["AppArmor"](https://gitlab.com/apparmor/apparmor/wikis/home/)

Para seguridad adicional en sistemas Linux, te recomendamos proteger tu pidgin usando estos pasos::

- copia usr.bin.pidgin a `/etc/apparmor.d/usr.bin.pidgin`
  * [usr.bin.pidgin for Ubuntu 14.04](https://bazaar.launchpad.net/~apparmor-dev/apparmor-profiles/master/view/head:/ubuntu/14.04/usr.bin.pidgin)
- reinicia apparmor
`sudo /etc/init.d/apparmor restart`
- reinicia pidgin

## Configuración de Pidgin con Tor

Para configurar que pidgin use Tor, necesitas modificar tus preferencias de esta forma:

Primero escoge `Modificar Preferencias de Cuenta`...

![pidginmodifyaccount](pidgin-modify-account.png)

enseguida da click en la pestaña de `Avanzadas` y establece los siguientes valores:

- `Seguridad de la conexión`: Solicitar cifrado
- `Puerto de conexión`: 5222
- `Conectar con el Servidor`: [[Página sobre tor->tor#riseups-tor-hidden-services]]
- `Pasarelas de transferencia de archivos`: proxy.riseup.net

Enseguida da click en la pestaña `Pasarela`...

![pidginmodifyaccountproxy](pidgin-modify-account-proxy.png)

Establece el tipo de proxy en `Socks5`, establece el servidor y el puerto como se muestra en la imagen y pon tu nombre de usuario y contraseña.
