# Extracción de datos (scraping) en redes sociales
# Autor: Abén Aljama Martínez (03/04/2020)

from library import *

'''---------------------------------------------------------'''
''' FUNCIONES NECESARIAS DURANTE EL PROCESO DE WEB SCRAPING '''
'''---------------------------------------------------------'''

# Función que realiza login en una red social

def login(browser,social_network):
    
    # Extracción de la URL para hacer login de la red social
    url_login = social_network['URL']+social_network['URL_LOGIN']
    
    # Carga de la URL para hacer login de la red social
    browser.get(url_login)
    sleep(2)

    # Inserción del usuario en la caja de texto de la página de login de la red social
    
    '''TENGO QUE MODULARIZAR LO QUE SE PUEDA'''
    if social_network['ALIAS'] == 'linkedin':
        id_usuario = browser.find_element_by_id("username") #LINKEDIN
    elif social_network['ALIAS'] == 'instagram':
        id_usuario = browser.find_element_by_name('username') #INSTAGRAM
    
    id_usuario.send_keys(social_network['USER_LOGIN'])
    sleep(1)
    
    '''CÓDIGO INCONCLUSO: WAIT EXPLÍCITO SIN SLEEP'''

    # Inserción del password en la caja de texto de la página de login de la red social
    if social_network['ALIAS'] == 'linkedin':
        id_clave = browser.find_element_by_id("password") #LINKEDIN
    elif social_network['ALIAS'] == 'instagram':
        id_clave = browser.find_element_by_name('password') #INSTAGRAM
    
    id_clave.send_keys(social_network['PASSWORD_LOGIN'])
    sleep(1)

    # Pulsación del botón de envío de usuario y contraseña
    id_clave.submit()

    sleep(3)

    '''CÓDIGO PARA INSTAGRAM, VENTANA QUE SALE TRAS EL LOGIN'''
    if social_network['ALIAS'] == 'instagram':
        try:
            browser.find_element_by_xpath(XPATH_MISC['POPUP_LOGIN_BUTTON_INSTAGRAM']).click()
        except:    
            print('')
        else:
            sleep(1)

        '''CÓDIGO PARA INSTAGRAM, VENTANA QUE SALE TRAS EL LOGIN'''
        try:
            browser.find_element_by_xpath(XPATH_MISC['POPUP_LOGIN_BUTTON_INSTAGRAM_2']).click()
        except:    
            print('')
        else:
            sleep(1)

    '''DEBERÍA DEVOLVER TRUE O FALSE SI HACE O NO LOGIN'''

# Función que navega a la url del perfil de un usuario de una red social

def go_to_target(browser,social_network):

    url_target = social_network['URL']+social_network['URL_TARGET']+social_network['TARGET_ACCOUNT']
    browser.get(url_target)
    sleep(1)

# Función que exporta la información extraída a un formato específico

def export_to_file(extracted_info,export_format):
    
    # Obtención de la fecha y hora actual
    now = datetime.now()
    now_string = str(now.year)+'-'+str(now.month)+'-'+str(now.day)
    
    # Exportación de la información a un fichero de texto
    if export_format == 'txt':

        # Apertura para escritura del fichero
        try:
            info_file_name = APP_CONFIG['PATH_EXPORT_INFO']+now_string+'_info'
            info_file_name = info_file_name.replace('.','-')
            info_file_name = info_file_name + '.' +export_format
            APP_CONFIG['EXPORT_FILE'] = info_file_name
            
            info_file = open(APP_CONFIG['EXPORT_FILE'],'a',encoding=APP_CONFIG['CHARSET'])
        
        except:
            print(FILE_ERROR['NO_OPEN_FILE'])

        # Escritura en el fichero de la fecha y hora actual
        info_file.write('\n'+'-'*50)
        date_string = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        time_string = str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        info_file.write('\nInformación extraida el '+date_string+' a las '+time_string)
        info_file.write('\n'+'-'*50)

        # Escritura en el fichero de la red social
        info_file.write('\n\n'+extracted_info['SOCIAL_NETWORK'].upper())
        info_file.write('\n'+'.'*10+'\n')
     
        # Escritura en el fichero de la información extraída
        for fields,info in extracted_info.items():
            if fields != 'SOCIAL_NETWORK':
                info_file.write('\n* '+XPATH_TRANSLATE[fields]+' --> '+info+'\n')
        
        # Cierre del fichero
        try:
            info_file.close()
        except:
            print(FORM_ERROR['NO_CLOSE_FILE'])

######################
# Programa principal #
######################

# Llamada al script que abre el formulario para introducir los datos

try:
    open('form.py')
except:
    print('No ha podido ejecutarse form.py')
    exit()
else:
    subprocess.getstatusoutput('form.py')

# Inicio del contador de tiempo de ejecución de la aplicación
start_execution = time()

# Lista que almacenará los datos del fichero temporal
scraping_data = []

