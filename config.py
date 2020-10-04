#Propiedades de la ventana principal
MAIN_WINDOWS_CONFIG = {

    #Propiedades de la ventana principal
    'SIZE' : '560x380+600+300', #anchoxalto+X+Y
    'TITLE' : 'Web Scraping',
    'BG_COLOR' : 'lightgrey',
}

#Propiedades y formato de los elementos del formulario
FORM_CONFIG = {

    'BG_COLOR' : 'lightgrey',

    #Propiedades y formato del título
    'FONT_TITLE' : 'Arial', 'SIZE_TITLE' : '20', 'WIDTH_TITLE' : '800', 'COLOR_TITLE' : 'white', 'BG_TITLE' : 'black', 'TEXT_TITLE' : 'Web Scraping',
    
    #Propiedades y formato de las imágenes (logotipos)
    'WIDTH_IMAGE' : '20','HEIGHT_IMAGE' : '20',
    
    #Propiedades y formato de los labels (etiquetas) superiores
    'TARGET_LABEL_TEXT' : 'Target','USER_LABEL_TEXT' : 'User (login)','PASSWORD_LABEL_TEXT' : 'Password',

    #Propiedades y formato de los inputs (cajas de texto) y botones
    'WIDTH_INPUT' : 118, 'HEIGHT_INPUT' : 25, 'WIDTH_BUTTON' : '10','HEIGHT_BUTTON' : '2','BGCOLOR_BUTTON' : 'grey','TEXT_SUBMIT' : 'Scraping','TEXT_RESET' : 'Reset',
    'WIDTH_TARGET_CHECK_BUTTON' : 15, 'HEIGHT_TARGET_CHECK_BUTTON' : 25, 'BGCOLOR_TARGET_CHECK_BUTTON' : 'black', 'TEXT_COLOR_TARGET_CHECK_BUTTON' : 'white',

    #Propiedades y formato de los labels (etiquetas) del check
    'TARGET_CHECK_LABEL_TEXT_OK' : 'V', 'TARGET_CHECK_LABEL_TEXT_NO' : 'X',   

    #Coordenadas de posición de los elementos del formulario
    'X_IMAGE' : 30, 'X_CHECK' : 60,'X_TARGET' : 100,'X_USER' : 250,'X_PASSWORD' : 400,'X_SUBMIT' : 190,'X_RESET' : 290,
    'Y_HEADERS' : 70,'Y_SOCIAL_NETWORK' : 100,'Y_SOCIAL_NETWORK_LOGO' : 98,'Y_BUTTON' : 310,
    'Y_OFFSET' : 40, 'Y_OFFSET_LOGO' : 2,
    'X_TARGET_CHECK_BUTTON' : 220, 'X_TARGET_CHECK' : 230,
    'X_EXPORT_LABEL' : 30, 'Y_EXPORT_LABEL' : 260,
    'X_EXPORT_MENU' : 170, 'Y_EXPORT_MENU' : 260,
    'X_ERROR_LABEL' : 20, 'Y_ERROR_LABEL' : 10
}

#Propiedades de la ventana de error
ERROR_WINDOWS_CONFIG = {
    'SIZE' : '400x50+700+450',
    'TITLE' : 'Error',
    'BGCOLOR' : 'lightgrey'}

#Configuración de redes sociales
SOCIAL_CONFIG =[
    
    # LinkedIn
    {'ALIAS':'linkedin',
    'NAME':'LinkedIn',
    'URL':'https://www.linkedin.com',
    'URL_LOGIN':'/login/',
    'URL_TARGET':'/in/',
    'SCRAPING':'False'},

    # Instagram
    {'ALIAS':'instagram',
    'NAME':'Instagram',
    'URL':'https://www.instagram.com',
    'URL_LOGIN':'/accounts/login/',
    'URL_TARGET':'/',
    'SCRAPING':'False'},

    # Twitter
    {'ALIAS':'twitter',
    'NAME':'Twitter',
    'URL':'https://twitter.com',
    'URL_LOGIN':'/login/',
    'URL_TARGET':'/',
    'SCRAPING':'False'},

    # Facebook
    {'ALIAS':'facebook',
    'NAME':'Facebook',
    'URL':'https://www.facebook.com',
    'URL_LOGIN':'/login/',
    'URL_TARGET':'/',
    'SCRAPING':'False'}
]

#Configuraciones generales de la aplicación
APP_CONFIG = {
    'CHARSET' : 'utf-8',
    'PATH_IMAGE' : 'img/',
    'PATH_PROFILE_IMAGE' : 'profile_images/',
    'PATH_EXPORT_INFO' : 'profile_info/',
    'TEMP_INPUT_DATA_FILE' : 'temp_input_data_scraping.txt',
    'DATA_FILE_SEPARATOR' : '#####',
    'EXPORT_TYPE' : 'none',
    'EXPORT_FILE' :'',
    'BROWSER' : 'chrome'
}

#Formatos de exportación permitidos
EXPORT_FORMAT = {
    'txt' : 'TXT',
    'none' : 'Ninguno'
}

#Errores
FORM_ERROR = {
    'NO_SOCIAL_NETWORK_SELECTED' : 'No ha seleccionado ninguna red social',
    'NO_TARGET' : 'Introduzca un perfil objetivo',
    'NO_TARGET_EXIST' : 'No se pudo acceder al perfil objetivo:',
    'NO_USER' : 'Introduzca un usuario para iniciar sesión',
    'NO_PASSWORD' : 'Introduzca una contraseña para el usuario'
}

FILE_ERROR = {
    'NO_OPEN_FILE' : 'Error en la apertura de fichero',
    'NO_READ_WRITE_FILE' : 'Error en la lectura/escritura del fichero',
    'NO_WRITE_FILE' : 'Error en la escritura del fichero',
    'NO_CLOSE_FILE' : 'Error en la clausura del fichero',
    'NO_DELETE_FILE' : 'Error en la eliminación del fichero'
}

SCRAPING_ERROR = {
    'NO_AVAILABLE_INFO' : 'Información no disponible',
    'NO_AVAILABLE_IMAGE' : 'Imagen de perfil no disponible'
}

MISC_ERROR = {
    'NO_HTTP_RESPONSE' : 'El sitio web no responde o no hay conexión a internet'
}