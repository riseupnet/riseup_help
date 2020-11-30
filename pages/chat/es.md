@title = "Chat de Riseup"
@nav_title = "Chat"

h2. ¿Qué es XMPP?

XMPP es un estándar abierto para mensajería instantánea, voz y vídeo chat. Con XMPP puedes enviar y recibir mensajes entre distintos centenares de proveedores de chat.


h2. Usando el servicio de XMPP de Riseup.

Tu dirección de correo en riseup.net también te sirve para ocuparla en XMPP. Para enviarle un mensaje a alguien o solicitud de amistad, simplemente necesitas enviárselo a [@usuario@riseup.net@]

En orden de configurar un [[cliente de XMPP => chat/clients]], necesitas la siguiente información:

* *protocolo*: "xmpp"
* *cuenta*: [@usuario@riseup.net@]
* *contraseña*: tu [[contraseña de riseup => human-security/riseup-password]]

Es importante que cuando configures tu cliente, marques *siempre requerir encriptación*. Pues algunos clientes tienen la opción "encriptar si es posible". A pesar de que los servidores de riseup.net requieren encriptación, si tu cliente está configurado con "encriptar si es posible", un atacante puede fácilmente adquirir tu contraseña. 

Algunos clientes de XMPP te pedirán tu nombre de usuario y dominio por separado. En este caso, debes especificar:

* *nombre de usuario usuario*: [@nombredeusuario@]
* *dominio*: @riseup.net@

Para ver tutoriales específicos de distintos clientes, ve nuestra página [[XMPP clientes => chat/clients]]



h2. Conectándose a salas de chat multiusuario.

Cuando te conectes o crees una sala de chat en el servidor de XMPP de Riseup, la sintaxis debe ser:


* [@nombre-de-sala@conference.riseup.net@]

Si necesitas especificar la sala por separado, haz esto:

* sala: @nombre-de-sala@
* dominio: @conference.riseup.net@

NO uses esto:

* [@nombre-de-sala@riseup.net@]

h3. Usando salas de chat en Pidgin

Si estás conectado vía [[pidgin]], para unirte o crear una sala, ve a @Añadir un chat@ en el menú @Buddy@ ubicado en la ventana principal de pidgin.

* Sala: @nombre-de-sala@
* Servidor: @conference.riseup.net@
* Manipulador: @tu-nick@
* Contraseña: [opcional]
* Alias: [opcional]
* Grupo: [opcional]

Pincha en @Ok@ y mira tu lista de contactos. Deberías ver un grupo llamado @Chat@ y dentro de él la sala creada.
Luego click derecho sobre ella y selecciona @unir@. También puedes hacer doble click sobre el nombre de la sala.

Para probar, puedes seleccionar @riseup.net@ como nombre de sala y unirte.


h2. Para una mayor seguridad


Para una mayor seguridad, accede a nuestro servidor de XMPP vía la [[VPN Riseup] => vpn] o a través del "servicio oculto Tor"::https://www.torproject.org/docs/hidden-services.html.en. Puedes ver nuestra [[Página sobre tor->tor#riseups-tor-hidden-services]] para una lista completa de nodos ocultos.
