# Importación de librerías
from library import *

'''----------------------------------------------------------------------------------------'''
''' FUNCIONES NECESARIAS PARA EL FUNCIONAMIENTO DEL FORMULARIO INICIAL DE ENTRADA DE DATOS '''
'''----------------------------------------------------------------------------------------'''

# Función que establece las propiedades de configuración de la ventana principal

def set_form_windows(form_windows):
    
    form_windows.geometry(MAIN_WINDOWS_CONFIG['SIZE']) #Dimensiones de la ventana
    form_windows.title(MAIN_WINDOWS_CONFIG['TITLE']) #Título de la ventana
    form_windows.resizable(False,False) #Se permite o no cambiar el título de la ventana
    form_windows.config(background = MAIN_WINDOWS_CONFIG['BG_COLOR']) #Color de fondo de la ventana

# Función que establece las propiedades de configuración de la ventana de errores

def open_error_windows(error_text): 
    
    error_windows = Tk()
    error_windows.geometry(ERROR_WINDOWS_CONFIG['SIZE']) #Dimensiones de la ventana
    error_windows.title(ERROR_WINDOWS_CONFIG['TITLE']) #Título de la ventana
    error_windows.resizable(False,False) #Se permite o no cambiar el título de la ventana
    error_windows.config(background = MAIN_WINDOWS_CONFIG['BG_COLOR']) #Color de fondo de la ventana
    
    error_label = Label(error_windows,text=error_text,background=MAIN_WINDOWS_CONFIG['BG_COLOR'])
    error_label.place(x=FORM_CONFIG['X_ERROR_LABEL'],y=FORM_CONFIG['Y_ERROR_LABEL'])

    error_windows.mainloop()

# Función que crea el fichero temporal donde se almacenan los datos de entrada del formulario

def create_data_file():
    
    # Apertura para escritura del fichero temporal
    try:
        temp_file = open(APP_CONFIG['TEMP_INPUT_DATA_FILE'],'w',encoding=APP_CONFIG['CHARSET'])
    except:
         open_error_windows(FILE_ERROR['NO_OPEN_FILE'])

    # Escritura en el fichero temporal del tipo de exportación elegido
    if APP_CONFIG['EXPORT_TYPE'] == 'Ninguno':
        text_to_file = 'none'
    else:
        text_to_file = APP_CONFIG['EXPORT_TYPE'].lower()

    temp_file.write(str(text_to_file+'\n'))

    # Escritura en el fichero temporal de los datos introducidos de las redes sociales seleccionadas
    for social_network in SOCIAL_CONFIG:
       
        if social_network['SCRAPING'] == 'True':

            for key_data,input_data in social_network.items():
            
                if key_data in ('ALIAS','TARGET','USER','PASS'):
                    
                    if input_data == '':
                        input_data = str(0) #Si no se ha usuario/contraseña, se añade un 0 

                    try:
                        temp_file.write(str(input_data)+APP_CONFIG['DATA_FILE_SEPARATOR'])
                    except:
                        open_error_windows(FORM_ERROR['NO_WRITE_FILE']) 
            
            temp_file.write('\n')
    
    

    # Cierre del fichero temporal
    try:
        temp_file.close()
    except:
        open_error_windows(FORM_ERROR['NO_CLOSE_FILE'])
    

# Función que recoge los datos enviados por el formulario

