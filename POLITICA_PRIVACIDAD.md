# Política de privacidad de EspacioGo

**Responsable:** Gabriel Rodríguez  
**Contacto:** gabow95k@gmail.com  
**Vigencia y última actualización:** 22 de noviembre de 2026  
**URL pública:** https://gaborohez.github.io/espaciogo-privacy/

## 1. Responsable y alcance

EspacioGo es una aplicación Android para administrar estacionamientos. El responsable del desarrollo y del contacto de privacidad es Gabriel Rodríguez. Puedes escribir a gabow95k@gmail.com.

Esta política explica el tratamiento de información de la aplicación y de esta página. El administrador de cada estacionamiento decide qué datos registra, quién puede acceder a ellos y cómo utiliza sus reportes. El desarrollador no recibe ni administra automáticamente los registros de esos negocios.

## 2. Información que se registra

La información operativa se guarda en el almacenamiento privado de la aplicación en el dispositivo Android. Según las funciones que utilices, puede incluir:

- Datos del estacionamiento: nombre, dirección escrita manualmente, teléfono, horario, logo, capacidad y cajones.
- Usuarios locales: nombre, nombre de usuario, rol, permisos y verificadores de contraseña y recuperación derivados con sal. No guardamos las contraseñas locales en texto legible.
- Vehículos y boletos: placa cuando corresponda, tipo, color, marca o modelo, cajón y piso, notas, folio, código QR o de barras y fechas de entrada y salida. Las bicicletas pueden registrarse sin placa.
- Clientes y pensiones: nombre, teléfono, placas, planes, vigencias, pagos y saldos registrados por el estacionamiento.
- Operación: tarifas, promociones, cobros, método de pago registrado, referencias escritas por el operador, movimientos de caja, cortes, reportes y auditoría.
- Preferencias locales: usuario recordado para el acceso, impresora seleccionada, carpeta y horario de respaldos, decisiones sobre estadísticas y avisos remotos y estado leído/no leído de los avisos.

Los pagos de estacionamiento con tarjeta o transferencia son registros de la operación. EspacioGo no procesa esos pagos bancarios ni solicita el número completo de tarjeta, CVV o claves bancarias.

## 3. Para qué se utiliza

Los datos se utilizan para registrar entradas y salidas, calcular importes, aplicar tarifas y beneficios, administrar clientes y pensiones, controlar los turnos y la caja, imprimir comprobantes, mostrar reportes y avisos, mantener trazabilidad y crear o restaurar respaldos.

La operación del estacionamiento funciona localmente y no se sincroniza con un servidor propio del desarrollador. No incorporamos anuncios. Los servicios opcionales de nube se describen a continuación. No vendemos los registros del estacionamiento.

### Servicios opcionales de Google

**Cuenta del propietario.** Si el propietario vincula voluntariamente su cuenta de Google, Firebase Authentication trata la identidad y los datos de perfil proporcionados por Google para autenticarlo. En Cloud Firestore guardamos su nombre, correo, identificador de Firebase, fecha de actualización y versión del registro. No sincronizamos con Firebase las cuentas de operadores ni sus verificadores de contraseña. Google también trata información técnica necesaria para autenticación y seguridad. Vincular Google no es necesario para crear las cuentas locales del estacionamiento.

**Respaldos en Google Drive.** Esta opción solicita acceso únicamente al espacio privado de EspacioGo (drive.appdata), no a tus demás documentos de Drive. Al crear un respaldo manual, Drive recibe el archivo cifrado, su nombre, tamaño y fecha. La clave del respaldo no se envía a Drive. Para recuperar una copia se necesita la misma cuenta de Google y la contraseña elegida; el desarrollador no puede recuperar esa contraseña. Los respaldos de Drive son independientes de la programación de copias locales.

**Estadísticas de uso.** Google Analytics es opcional y está desactivado al inicio, en versiones de desarrollo y en la demostración. Al entrar a Inicio solicitamos autorización una sola vez, explicando que las estadísticas sirven para conocer las pantallas más utilizadas y priorizar mejoras que simplifiquen la app. Recordamos tanto la aceptación como la negativa en el dispositivo; puedes continuar usando EspacioGo sin compartir estadísticas. Al autorizarlas se tratan eventos de pantallas, identificadores de instalación e información técnica de uso y dispositivo. Google puede deducir ubicación aproximada a partir de la conexión, aunque EspacioGo no use GPS. No añadimos nombres, correos, placas, importes ni texto de formularios a los eventos. No usamos identificadores de publicidad ni activamos personalización publicitaria. Puedes cambiar tu decisión en Privacidad y datos o en Cuenta y nube. Desactivar la opción detiene las nuevas mediciones; no elimina automáticamente los datos ya recibidos por Google. La decisión es independiente de vincular Google y de permitir notificaciones.

