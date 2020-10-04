#Configuración de los XPATH de las redes sociales

XPATH_LOGIN_LINKEDIN = {

	'NAME' : '//section/div/div/div/ul/li[@class="inline t-24 t-black t-normal break-words"]',
	'JOB' : '//section/div/div/div/div/h2',
	'LOCATION' : '//ul[@class="pv-top-card--list pv-top-card--list-bullet mt1"]/li[1]',
	'CONTACTS' : '//ul[@class="pv-top-card--list pv-top-card--list-bullet mt1"]/li[2]',
	'FOLLOWERS' : '//h3[@class="pv-recent-activity-section__follower-count t-14 t-black--light t-normal ember-view"]',
	'PROFILE_IMAGE' : '//div[@class="pv-top-card--photo text-align-left"]/div/div/img'
}

XPATH_NOLOGIN_LINKEDIN = {

	'NAME' : '//h1',
	'JOB' : '//section/section/section/div/div/div/h2',
	'LOCATION' : '//section/section/section/div/div/div/h3',
	'PROFILE_IMAGE' : '//section/section/section/div/img'
}

XPATH_NOLOGIN_INSTAGRAM = {

	'NAME' : '//h1',
	'BIOGRAPHY' : '//div[@class="-vDIg"]/span',
	'WEBSITE' : '//div[@class="-vDIg"]/a',
	'PUBLICATIONS' : '//header/section/ul/li[1]/a/span',
	'FOLLOWERS' : '//header/section/ul/li[2]/a/span',
	'FOLLOWING' : '//header/section/ul/li[3]/a/span',
	'PROFILE_IMAGE' : '//header/div/div/span/img'
}

XPATH_LOGIN_INSTAGRAM = {

	'NAME' : '//h1',
	'BIOGRAPHY' : '//div[@class="-vDIg"]/span',
	'WEBSITE' : '//div[@class="-vDIg"]/a',
	'PUBLICATIONS' : '//header/section/ul/li/span/span',
	'FOLLOWERS' : '//header/section/ul/li[2]/a/span',
	'FOLLOWING' : '//header/section/ul/li[3]/a/span',
	'PROFILE_IMAGE' : '//header/div/div/span/img'
}

XPATH_MISC = {
	'POPUP_LOGIN_BUTTON_INSTAGRAM' : '/html/body/div[4]/div/div/div[3]/button[2]',
	'POPUP_LOGIN_BUTTON_INSTAGRAM_2' : '/html/body/div[1]/section/main/div/div/div/section/div/button',
}

XPATH_TRANSLATE = {

	'ACCOUNT' : 'Perfil/Cuenta',
	'NAME' : 'Nombre',
	'BIOGRAPHY' : 'Biografía',
	'WEBSITE' : 'Sitio Web',
	'PUBLICATIONS' : 'Publicaciones',
	'FOLLOWERS' : 'Seguidores',
	'FOLLOWING' : 'Siguiendo',
	'JOB' : 'Trabajo/Empleo',
	'LOCATION' : 'Localización',
	'CONTACTS' : 'Contactos',
	'PROFILE_IMAGE' : 'Imagen de perfil'
	}

