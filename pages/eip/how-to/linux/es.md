@nav_title = "Linux"
@title = "How to: Linux"
@summary = "Getting, Installing and Configuring the Bitmask client"

Para usar el nuevo sistema VPN de Riseup (Riseup EIP) necesitas una cuenta que funcione bajo LEAP. Puedes crear una desde Bitmask (el cliente de LEAP) o desde [https://black.riseup.net/signup](https://black.riseup.net/signup). **Recomendamos registrar tu cuenta desde Bitmask a menos que solo planees usar la VPN desde Android**.

## Obteniendo y Instalando Bitmask

La aplicación Bitmask para Linux se puede obtener de dos formas. Si usas Ubuntu o Debian puedes añadir el repositorio de software de Bitmask para mantener siempre tu versión actualizada. Alternativamente puedes descargar el bundle, el cual puedes ejecutar desde un dispositivo externo como una memoria usb. Ten encuenta que el bundle puede funcionar más lento, ocupará más espacio y estará menos integrado con el escritorio que la versión para Ubuntu/Debian. Además tendrás que actualizarlo manualmente. Por este motivo **recomendamos usar la versión de Ubuntu/Debian**.

### Ubuntu

Los pasos descritos acontinuación añadirán los repositorios de Bitmask para tu sistema. Estos comandos tienen que ser ejecutados dentro de tu aplicación de Terminal, uno por uno porque se te pedirá tu password de sudo. La información de los repositorios se almacenará en `/etc/apt/sources.list.d/bitmask.list`. 

#### Instalar en Trusty Thar (14.04)

    echo "deb http://deb.bitmask.net/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    curl https://dl.bitmask.net/apt.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install bitmask leap-keyring

#### Instalar en Saucy Salamander (13.10)

    echo "deb http://deb.bitmask.net/debian saucy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    curl https://dl.bitmask.net/apt.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install bitmask leap-keyring

#### Desinstalar

    sudo apt-get remove bitmask leap-keyring
    sudo apt-key del 0x1E34A1828E207901
    sudo rm /etc/apt/sources.list.d/bitmask.list

### Debian

#### Install on Wheezy (Debian 7)

You need to enable `wheezy-backports` as a software source. 

    echo "deb http://http.debian.net/debian wheezy-backports main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    echo "deb http://deb.bitmask.net/debian wheezy main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    curl https://dl.bitmask.net/apt.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install bitmask leap-keyring

#### Install on Jessie (Debian 8)

    echo "deb http://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    curl https://dl.bitmask.net/apt.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install bitmask leap-keyring

#### Install on Jessie using the Tor anonymizing network:

    sudo apt-get install apt-transport-tor
    echo "deb tor://deb.bitmask.net/debian jessie main" | sudo tee -a /etc/apt/sources.list.d/bitmask.list
    curl https://dl.bitmask.net/apt.key | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install bitmask leap-keyring

#### Desinstalar

    sudo apt-get remove bitmask leap-keyring
    sudo apt-key del 0x1E34A1828E207901
    sudo rm /etc/apt/sources.list.d/bitmask.list

### Stand-alone bundle

El bundle de Bitmask debería funcionar en las versiones recientes de Debian y sus derivados (Mint, Ubuntu, Elementary, etc). ¡Recuerda que te debes encargar de mantener el software actualizado!

Para obtener la versión correcta del bundle debemos determinar primero qué tipo de kernel tienes. Esto se puede hacer ejecutando el siguiente comando `ùname -m`

#### 64bits

Si el resultado de ese comando contiene 'x86_64' ó 'amd64' entonces debes descargar la última versión disponible desde [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2) y su firma OpenPGP desde [https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc). 

Puedes usar los siguientes comandos para descargar y verificar la autenticidad del bundle.

    gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
    curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2
    curl -O https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2.asc
    gpg --verify Bitmask-linux64-latest.tar.bz2.asc Bitmask-linux64-latest.tar.bz2

Si obtuviste 'Firma Correcta', 'Good signature' o 'Correct Signature' en la respuesta, descomprime con el siguiente comando:

    tar xfj https://dl.bitmask.net/client/linux/Bitmask-linux64-latest.tar.bz2

#### 32bits

Si el resultado de ese comando contiene 'i686' or 'i386' entonces debes descargar la última versión disponible desde [https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2](https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2) y su firma OpenPGP desde [https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc](https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc). 

Puedes usar los siguientes comandos para descargar y verificar la autenticidad del bundle.

    gpg --keyserver pool.sks-keyservers.net --recv-key "1E45 3B2C E87B EE2F 7DFE 9966 1E34 A182 8E20 7901"
    curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2
    curl -O https://dl.bitmask.net/client/linux/Bitmask-linux32-latest.tar.bz2.asc
    gpg --verify Bitmask-linux32-latest.tar.bz2.asc Bitmask-linux32-latest.tar.bz2

Si obtuviste 'Firma Correcta', 'Good signature' o 'Correct Signature' en la respuesta, descomprime con el siguiente comando:

    tar xfj Bitmask-linux32-latest.tar.bz2

## Usando Bitmask por primera vez

Cuando inicias Bitmask por primera vez necesitarás configurarlo con Riseup como un proveedor LEAP. Estos pasos te guiarán para hacerlo.

h3. Crear una cuenta LEAP en Riseup

![Step 1](linux/Bitmask-1.png)

Selecciona sign up for a new account y presiona el botón *next*.

![Step 2](linux/Bitmask-2.png)

Selecciona 'Configure a new provider' y escribe en el campo 'riseup.net'. Luego presiona el botón *check*.

![Step 3](linux/Bitmask-3.png)

Bitmask tiene que asegurarse que riseup.net es un proveedor válido. Si todo sale bien puedes presionar el botón *next* para continuar. Si hay un problema, por favor visita la sección Resolviendo Problemas en esta página.

![Step 4](linux/Bitmask-4.png)

Si todo salió bien verás esta pantalla. Presiona nuevamente *next*.

![Step 5](linux/Bitmask-5.png)

Bitmask tiene confirmar que se puede conectar de forma segura con riseup.net. Si todo sale bien puedes presionar el botón *next* para continuar. Si hay un problema, por favor visita la sección Resolviendo Problemas en esta página.

![Step 6](linux/Bitmask-6.png)

El siguiente paso es definir un nombre de usuario y contraseña para tu cuenta. ¡Asegúrate de recordarlos!

Recuerda que en esta etapa de la fase de prueba los nombres de usuarios actuales de riseup.net están reservados y no pueden ser ocupados. Así que debes crear uno sin miedo, es solo para este servicio.

![Step 6](linux/Bitmask-7.png)

Mensaje de confirmación. Puedes hacer que Bitmask recuerde tu nombre de usuario y contraseña. Si le dices que no, asegúrate de recordarlos!

![Step 7](linux/Bitmask-8.png)

Selecciona "Encrypted Internet" y Connect. Bienvenid· a la nueva VPN, Riseup EIP!

## Resolviendo Problemas

Ok, encontraste un fallo? Por favor indícanos dónde y así podremos resolver cualquier problema antes e abrir este servicio a tod·s!

### Algo no funciona... ¿Qué hago?

Lo primero es saber qué está causando el problema, para esto abre la aplicación Terminal y ejecuta el siguiente comando  `bitmask --debug --logfile /tmp/bitmask.log`. Esto hará correr Bitmask en modo debug y almacenará los posibles problemas en un fichero de texto en `/tmp/bitmask.log`. Si tú eres un/a usuari· avanzad· es posible que puedas ver dónde está el error... comunícanoslo!. Si no lo eres, por favor llena un ticket con el contenido de `/tmp/bitmask.log` y el sistema que ocupas (Debian Wheezy, Mint 17, Ubuntu Trusty, etc).

Para llenar un ticket de soporte, por favor visita [https://black.riseup.net/tickets/new](https://black.riseup.net/tickets/new). ¡Muchas gracias por su invaluable ayuda!

### Problemas que nos han reportado y posibles soluciones

#### ¡Mi usuario y password de riseup no funcionan!

En esta etapa de la beta, todos los nombres de usuarios actuales de riseup se encuentran reservados y no pueden ser utilizados. Necesitarás crear uno usando la aplicación Bitmask o en [https://black.riseup.net](https://black.riseup.net). No te preocupes, estas cuentas solo serán utilizadas durante el periodo beta y no serán usadas en ningún otro servicio. Siéntete libre de ocupar cualquier nombre de usuario.

#### Una ventana de "Configure Bitmask email Account" aparece cada vez que inicio Thunderbird/Icedove

Por algún motivo el paquete `xul-ext-bitmask` se instaló. Este paquete contiene la extensión para soportar LEAP como proveedor de Mail. Siéntete libre de eliminarla, solo ejecuta `sudo apt-get remove xul-ext-bitmask` y reinicia Thunderbird/Icedove. 