**Avisos remotos e identificador para soporte.** Los avisos remotos de EspacioGo se activan automáticamente con el primer inicio de sesión normal, sin necesidad de vincular una cuenta de Google. Firebase Cloud Messaging trata identificadores de instalación y tokens de registro para entregar mensajes del desarrollador. Los mensajes procesados se guardan en la bandeja local del último usuario que inició sesión y se muestran como notificaciones si Android lo permite. En Android 13 o posterior se solicita el permiso al iniciar sesión por primera vez; negar ese permiso impide la notificación del sistema, pero no desactiva por sí solo la recepción en la bandeja. Puedes desactivar los avisos remotos en Cuenta y nube, sin desactivar los avisos operativos locales. Los siguientes inicios de sesión respetarán esa elección. La entrega necesita Internet y puede retrasarse por restricciones de Android.

El administrador puede usar Cuenta y nube → Copiar identificador para soporte y compartir voluntariamente el token FCM de esa instalación con el responsable. Esto permite enviar un aviso a ese dispositivo, además de los avisos generales. El token se copia al portapapeles marcado como contenido sensible; la app no lo añade a los respaldos, a registros de diagnóstico ni a los perfiles de Firestore. Puede cambiar con el tiempo. Identifica una instalación, no una persona ni un operador concreto: un aviso dirigido al dispositivo puede verlo el último usuario local que inició sesión. No lo compartas públicamente ni envíes por este canal información confidencial de clientes. Si lo remites por correo, su tratamiento se rige también por el apartado de consultas de esta política.

Estos servicios son proporcionados por Google. Consulta https://firebase.google.com/support/privacy y https://policies.google.com/privacy. La operación del estacionamiento continúa siendo local; las funciones de nube necesitan conexión.

## 4. Permisos y funciones del dispositivo

- Cámara: se utiliza para leer el QR o código de barras de los boletos en el dispositivo. Las imágenes de la lectura no se guardan ni se envían al desarrollador.
- Bluetooth y dispositivos cercanos: permiten buscar y conectar una impresora y enviarle el contenido de los comprobantes. La configuración de la impresora se conserva localmente.
- Ubicación en Android 10 y 11: el sistema exige este permiso para descubrir dispositivos Bluetooth. Se solicita únicamente para esa búsqueda; EspacioGo no obtiene ni guarda coordenadas GPS. La dirección del negocio se escribe manualmente.
- Archivos e imágenes seleccionados: Android permite elegir un logo, una carpeta o un archivo concreto. El logo se copia al almacenamiento privado; los respaldos y exportaciones se guardan en el destino elegido.
- Notificaciones: si las autorizas, Android muestra avisos operativos, mensajes remotos de EspacioGo y el progreso o resultado de los respaldos. Pueden contener información del negocio o de su operación. Puedes configurar su visibilidad en los ajustes del sistema.

Puedes negar o revocar permisos desde los ajustes de Android. La lectura manual por placa o folio sigue disponible sin cámara, y los comprobantes pueden consultarse en pantalla sin impresora. Sin permiso de notificaciones, los avisos permanecen dentro de la app.

## 5. Respaldos, exportaciones e impresión

Los respaldos contienen datos operativos, usuarios, historial e identidad de los boletos. Se cifran con la contraseña elegida por el administrador mediante AES-256-GCM. La programación automática utiliza una clave protegida mediante Android Keystore, para ejecutar el trabajo autorizado sin pedir la contraseña en cada copia.

El administrador elige la carpeta de destino. Si selecciona un proveedor de almacenamiento en la nube, ese proveedor puede recibir el archivo y tratarlo conforme a sus condiciones. La vinculación de Google y los respaldos de Drive requieren una acción del propietario en Cuenta y nube.

Las exportaciones CSV y PDF son archivos legibles. Los comprobantes se envían a la impresora Bluetooth elegida y quedan también en el papel impreso. El administrador controla a quién entrega estos documentos. Borrar la app no elimina los respaldos, exportaciones o impresiones que existan por separado.

Las copias programadas se ejecutan mediante Android WorkManager. El sistema puede retrasarlas por ahorro de batería; después de forzar la detención de la app es necesario volver a abrirla para reactivar el trabajo.

## 6. Google Play y suscripciones

Google Play administra la compra, renovación, cancelación y ofertas de prueba de la suscripción de EspacioGo. Estas funciones y la consulta periódica de la licencia requieren conexión. En las versiones comerciales se consulta el acceso al iniciar sesión, al mostrar Inicio y al regresar a primer plano; también se programa una comprobación periódica sujeta a las restricciones de Android. La app conserva localmente evidencia de la compra y del estado de acceso, incluidos los datos necesarios para verificarla y las referencias de tiempo de la comprobación. Un fallo de conectividad no se registra por sí solo como falta de pago.

La elegibilidad y la duración de una oferta de prueba provienen de Google Play y de la cuenta que realiza la compra, no de crear otro usuario local, reinstalar o restaurar un respaldo. La prueba se activa al aceptar la oferta en Google Play y puede convertirse en una suscripción con cobro automático conforme a las condiciones que Google muestre antes de contratar.

Google y sus componentes de facturación tratan información de cuenta, transacción y datos técnicos relacionados con ese servicio conforme a sus propias condiciones y política de privacidad. EspacioGo no recibe el número completo de la tarjeta usada para pagar la suscripción y no envía los registros de vehículos, clientes o caja a Google Play para validar el acceso.