# Lectura de los datos del fichero temporal para extraerlos y almacenarlos en la lista
try:
    with open(APP_CONFIG['TEMP_INPUT_DATA_FILE'],'r',encoding=APP_CONFIG['CHARSET']) as temp_file:

        line_count = 1

        for file_line in temp_file:
        
            # La primera línea del fichero contiene el tipo de exportación
            if line_count == 1:
                APP_CONFIG['EXPORT_TYPE'] = file_line.rstrip('\n')
            else:
                split_data = file_line.split(sep=APP_CONFIG['DATA_FILE_SEPARATOR']) #Extracción de los datos
                split_data.pop() #Eliminación del carácter '\n'
                scraping_data.append(split_data)
            
            line_count +=1
        
except:
    exit()

# Borrado del fichero temporal
try:
    remove(APP_CONFIG['TEMP_INPUT_DATA_FILE'])
except:
    print(FILE_ERROR['NO_DELETE_FILE'])
else:
    temp_file.close()

# Almacenamiento de los datos de las redes sociales a scrapear en una lista
for soc_cfg in SOCIAL_CONFIG:
    for scr_dat in scraping_data:
        if scr_dat[0] == soc_cfg['ALIAS']:
            soc_cfg['TARGET_ACCOUNT']=scr_dat[1]
            soc_cfg['SCRAPING']='True'

            if scr_dat[1] != 0:
                soc_cfg['USER_LOGIN']=scr_dat[2]
                soc_cfg['PASSWORD_LOGIN']=scr_dat[3]
            else:
                soc_cfg['USER_LOGIN']=''
                soc_cfg['PASSWORD_LOGIN']=''


# Se abre una instancia del navegador que se haya configurado
web_browser = APP_CONFIG['BROWSER']
export_format = APP_CONFIG['EXPORT_TYPE']

if web_browser == 'chrome':
    browser = webdriver.Chrome()
elif web_browser == 'firefox':
    browser = webdriver.Firefox()
elif web_browser == 'edge':
    browser = webdriver.Edge()

system("cls")
        
# Scraping en cada una de las redes sociales seleccionadas

for social_network in SOCIAL_CONFIG:

    if social_network['SCRAPING'] == 'True':
        
        print('\n\nRealizando scraping en '+social_network['NAME']+'.....')

        # Se intenta hacer login en la red social, si se ha insertado usuario
        # En función de si se ha hecho o no login, extraerá una u otra información
        if social_network['USER_LOGIN'] == '0': 
            log_in = 'NO'
        else: 
            log_in = ''
            login(browser,social_network)
        
        # Se visita el perfil del usuario objetivo
        go_to_target(browser,social_network)

        # Se muestra por pantalla la información extraída de la red social
        target_profile = social_network['TARGET_ACCOUNT']
        print('\nInformación extraída de:'+target_profile+'\n')
        
        xpath_social_network = globals()['XPATH_'+log_in+'LOGIN_'+social_network['ALIAS'].upper()]

        extracted_info = xpath_social_network

        for fields,xpaths in xpath_social_network.items():
            
            try:
                if fields == 'PROFILE_IMAGE':
                    
                    info = browser.find_element_by_xpath(xpaths)

                    try:
                        profile_image_name = APP_CONFIG['PATH_PROFILE_IMAGE']+social_network['TARGET_ACCOUNT']+'_'+social_network['ALIAS']+'_profile.png'
                        
                        with open(profile_image_name,'wb') as file_image:
                            file_image.write(info.screenshot_as_png)
                        
                        info = profile_image_name

                    except:
                        print(FILE_ERROR['NO_READ_WRITE_FILE'])

                else:
                    info = browser.find_element_by_xpath(xpaths).text
            except:
                if fields == 'PROFILE_IMAGE':
                    info = SCRAPING_ERROR['NO_AVAILABLE_IMAGE']
                else:
                    info = SCRAPING_ERROR['NO_AVAILABLE_INFO']
            else:
                print(XPATH_TRANSLATE[fields]+'-->'+info)

            extracted_info[fields] = info

        extracted_info['SOCIAL_NETWORK'] = social_network['ALIAS']

        try:
            if extracted_info['ACCOUNT'] == '':
                extracted_info['ACCOUNT'] = social_network['TARGET_ACCOUNT']

        except:
            extracted_info['ACCOUNT'] = social_network['TARGET_ACCOUNT']

        # Se procede a exportar la información extraída al formato elegido
        if APP_CONFIG['EXPORT_TYPE'] != 'none':
            export_to_file(extracted_info,APP_CONFIG['EXPORT_TYPE'])
            
if APP_CONFIG['EXPORT_TYPE'] != 'none':
    print('\nInformación extraída --> '+APP_CONFIG['EXPORT_FILE'])                    
        
# Visualización por pantalla del tiempo de ejecución del web scraping
execution_time = time() - start_execution
print ('\nFin de la ejecución. Tiempo: %.10f segundos' % execution_time)