def send_data_form():
    
    social_network_checked = False

    # Comprobar que no hay errores en los campos del formulario

    # Comprobar si hay marcada alguna red social para hacer scraping
    for social_network in SOCIAL_CONFIG:
        if globals()[social_network['ALIAS']+'_option'].get() == True:
            social_network_checked = True
            break
    
    # Si no se ha marcado ninguna red social, se indica
    if social_network_checked == False:   
        open_error_windows(FORM_ERROR['NO_SOCIAL_NETWORK_SELECTED'])

    # Errores en los datos introducidos
    for social_network in SOCIAL_CONFIG:

        if globals()[social_network['ALIAS']+'_target'].get() == '' and globals()[social_network['ALIAS']+'_option'].get() == True:
            open_error_windows(FORM_ERROR['NO_TARGET']+' para '+social_network['NAME']) #Error: Perfil objetivo no insertado

        # Almacenamos los datos de la red social en la lista
        if globals()[social_network['ALIAS']+'_option'].get() == True:
            social_network['SCRAPING'] = 'True'
            social_network['TARGET'] = globals()[social_network['ALIAS']+'_target'].get()
            social_network['USER'] = globals()[social_network['ALIAS']+'_user'].get()
            social_network['PASS'] = globals()[social_network['ALIAS']+'_pass'].get() 
        else:
            social_network['SCRAPING'] = 'False'
            social_network['TARGET'] = ''
            social_network['USER'] = ''
            social_network['PASS'] = ''

    # Se establece el formato de exportación seleccionado
    APP_CONFIG['EXPORT_TYPE'] = globals()[export_option].get()
    
    # Se almacenan los datos introducidos en un fichero de texto temporal
    create_data_file()

    # Finalización de la ejecución y retorno al programa principal
    exit()
        
# Función que limpia los datos introducidos en el formulario

def form_data_reset():
    
    for social_network in SOCIAL_CONFIG:
        globals()[social_network['ALIAS']+'_target'].set('')
        globals()[social_network['ALIAS']+'_user'].set('')
        globals()[social_network['ALIAS']+'_pass'].set('')
        globals()[social_network['ALIAS']+'_option'].set(False)
    
    globals()[export_option].set('Ninguno')


# Programa principal

# Creación de la ventana y configuración de las propiedades de la ventana
form_windows = Tk()
set_form_windows(form_windows)

# Título del formulario
form_title = Label(form_windows,text=FORM_CONFIG['TEXT_TITLE'],bg=FORM_CONFIG['BG_TITLE'],fg=FORM_CONFIG['COLOR_TITLE'],width=FORM_CONFIG['WIDTH_TITLE'],font=(FORM_CONFIG['FONT_TITLE'],FORM_CONFIG['SIZE_TITLE']))
form_title.pack()

# Elementos del formulario: Etiquetas de cabecera superiores
target_label = Label(form_windows,text=FORM_CONFIG['TARGET_LABEL_TEXT'],bg=FORM_CONFIG['BG_COLOR'])
target_label.place(x=FORM_CONFIG['X_TARGET'], y=FORM_CONFIG['Y_HEADERS'])
user_label = Label(form_windows,text=FORM_CONFIG['USER_LABEL_TEXT'],bg=FORM_CONFIG['BG_COLOR'])
user_label.place(x=FORM_CONFIG['X_USER'], y=FORM_CONFIG['Y_HEADERS'])
pass_label = Label(form_windows,text=FORM_CONFIG['PASSWORD_LABEL_TEXT'],bg=FORM_CONFIG['BG_COLOR'])
pass_label.place(x=FORM_CONFIG['X_PASSWORD'], y=FORM_CONFIG['Y_HEADERS'])


# Elementos del formulario: datos de las redes sociales introducidos por el usuario

