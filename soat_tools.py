import http.client
import mimetypes
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

session='0000B4L6lGNYI8DUQUefeQ0Ul9W:1b0vr56u2'
fduid='d4caa0bce7fbd0c8c34dd5f3707d55bc11587338533'


def getFinalPrice(placa):
	respuesta=getPrice(placa)
	if "expirado," in respuesta['mensaje'].split():
		setcookies()
		#print("antes de setear cookies")
		#tt.setcookies()
		respuesta=getPrice(placa)
	#print(respuesta)
	#if respuesta['success']==True:		
	while((respuesta['success']==True) and (respuesta['precio']=='00')):
		respuesta=getPrice(placa)
	return respuesta	



def getPrice(placa):
	#if needCookies:
	#	setcookies()
	#print (session)
	#print (fduid)
	message=""
	conn = http.client.HTTPSConnection("www.lapositiva.com.pe")
	payload = 'home=1&iplaca='+placa+'&socio='
	headers = {
		'Accept': 'application/json, text/javascript, /; q=0.01',
	  #'x-dtpc': '1$170024642_964h13vUNPRMOSRMNOHAGJRJACAEPKIFOKRBANM-0',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': '__cfduid='+fduid+'; JSESSIONID='+session+'; _hjIncludedInSample=1; dtCookie=v_4_srv_1_sn_A6164DBE6F6C91E1A138AF45B7E3CC4B_perc_100000_ol_0_mul_1'
	}
	conn.request("POST", "/wps/portal/corporativo/home/cotizador/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zijSyNLAxNDAx9_S3NDAwCDUwD_T09DI1NPMz1w8EKDHAARwP9KGL041EQhd_4cP0oVCvcjVwsDBzDAnyCTYNcDQIszaAK8JhRkBsaYZDpqAgAyxwNmg!!/p0/IZ7_29281401MO9600Q05QOIH134P6=CZ6_29281401MO9600Q05QOIH134H7=NJ43=/", payload, headers)
	res = conn.getresponse()
	data = res.read()
	res= json.loads(data.decode("utf-8"))
	success = res['success']
	if success:
		dniasociado = res['dniasociado']
		if dniasociado:
			#message = 'El precio para la placa '+placa+' es: '+res['soat']['precio']['valor']+' soles'
			message={'success': True, 'precio':res['soat']['precio']['valor'],'placa':placa,
					'mensaje':'El precio para la placa '+placa+' es: '+res['soat']['precio']['valor']+' soles'}
		else:
			message = getPriceNuevo(placa)
	else :
		#message='Se registró el ERROR: '+res['message']
		message={'success': False,'mensaje':'Se registró el ERROR: '+res['message']}
		#print(res)
	return message

def getPriceNuevo(placa):
	message=""
	conn = http.client.HTTPSConnection("www.lapositiva.com.pe")
	payload = 'hanio=2016&hchasis=asasdasdasa&hclase=Moto&hidclase=10&hidmarca=6091&hidmodelo=1001142&hiduso=1&hidversion=10001913&hidzona=15&hmarca=BAJAJ&hmodelo=PULSAR&hmotor=&hplaca='+placa+'&hplazo=&huso=Particular&hversion=SIN%20VERSI%D3N&hzona=LIMA'
	headers = {
		'Accept': 'application/json, text/javascript, /; q=0.01',
	  #'x-dtpc': '1$170024642_964h13vUNPRMOSRMNOHAGJRJACAEPKIFOKRBANM-0',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': '__cfduid='+fduid+'; JSESSIONID='+session+'; _hjIncludedInSample=1; dtCookie=v_4_srv_1_sn_A6164DBE6F6C91E1A138AF45B7E3CC4B_perc_100000_ol_0_mul_1'
	}
	conn.request("POST", "/wps/portal/corporativo/home/cotizador/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zijSyNLAxNDAx9_S3NDAwCDUwD_T09DI1NPMz1w8EKDHAARwP9KGL041EQhd_4cP0oVCvcjVwsDBzDAnyCTYNcDQIszaAK8JhRkBsaYZDpqAgAyxwNmg!!/p0/IZ7_29281401MO9600Q05QOIH134P6=CZ6_29281401MO9600Q05QOIH134H7=NJ40=/", payload, headers)
	res = conn.getresponse()
	data = res.read()
	res= json.loads(data.decode("utf-8"))
	success = res['success']
	if success:
		message={'success': True, 'precio':res['data']['precio']['valor'],'placa':placa,
				 'mensaje':'El precio para la placa '+placa+' es: '+res['data']['precio']['valor']+' soles'}
		#message = 'El precio para la placa '+placa+' es: '+res['data']['precio']['valor']+' soles'
	else :
		message={'success': False,'mensaje':'Se registró el ERROR: '+res['message']}
		#message='Se registró el ERROR: '+res['message']
		#print(res)
	return message    

def setcookies():
	global session
	global fduid
	chrome_path= r"C:\Users\7000012977\Documents\chromedriver.exe"
	#chrome_path= r"C:\chromedriver.exe"
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	driver= webdriver.Chrome(chrome_path,options=options)
	driver.implicitly_wait(20) # seconds
	driver.get("https://www.lapositiva.com.pe/wps/portal/corporativo/home/cotizador")
	#cookies=driver.get_cookies()
	#print(driver.get_cookies())
	driver.find_element_by_xpath("""//*[@id="layoutContainers"]/div/div[2]/div/div/div[4]/div/div/section/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div""").click()
	placaForm=driver.find_element_by_id("iplaca-home")
	placaForm.send_keys("4952-0W")
	#driver.find_element_by_id("btngo").click()    
	driver.execute_script("arguments[0].click();", driver.find_element_by_id("btngo"))
	cookies=driver.get_cookies()
	#session=cookies[10]['value']
	#fduid=cookies[12]['value']
	for cookie in cookies:
		if cookie['name']=="JSESSIONID":
			#print('seteo session : '+cookie['value'])
			session=cookie['value']
		elif cookie['name']=="__cfduid":
			#print('seteo fduid : '+ cookie['value'])
			fduid=cookie['value']
	driver.quit()