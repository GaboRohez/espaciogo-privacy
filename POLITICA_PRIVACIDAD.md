# Política de privacidad de EspacioGo

**Responsable:** Gabriel Rodríguez  
**Contacto:** gabow95k@gmail.com  
**Vigencia y última actualización:** 14 de noviembre de 2026  
**URL pública:** https://gaborohez.github.io/espaciogo-privacy/

## 1. Responsable y alcance

EspacioGo es una aplicación Android para administrar estacionamientos. El responsable del desarrollo y del contacto de privacidad es Gabriel Rodríguez. Puedes escribir a gabow95k@gmail.com.

Esta política explica el tratamiento de información de la aplicación y de esta página. El administrador de cada estacionamiento decide qué datos registra, quién puede acceder a ellos y cómo utiliza sus reportes. El desarrollador no recibe ni administra automáticamente los registros de esos negocios.

## 2. Información que se registra

La información operativa se guarda en el almacenamiento privado de la aplicación en el dispositivo Android. Según las funciones que utilices, puede incluir:

- Datos del estacionamiento: nombre, dirección escrita manualmente, teléfono, horario, logo, capacidad y cajones.
- Usuarios locales: nombre, nombre de usuario, rol, permisos y verificadores de contraseña y recuperación derivados con sal. No guardamos las contraseñas locales en texto legible.
- Vehículos y boletos: placa, tipo, color, modelo, cajón, notas, folio, código QR y fechas de entrada y salida.
- Clientes y pensiones: nombre, teléfono, placas, planes, vigencias, pagos y saldos registrados por el estacionamiento.
- Operación: tarifas, promociones, cobros, método de pago registrado, referencias escritas por el operador, movimientos de caja, cortes, reportes y auditoría.
- Preferencias locales: usuario recordado para el acceso, impresora seleccionada, carpeta y horario de respaldos y estado leído/no leído de los avisos.

Los pagos de estacionamiento con tarjeta o transferencia son registros de la operación. EspacioGo no procesa esos pagos bancarios ni solicita el número completo de tarjeta, CVV o claves bancarias.

## 3. Para qué se utiliza

Los datos se utilizan para registrar entradas y salidas, calcular importes, aplicar tarifas y beneficios, administrar clientes y pensiones, controlar los turnos y la caja, imprimir comprobantes, mostrar reportes y avisos, mantener trazabilidad y crear o restaurar respaldos.

La operación del estacionamiento funciona localmente y no se sincroniza con un servidor propio del desarrollador. No incorporamos anuncios ni herramientas propias de analítica de uso. No vendemos los registros del estacionamiento.

## 4. Permisos y funciones del dispositivo

- Cámara: se utiliza para leer el QR de los boletos en el dispositivo. Las imágenes de la lectura no se guardan ni se envían al desarrollador.
- Bluetooth y dispositivos cercanos: permiten buscar y conectar una impresora y enviarle el contenido de los comprobantes. La configuración de la impresora se conserva localmente.
- Ubicación en Android 10 y 11: el sistema exige este permiso para descubrir dispositivos Bluetooth. Se solicita únicamente para esa búsqueda; EspacioGo no obtiene ni guarda coordenadas GPS. La dirección del negocio se escribe manualmente.
- Archivos e imágenes seleccionados: Android permite elegir un logo, una carpeta o un archivo concreto. El logo se copia al almacenamiento privado; los respaldos y exportaciones se guardan en el destino elegido.
- Notificaciones: si las autorizas, Android muestra avisos operativos y el progreso o resultado de los respaldos. Pueden contener información del negocio o de su operación. Puedes configurar su visibilidad en los ajustes del sistema.

Puedes negar o revocar permisos desde los ajustes de Android. La lectura manual por placa o folio sigue disponible sin cámara, y los comprobantes pueden consultarse en pantalla sin impresora. Sin permiso de notificaciones, los avisos permanecen dentro de la app.

## 5. Respaldos, exportaciones e impresión

Los respaldos contienen datos operativos, usuarios, historial e identidad de los boletos. Se cifran con la contraseña elegida por el administrador mediante AES-256-GCM. La programación automática utiliza una clave protegida mediante Android Keystore, para ejecutar el trabajo autorizado sin pedir la contraseña en cada copia.

El administrador elige la carpeta de destino. Si selecciona un proveedor de almacenamiento en la nube, ese proveedor puede recibir el archivo y tratarlo conforme a sus condiciones. La app no crea por sí sola una cuenta de nube ni un servicio propio de almacenamiento remoto.