for social_network in SOCIAL_CONFIG:
    
    # Inicialización de variables
    globals()[social_network['ALIAS']+'_option'] = BooleanVar()
    globals()[social_network['ALIAS']+'_target'] = StringVar()
    globals()[social_network['ALIAS']+'_user'] = StringVar()
    globals()[social_network['ALIAS']+'_pass'] = StringVar()
    globals()[social_network['ALIAS']+'_target_check_button'] = StringVar()

    # Elementos del formulario
    globals()[social_network['ALIAS']+'_logo'] = PhotoImage(file=APP_CONFIG['PATH_IMAGE']+social_network['ALIAS']+'_img.gif')
    social_image = Label(form_windows, image=globals()[social_network['ALIAS']+'_logo'], width=FORM_CONFIG['WIDTH_IMAGE'], height=FORM_CONFIG['HEIGHT_IMAGE'],bg=FORM_CONFIG['BG_COLOR'])
    social_image.place(x=FORM_CONFIG['X_IMAGE'],y=FORM_CONFIG['Y_SOCIAL_NETWORK_LOGO'])

    # Elementos del formulario: Seleccionar red social
    social_check = Checkbutton(form_windows, bg=FORM_CONFIG['BG_COLOR'], variable=globals()[social_network['ALIAS']+'_option'], onvalue=1, offvalue=0)
    social_check.place(x=FORM_CONFIG['X_CHECK'], y=FORM_CONFIG['Y_SOCIAL_NETWORK_LOGO'])

    # Elementos del formulario: Insertar perfil/cuenta del objetivo
    social_target_input = Entry(form_windows,textvariable=globals()[social_network['ALIAS']+'_target'])
    social_target_input.place(x=FORM_CONFIG['X_TARGET'], y=FORM_CONFIG['Y_SOCIAL_NETWORK'],width=FORM_CONFIG['WIDTH_INPUT'],height=FORM_CONFIG['HEIGHT_INPUT'])

    # Elementos del formulario: Insertar usuario para hacer login en la red social
    user_input = Entry(form_windows,textvariable=globals()[social_network['ALIAS']+'_user'])
    user_input.place(x=FORM_CONFIG['X_USER'], y=FORM_CONFIG['Y_SOCIAL_NETWORK'],width=FORM_CONFIG['WIDTH_INPUT'],height=FORM_CONFIG['HEIGHT_INPUT'])

    # Elementos del formulario: Insertar contraseña del usuario indicado
    pass_input = Entry(form_windows,textvariable=globals()[social_network['ALIAS']+'_pass'], show='*')
    pass_input.place(x=FORM_CONFIG['X_PASSWORD'], y=FORM_CONFIG['Y_SOCIAL_NETWORK'],width=FORM_CONFIG['WIDTH_INPUT'],height=FORM_CONFIG['HEIGHT_INPUT'])

    # Configuración de la coordenada Y de los siguientes elementos del formulario (siguiente red social)
    FORM_CONFIG['Y_SOCIAL_NETWORK'] += FORM_CONFIG['Y_OFFSET']
    FORM_CONFIG['Y_SOCIAL_NETWORK_LOGO'] = FORM_CONFIG['Y_SOCIAL_NETWORK'] - FORM_CONFIG['Y_OFFSET_LOGO']

# Elementos del formulario: lista desplegable tipos de exportación 

export_option = ''
globals()[export_option] = StringVar()

export_label = Label(form_windows,text='Formato de exportación',bg=FORM_CONFIG['BG_COLOR'])
export_label.place(x=FORM_CONFIG['X_EXPORT_LABEL'], y=FORM_CONFIG['Y_EXPORT_LABEL']) 
export_type_menu = ttk.Combobox(form_windows,textvariable=globals()[export_option],state="readonly",width=10)

export_type = list()

for te in EXPORT_FORMAT.values():
    export_type.append(te)
    export_type_menu["values"] = export_type

export_type_menu.set(EXPORT_FORMAT['none'])
export_type_menu.place(x=FORM_CONFIG['X_EXPORT_MENU'], y=FORM_CONFIG['Y_EXPORT_MENU'])


# Elementos del formulario: botones reset y enviar
scraping_submit = Button(form_windows, text=FORM_CONFIG['TEXT_SUBMIT'], command=send_data_form, width=FORM_CONFIG['WIDTH_BUTTON'], height=FORM_CONFIG['HEIGHT_BUTTON'], bg=FORM_CONFIG['BGCOLOR_BUTTON'])
scraping_submit.place(x=FORM_CONFIG['X_SUBMIT'], y=FORM_CONFIG['Y_BUTTON'])

scraping_reset = Button(form_windows, text=FORM_CONFIG['TEXT_RESET'], command=form_data_reset, width=FORM_CONFIG['WIDTH_BUTTON'], height=FORM_CONFIG['HEIGHT_BUTTON'], bg=FORM_CONFIG['BGCOLOR_BUTTON'])
scraping_reset.place(x=FORM_CONFIG['X_RESET'], y=FORM_CONFIG['Y_BUTTON'])

form_windows.mainloop()