Puedes consultar la política de Google en https://policies.google.com/privacy. Desinstalar EspacioGo o borrar sus datos no cancela la suscripción: se administra en Google Play, en Pagos y suscripciones → Suscripciones.

## 7. Seguridad y acceso local

La app utiliza el almacenamiento privado de Android, roles y permisos de usuario, contraseñas locales representadas por verificadores derivados con sal y bloqueo de acceso. Al regresar a la app se solicita contraseña aunque se recuerde el nombre de usuario. Los respaldos se cifran con contraseña.

Estos controles no sustituyen la protección del teléfono y de los archivos que exportes. Protege el dispositivo con bloqueo de pantalla y conserva las contraseñas de respaldo y el código de recuperación en un lugar seguro. No los envíes por correo de soporte.

## 8. Conservación y eliminación

Los registros operativos permanecen en el dispositivo mientras el administrador conserve la información. Eliminar o desactivar operadores, clientes, promociones u horarios en la app puede conservar su historial y referencias para trazabilidad; no equivale a borrar físicamente todos los registros relacionados.

Para eliminar toda la información local, el propietario del dispositivo puede utilizar Ajustes de Android → Aplicaciones → EspacioGo → Almacenamiento → Borrar datos, o desinstalar la app. Esto elimina también las cuentas locales y la configuración. Revisa antes si necesitas conservar un respaldo.

Los respaldos y reportes guardados fuera de la app se eliminan por separado en el almacenamiento o proveedor correspondiente. El desarrollador no puede borrar a distancia información que sólo existe en el dispositivo, en archivos del administrador o en tickets impresos. Restaurar un respaldo vuelve a incorporar los datos contenidos en él.

### Eliminación del perfil de la nube

Puedes eliminar el perfil remoto desde Ajustes → Cuenta y nube → Eliminar perfil de la nube; se eliminan el documento del propietario en Firestore y su cuenta de Firebase Authentication. Google puede pedirte volver a identificarte. Desvincular solo cierra el acceso y conserva el perfil remoto. Estas acciones no eliminan los registros operativos locales, respaldos de Drive ni la suscripción de Google Play. Tampoco cambian por sí solas las preferencias independientes de estadísticas y avisos remotos.

También puedes solicitar la eliminación del perfil remoto fuera de la app escribiendo desde el correo de Google vinculado a gabow95k@gmail.com con el asunto “Eliminar perfil de EspacioGo”. Para verificar la titularidad podemos pedirte confirmar la solicitud; no envíes contraseñas ni respaldos. Revisaremos la solicitud y verificaremos su titularidad antes de eliminar el perfil; conservaremos únicamente la información que corresponda a obligaciones aplicables. Los respaldos de Drive pueden eliminarse desde la administración de aplicaciones de Google Drive; los archivos descargados y reportes se borran por separado. Google conserva registros técnicos según las condiciones del servicio correspondiente.

La cuenta y los datos de facturación de Google Play se gestionan con Google.

## 9. Consultas, correcciones y solicitudes

Si tus datos fueron registrados por un estacionamiento, solicita al administrador de ese lugar su consulta, corrección o eliminación; él controla la base local y sus archivos. Para consultas sobre esta política o el funcionamiento de la app, escribe a gabow95k@gmail.com.

Si nos contactas por correo, utilizaremos tu dirección y el contenido que envíes para atender la consulta y conservaremos esa correspondencia durante el tiempo necesario para resolverla y atender obligaciones aplicables. Puedes solicitar su eliminación por el mismo medio. No adjuntes información de clientes, contraseñas ni respaldos para una consulta general.

## 10. Público de la aplicación

EspacioGo es una herramienta de administración de estacionamientos y no está dirigida al público infantil. El administrador debe limitar los datos que registra a los necesarios para prestar su servicio.

## 11. Privacidad de esta página

Esta página se aloja en GitHub Pages. No añadimos formularios, publicidad, cookies de seguimiento ni herramientas de analítica. GitHub puede registrar direcciones IP y otra información técnica para servir y proteger el sitio, conforme a su Declaración de privacidad: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement.

La app muestra esta página en un WebView mediante HTTPS. Al cargarla, GitHub recibe la solicitud y los datos técnicos normales de la conexión; EspacioGo no añade a ella registros del estacionamiento, credenciales locales ni tokens de notificaciones. Si no puede cargar la página, muestra una copia de esta política incluida en la app y señala que se trata de esa copia. Los enlaces a otros sitios o al correo de contacto se abren en la aplicación externa correspondiente.

Abrir un enlace externo o escribir al correo de contacto implica utilizar el servicio correspondiente, sujeto también a sus propias condiciones.

## 12. Cambios y contacto

Si cambian las funciones o el tratamiento de datos, actualizaremos esta política y su fecha de vigencia. La versión vigente estará disponible en esta dirección pública y accesible desde EspacioGo.

Responsable: Gabriel Rodríguez. Contacto de privacidad: gabow95k@gmail.com. Vigencia y última actualización: 22 de noviembre de 2026.