Las exportaciones CSV y PDF son archivos legibles. Los comprobantes se envían a la impresora Bluetooth elegida y quedan también en el papel impreso. El administrador controla a quién entrega estos documentos. Borrar la app no elimina los respaldos, exportaciones o impresiones que existan por separado.

Las copias programadas se ejecutan mediante Android WorkManager. El sistema puede retrasarlas por ahorro de batería; después de forzar la detención de la app es necesario volver a abrirla para reactivar el trabajo.

## 6. Google Play y suscripciones

Google Play administra la compra, renovación, cancelación y ofertas de prueba de la suscripción de EspacioGo. Estas funciones y la consulta periódica de la licencia requieren conexión. La app conserva localmente información de la compra y del estado de acceso para validar la suscripción.

Google y sus componentes de facturación tratan información de cuenta, transacción y datos técnicos relacionados con ese servicio conforme a sus propias condiciones y política de privacidad. EspacioGo no recibe el número completo de la tarjeta usada para pagar la suscripción y no envía los registros de vehículos, clientes o caja a Google Play para validar el acceso.

Puedes consultar la política de Google en https://policies.google.com/privacy. Desinstalar EspacioGo o borrar sus datos no cancela la suscripción: se administra en Google Play, en Pagos y suscripciones → Suscripciones.

## 7. Seguridad y acceso local

La app utiliza el almacenamiento privado de Android, roles y permisos de usuario, contraseñas locales representadas por verificadores derivados con sal y bloqueo de acceso. Al regresar a la app se solicita contraseña aunque se recuerde el nombre de usuario. Los respaldos se cifran con contraseña.

Estos controles no sustituyen la protección del teléfono y de los archivos que exportes. Protege el dispositivo con bloqueo de pantalla y conserva las contraseñas de respaldo y el código de recuperación en un lugar seguro. No los envíes por correo de soporte.

## 8. Conservación y eliminación

Los registros operativos permanecen en el dispositivo mientras el administrador conserve la información. Eliminar o desactivar operadores, clientes, promociones u horarios en la app puede conservar su historial y referencias para trazabilidad; no equivale a borrar físicamente todos los registros relacionados.

Para eliminar toda la información local, el propietario del dispositivo puede utilizar Ajustes de Android → Aplicaciones → EspacioGo → Almacenamiento → Borrar datos, o desinstalar la app. Esto elimina también las cuentas locales y la configuración. Revisa antes si necesitas conservar un respaldo.

Los respaldos y reportes guardados fuera de la app se eliminan por separado en el almacenamiento o proveedor correspondiente. El desarrollador no puede borrar a distancia información que sólo existe en el dispositivo, en archivos del administrador o en tickets impresos. Restaurar un respaldo vuelve a incorporar los datos contenidos en él.

No existe una cuenta remota de EspacioGo en un servidor del desarrollador. La cuenta y los datos de facturación de Google Play se gestionan con Google.

## 9. Consultas, correcciones y solicitudes

Si tus datos fueron registrados por un estacionamiento, solicita al administrador de ese lugar su consulta, corrección o eliminación; él controla la base local y sus archivos. Para consultas sobre esta política o el funcionamiento de la app, escribe a gabow95k@gmail.com.

Si nos contactas por correo, utilizaremos tu dirección y el contenido que envíes para atender la consulta y conservaremos esa correspondencia durante el tiempo necesario para resolverla y atender obligaciones aplicables. Puedes solicitar su eliminación por el mismo medio. No adjuntes información de clientes, contraseñas ni respaldos para una consulta general.

## 10. Público de la aplicación

EspacioGo es una herramienta de administración de estacionamientos y no está dirigida al público infantil. El administrador debe limitar los datos que registra a los necesarios para prestar su servicio.

## 11. Privacidad de esta página

Esta página se aloja en GitHub Pages. No añadimos formularios, publicidad, cookies de seguimiento ni herramientas de analítica. GitHub puede registrar direcciones IP y otra información técnica para servir y proteger el sitio, conforme a su Declaración de privacidad: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement.

Abrir un enlace externo o escribir al correo de contacto implica utilizar el servicio correspondiente, sujeto también a sus propias condiciones.

## 12. Cambios y contacto

Si cambian las funciones o el tratamiento de datos, actualizaremos esta política y su fecha de vigencia. La versión vigente estará disponible en esta dirección pública y accesible desde EspacioGo.

Responsable: Gabriel Rodríguez. Contacto de privacidad: gabow95k@gmail.com. Vigencia y última actualización: 14 de noviembre de 2026.

