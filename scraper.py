#!/usr/bin/python

import sys, getopt
import csv
import time
import urllib.request
import os

from variables import *

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains

cislaKategorii = ["7", "13", "16", "107", "108", "109", "110", "112", "132", "134", "24", "39", "118", "119", "120", "121", "122", "123", "42", "114", "114", "115", "116", "117", "43", "100", "101", "102", "103", "104", "105", "106", "51", "37", "57", "64", "68", "72", "73", "140", "141", "142", "144", "145", "146", "60", "61", "66", "33", "34", "56", "63", "65", "67", "69", "70", "71", "74", "75", "76", "79", "80", "81", "133", "147", "148", "149", "150", "151", "6", "8", "9", "10", "12", "48", "52", "58", "152", "15", "53"]

def main(argv):
	produktyFilePath = ''
	produktyImagesFilePath = ''
	
	try:
		opts, args = getopt.getopt(argv,"hp:s:",["pfile=","sfile="])
	except getopt.GetoptError:
		print ('test.py -p <produktyFilePath.csv> -s <produktyImagesFilePath.csv>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print ('test.py -p <produktyFilePath.csv> -s <produktyImagesFilePath.csv>')
			sys.exit()
		elif opt in ("-p", "--pfile"):
			produktyFilePath = arg
		elif opt in ("-s", "--sfile"):
			produktyImagesFilePath = arg
		else:
			sys.exit(2)
	
	produktyFilePath = os.path.dirname(os.path.abspath(__file__)) + '/' + produktyFilePath
	produktyImagesFilePath = os.path.dirname(os.path.abspath(__file__)) + '/' + produktyImagesFilePath
	ScrapeniProdukty(produktyFilePath, produktyImagesFilePath)

def ScrapeniProdukty(produktyFilePath, produktyImagesFilePath):
	produktyFile = open(produktyFilePath, 'w', newline='', encoding='utf-8')
	produktyImagesFile = open(produktyImagesFilePath, 'w', newline='', encoding='utf-8')
	writer = csv.writer(produktyFile)
	writerImages = csv.writer(produktyImagesFile)
	### CHROMEDRIVER JE NANIC, NEFUNGUJE NA 100%, NEPOUZIVAT!!!
	driver = webdriver.PhantomJS(executable_path='/home/ipsec/bizuteria-eshop_scraper/phantomjs/phantomjs', service_args=['--ignore-ssl-errors=true'])
	#driver = webdriver.Chrome(executable_path=r"C:\WORK\bizuteria-eshop_scraper\chromedriver\chromedriver.exe")
	#driver = webdriver.Firefox(executable_path=r"/usr/bin/firefox")
	mouse = webdriver.ActionChains(driver)
	
	global store
	global websites
	global attribute_set
	global type
	global category_ids
	global sku
	global has_options
	global name
	global url_key
	global country_of_manufacture
	global msrp_enabled
	global msrp_display_actual_price_type
	global meta_title
	global meta_description
	global image
	global small_image
	global thumbnail
	global velkost_celenky
	global material_celenky
	global velkost_manzetoveho_gombika
	global sirka_naramku
	global velkost_brosne
	global zapinanie_brosne
	global rozmer_sperkovnice
	global velkost_privesku
	global rozmery_skatulky
	global velkost_koralikov
	global velkost_periel
	global custom_design
	global page_layout
	global options_container
	global gift_message_available
	global image_label
	global small_image_label
	global thumbnail_label
	global url_path
	global weight
	global price
	global special_price
	global msrp
	global description
	global short_description
	global meta_keyword
	global videobox
	global custom_layout_update
	global customtab
	global customtabtitle
	global shortparams
	global status
	global visibility
	global ebizmarts_mark_visited
	global tax_class_id
	global color
	global dlzka_nausnice
	global dlzka_naramku
	global dlzka_retiazky_k_privesku
	global poznamka
	global dlzka_nahrdelnika
	global zapinanie_retiazky
	global udalost
	global polodrahokam
	global material
	global typ_periel
	global idealne_ako
	global material_kovovych_casti
	global velkost_prstena
	global zavesenie_nausnice
	global material_krystalov
	global zapinanie_nahrdelnika
	global manufacturer
	global zapinanie_naramku
	global is_recurring
	global news_from_date
	global news_to_date
	global special_from_date
	global special_to_date
	global custom_design_from
	global custom_design_to
	global qty
	global min_qty
	global use_config_min_qty
	global is_qty_decimal
	global backorders
	global use_config_backorders
	global min_sale_qty
	global use_config_min_sale_qty
	global max_sale_qty
	global use_config_max_sale_qty
	global is_in_stock
	global low_stock_date
	global notify_stock_qty
	global use_config_notify_stock_qty
	global manage_stock
	global use_config_manage_stock
	global stock_status_changed_auto
	global use_config_qty_increments
	global qty_increments
	global use_config_enable_qty_inc
	global enable_qty_increments
	global is_decimal_divided
	global stock_status_changed_automatically
	global use_config_enable_qty_increments
	global product_name
	global store_id
	global product_type_id
	global product_status_changed
	global product_changed_websites
	global website
	global _media_image
	global _media_lable
	global _media_position
	global _media_is_disabled
	
	writer.writerow(['store', 'websites', 'attribute_set', 'type', 'category_ids', 'sku', 'has_options', 'name', 'url_key' , 'country_of_manufacture', 'msrp_enabled', 'msrp_display_actual_price_type', 'meta_title', 'meta_description', 'image', 'small_image', 'thumbnail', 'velkost_celenky','material_celenky','velkost_manzetoveho_gombika','sirka_naramku','velkost_brosne','zapinanie_brosne','rozmer_sperkovnice','velkost_privesku','rozmery_skatulky','velkost_koralikov','velkost_periel','custom_design','page_layout','options_container','gift_message_available','url_path','weight','price','special_price','msrp','short_description','description','meta_keyword','videobox','custom_layout_update','customtab','customtabtitle','shortparams','status','visibility','ebizmarts_mark_visited','tax_class_id','color','dlzka_nausnice','dlzka_naramku','dlzka_retiazky_k_privesku','poznamka','dlzka_nahrdelnika','zapinanie_retiazky','udalost','polodrahokam','material','typ_periel','idealne_ako','material_kovovych_casti','velkost_prstena','zavesenie_nausnice','material_krystalov','zapinanie_nahrdelnika','manufacturer','zapinanie_naramku','is_recurring','news_from_date','news_to_date','special_from_date','special_to_date','custom_design_from','custom_design_to','qty','min_qty','use_config_min_qty','is_qty_decimal','backorders','use_config_backorders','min_sale_qty','use_config_min_sale_qty','max_sale_qty','use_config_max_sale_qty','is_in_stock','low_stock_date','notify_stock_qty','use_config_notify_stock_qty','manage_stock','use_config_manage_stock','stock_status_changed_auto','use_config_qty_increments','qty_increments','use_config_enable_qty_inc','enable_qty_increments','is_decimal_divided','stock_status_changed_automatically','use_config_enable_qty_increments','product_name','store_id','product_type_id','product_status_changed','product_changed_websites'])
	writerImages.writerow(['sku', 'image', 'small_image', 'thumbnail'])

	driver.set_window_size(1024, 768)
	
	# lognem sa
	driver.get('http://www.bizuteria-eshop.sk/site/login')
	driver.find_element_by_id('LoginForm_username').send_keys("xxx")
	driver.find_element_by_id('LoginForm_password').send_keys("xxx")
	driver.find_element_by_name('yt0').click()
		
	# dostavame sa na zoznam produktov a potom na jednotlive produktove stranky
	driver.find_element_by_link_text('Produkty').click()
	driver.find_element_by_xpath("//a[@href='/products']").click()
	
	productPageCounter = 1
	x = 1
	
	# velky for cyklus, ktory skace medzi jednotlivymi produktami
	while x < 101:
		poleKategoriiOld = []
		i = 1
	
		tableXPath = '//table/tbody/tr[' + str(x) + ']/td[2]/a'
		driver.find_element_by_xpath(tableXPath).click()
		
		# scrapujeme vsetko info
		store = "admin"
		websites = "base"
		attribute_set = "Default"
		type = "simple" 
		
		
		poleKategoriiOld.append((Select(driver.find_element_by_class_name('pr_category_id'))).first_selected_option.text)
		
		element = driver.find_element_by_id('select-category')
		driver.execute_script("arguments[0].click()", element)
		#for i in range(1,9):
		#	driver.find_element_by_css_selector("div[class*='hitarea expandable-hitarea']").click()

		for j in range(len(cislaKategorii)):
			katName = "ProductsCategories[category_id][" + cislaKategorii[j] + "]"
			kat = driver.find_element_by_name(katName)
			if (driver.find_element_by_name(katName).is_selected()):
				poleKategoriiOld.append(kat.get_attribute("value"))
		
		category_ids = ZistiKategorie(poleKategoriiOld); 
		
		sku = driver.find_element_by_name('Products[sku]').get_attribute("value")
		
		# mam SKU, idem zhanat obrazky k nemu
		ScrapeniImages(produktyImagesFilePath, driver, sku, writerImages)
		
		has_options = "0"
		name = driver.find_element_by_name('Products[name]').get_attribute("value")
		url_key = driver.find_element_by_name('Products[url]').get_attribute("value")
		country_of_manufacture = ""
		msrp_enabled = "Use config"
		msrp_display_actual_price_type = "Use config"
		meta_title = ""
		meta_description = ""
		image = ""
		small_image = ""
		thumbnail = ""
		custom_design = ""
		page_layout = "No layout updates"
		options_container = "Product Info Column"
		gift_message_available = "No"
		url_path = driver.find_element_by_name('Products[url]').get_attribute("value")
		weight = driver.find_element_by_name('Products[weight]').get_attribute("value")
		price = str(float(driver.find_element_by_name('Products[price]').get_attribute("value")) * 1.2)	### DORIESIT CENU S DANOU LEBO JE NA NOM ZAVESENY SKRIPT JE TO DOBRE???		
		special_price = ""
		msrp = ""
		description = ""
		short_description = driver.find_element_by_css_selector("div[class*='redactor_translatable-redactor redactor_editor']").text
		meta_keyword = ""
		videobox = ""
		custom_layout_update = ""
		customtab = ""
		customtabtitle = ""
		shortparams = "" 
		if(((Select(driver.find_element_by_id('Products_published'))).first_selected_option.text) == "Áno"):
			status = "Enabled"
		else:
			status = "Disabled"
		visibility = "Catalog, Search"
		ebizmarts_mark_visited = "No"
		tax_class_id = "None"
			
		### TREBA SA PREKLIKNUT NA TAB PARAMETRE
		driver.execute_script("window.scrollTo(0, 0)")
		driver.find_element_by_css_selector("a[href*='#parameters']").click()
		
		try:
			velkost_celenky = driver.find_element_by_name('ProductsParameters[parameter_id][38][value]38').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			material_celenky = driver.find_element_by_name('ProductsParameters[parameter_id][37][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_manzetoveho_gombika = driver.find_element_by_name('ProductsParameters[parameter_id][30][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			sirka_naramku = driver.find_element_by_name('ProductsParameters[parameter_id][22][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_brosne = driver.find_element_by_name('ProductsParameters[parameter_id][27][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			zapinanie_brosne = driver.find_element_by_name('ProductsParameters[parameter_id][26][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			rozmer_sperkovnice = driver.find_element_by_name('ProductsParameters[parameter_id][24][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_privesku = driver.find_element_by_name('ProductsParameters[parameter_id][15][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			rozmery_skatulky = driver.find_element_by_name('ProductsParameters[parameter_id][18][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_koralikov = driver.find_element_by_name('ProductsParameters[parameter_id][10][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_periel = driver.find_element_by_name('ProductsParameters[parameter_id][6][value]').get_attribute("value")
		except NoSuchElementException:
			pass
			
			
		try:
			color = driver.find_element_by_name('ProductsParameters[parameter_id][33][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			dlzka_nausnice = driver.find_element_by_name('ProductsParameters[parameter_id][8][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			dlzka_naramku = driver.find_element_by_name('ProductsParameters[parameter_id][13][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			dlzka_retiazky_k_privesku = driver.find_element_by_name('ProductsParameters[parameter_id][35][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			poznamka = driver.find_element_by_name('ProductsParameters[parameter_id][12][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			dlzka_nahrdelnika = driver.find_element_by_name('ProductsParameters[parameter_id][7][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			zapinanie_retiazky = driver.find_element_by_name('ProductsParameters[parameter_id][36][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			udalost = driver.find_element_by_name('ProductsParameters[parameter_id][32][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			polodrahokam = driver.find_element_by_name('ProductsParameters[parameter_id][31][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			material = driver.find_element_by_name('ProductsParameters[parameter_id][11][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			typ_periel = driver.find_element_by_name('ProductsParameters[parameter_id][23][value]').get_attribute("value")
			if "see" in typ_periel:
				typ_periel = "sea shell"
		except NoSuchElementException:
			pass
		try:
			idealne_ako = driver.find_element_by_name('ProductsParameters[parameter_id][19][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			material_kovovych_casti = driver.find_element_by_name('ProductsParameters[parameter_id][20][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			velkost_prstena = driver.find_element_by_name('ProductsParameters[parameter_id][17][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			zavesenie_nausnice = driver.find_element_by_name('ProductsParameters[parameter_id][9][value]').get_attribute("value")
			print (zavesenie_nausnice)
		except NoSuchElementException:
			pass
		try:
			material_krystalov = driver.find_element_by_name('ProductsParameters[parameter_id][21][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			zapinanie_nahrdelnika = driver.find_element_by_name('ProductsParameters[parameter_id][14][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			manufacturer = driver.find_element_by_name('ProductsParameters[parameter_id][34][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		try:
			zapinanie_naramku = driver.find_element_by_name('ProductsParameters[parameter_id][16][value]').get_attribute("value")
		except NoSuchElementException:
			pass
		
		is_recurring = "No"
		news_from_date = ""
		news_to_date = ""
		special_from_date = ""
		special_to_date = ""
		custom_design_from = ""
		custom_design_to = ""
		
		### TREBA SA PREKLIKNUT NA NOVY TAB SKLADOVA KARTA
		driver.find_element_by_css_selector("a[href*='#stock-card']").click()
		
		qty = driver.find_element_by_name('st_count').get_attribute("value")
		min_qty = "0"
		use_config_min_qty = "1"
		is_qty_decimal = "0"
		backorders = "0"
		use_config_backorders = "1"
		min_sale_qty = "1"
		use_config_min_sale_qty = "1"
		max_sale_qty = "0"
		use_config_max_sale_qty = "1"
		if (int(qty) > 0):
			is_in_stock = "1"
		else:
			is_in_stock = "0"
		low_stock_date = "" ###TREBA MOZNO DOROBIT DATUM
		notify_stock_qty = ""
		use_config_notify_stock_qty = "1"
		manage_stock = "0"
		use_config_manage_stock = "1"
		stock_status_changed_auto = "1"
		use_config_qty_increments = "1"
		qty_increments = "0"
		use_config_enable_qty_inc = "1"
		enable_qty_increments = "0"
		is_decimal_divided = "0"
		stock_status_changed_automatically = "1"
		use_config_enable_qty_increments = "1"
		product_name = driver.find_element_by_name('Products[name]').get_attribute("value")
		store_id = "0"
		product_type_id = "simple"
		product_status_changed = ""
		product_changed_websites = ""
		
		driver.find_element_by_link_text('Produkty').click()
		driver.find_element_by_xpath("//a[@href='/products']").click()
		
		writer.writerow([store, websites, attribute_set, type, category_ids, sku, has_options, name, url_key , country_of_manufacture, msrp_enabled, msrp_display_actual_price_type, meta_title, meta_description, image, small_image, thumbnail, velkost_celenky,material_celenky,velkost_manzetoveho_gombika,sirka_naramku,velkost_brosne,zapinanie_brosne,rozmer_sperkovnice,velkost_privesku,rozmery_skatulky,velkost_koralikov,velkost_periel,custom_design,page_layout,options_container,gift_message_available,url_path,weight,price,special_price,msrp,short_description,description,meta_keyword,videobox,custom_layout_update,customtab,customtabtitle,shortparams,status,visibility,ebizmarts_mark_visited,tax_class_id,color,dlzka_nausnice,dlzka_naramku,dlzka_retiazky_k_privesku,poznamka,dlzka_nahrdelnika,zapinanie_retiazky,udalost,polodrahokam,material,typ_periel,idealne_ako,material_kovovych_casti,velkost_prstena,zavesenie_nausnice,material_krystalov,zapinanie_nahrdelnika,manufacturer,zapinanie_naramku,is_recurring,news_from_date,news_to_date,special_from_date,special_to_date,custom_design_from,custom_design_to,qty,min_qty,use_config_min_qty,is_qty_decimal,backorders,use_config_backorders,min_sale_qty,use_config_min_sale_qty,max_sale_qty,use_config_max_sale_qty,is_in_stock,low_stock_date,notify_stock_qty,use_config_notify_stock_qty,manage_stock,use_config_manage_stock,stock_status_changed_auto,use_config_qty_increments,qty_increments,use_config_enable_qty_inc,enable_qty_increments,is_decimal_divided,stock_status_changed_automatically,use_config_enable_qty_increments,product_name,store_id,product_type_id,product_status_changed,product_changed_websites])
		
		if(x == 100):
			if (productPageCounter <= 28) :
				driver.find_element_by_link_text('Ďalší').click()
				productPageCounter += 1
				x = 0;
			else:
				print("Dokoncil som scrapovat produkty. HOTOVO!")
				driver.quit()
		x += 1
	 
def ScrapeniImages(produktyImagesFilePath, driver, sku, writerImages):
	
	
	adresaWebu = "http://www.bizuteria-eshop.sk"
	imagesFolder = os.path.dirname(os.path.abspath(__file__)) + "/images/"
	imageID = 1
	
	items = driver.find_elements_by_xpath("//ul[@class='product-images ui-sortable']//li[not(@class)]")
	for item in items:	
		try:
			name = '/' + sku + '_' +str(imageID) + ".jpg"
			finalPath = imagesFolder + name
		
			imageNumber = item.get_attribute("id")
			imageXPath = "//ul[@class='product-images ui-sortable']//li[@id='" + imageNumber + "'" +"]/img" 
			imageSRC = driver.find_element_by_xpath(imageXPath).get_attribute("src")
			imageSRC = imageSRC.split("src=")[1]
			imageURL = adresaWebu + imageSRC
			urllib.request.urlretrieve(imageURL, finalPath)
			if(imageID == 1):
				writerImages.writerow([sku, name, name, name])
			else:
				writerImages.writerow([sku, name])		
			imageID += 1
		except NoSuchElementException:
			pass
	
	
	
def ZistiKategorie(poleKategoriiOld):
	convertedKategorie = ""
	jednaKategoria = ""
	
	poleKategoriiOld = list(set(poleKategoriiOld))
	
	for i in range(len(poleKategoriiOld)):
		jednaKategoria = poleKategoriiOld[i]
	
		if (jednaKategoria == 'Detská bižutéria'):
			jednaKategoria = str(9)
		elif (jednaKategoria == 'Pánska bižutéria'):
			jednaKategoria = str(10)
		elif (jednaKategoria == 'Swarovski šperky'):
			jednaKategoria = str(113)
		elif (jednaKategoria == 'Náušnice Swarovski'):
			jednaKategoria = str(114)
		elif (jednaKategoria == 'Prívesky Swarovski'):
			jednaKategoria = str(115)
		elif (jednaKategoria == 'Náramky Swarovski'):
			jednaKategoria = str(116)
		elif (jednaKategoria == 'Prstene Swarovski'):
			jednaKategoria = str(117)
		elif (jednaKategoria == 'Súpravy Swarovski'):
			jednaKategoria = str(118)
		elif (jednaKategoria == 'Brošne so Swarovski kryštáľmi'):
			jednaKategoria = str(119)
		elif (jednaKategoria == 'Manžetové gombíky Swarovski'):
			jednaKategoria = str(120)
		elif (jednaKategoria == 'Kompletná ponuka bižutérie a šperkov'):
			jednaKategoria = str(13)
		elif (jednaKategoria == 'Perlové šperky a šperky z prírodnej perlete'):
			jednaKategoria = str(15)
		elif (jednaKategoria == 'Perlové náušnice'):
			jednaKategoria = str(88)
		elif (jednaKategoria == 'Perlové náhrdelníky'):
			jednaKategoria = str(89)
		elif (jednaKategoria == 'Perlové náramky'):
			jednaKategoria = str(90)
		elif (jednaKategoria == 'Perlové prstene'):
			jednaKategoria = str(91)
		elif (jednaKategoria == 'Súpravy z perál a perlete'):
			jednaKategoria = str(92)
		elif (jednaKategoria == 'Perlové brošne'):
			jednaKategoria = str(93)
		elif (jednaKategoria == 'Štrasové šperky'):
			jednaKategoria = str(17)
		elif (jednaKategoria == 'Štrasové náramky'):
			jednaKategoria = str(83)
		elif (jednaKategoria == 'Štrasové náušnice'):
			jednaKategoria = str(84)
		elif (jednaKategoria == 'Štrasové náhrdelníky'):
			jednaKategoria = str(85)
		elif (jednaKategoria == 'Štrasové súpravy'):
			jednaKategoria = str(86)
		elif (jednaKategoria == 'Prstene so štrasovým očkom'):
			jednaKategoria = str(87)
		elif (jednaKategoria == 'Jablonecká bižutéria'):
			jednaKategoria = str(18)
		elif (jednaKategoria == 'Náramky Jablonecká bižutéria'):
			jednaKategoria = str(76)
		elif (jednaKategoria == 'Náušnice Jablonecká bižutéria'):
			jednaKategoria = str(77)
		elif (jednaKategoria == 'Náhrdelníky Jablonecká bižutéria'):
			jednaKategoria = str(78)
		elif (jednaKategoria == 'Súpravy Jablonecká bižutéria'):
			jednaKategoria = str(79)
		elif (jednaKategoria == 'Prstene Jablonecká bižutéria'):
			jednaKategoria = str(80)
		elif (jednaKategoria == 'Prívesky Jablonecká bižutéria'):
			jednaKategoria = str(81)
		elif (jednaKategoria == 'Vlasová bižutéria'):
			jednaKategoria = str(82)
		elif (jednaKategoria == 'Bižutéria'):
			jednaKategoria = str(20)
		elif (jednaKategoria == 'Náušnice s pierkom'):
			jednaKategoria = str(46)
		elif (jednaKategoria == 'Shamballa náušnice'):
			jednaKategoria = str(57)
		elif (jednaKategoria == 'Umelé perly, perličky'):
			jednaKategoria = str(60)
		elif (jednaKategoria == 'Shamballa náramky'):
			jednaKategoria = str(63)
		elif (jednaKategoria == 'Shamballa prívesky'):
			jednaKategoria = str(67)
		elif (jednaKategoria == 'Krištáľové súpravy'):
			jednaKategoria = str(68)
		elif (jednaKategoria == 'Náušnice bižutéria'):
			jednaKategoria = str(100)
		elif (jednaKategoria == 'Prstene bižutéria'):
			jednaKategoria = str(101)
		elif (jednaKategoria == 'Brošne bižutéria'):
			jednaKategoria = str(102)
		elif (jednaKategoria == 'Náhrdelníky bižutéria'):
			jednaKategoria = str(104)
		elif (jednaKategoria == 'Prívesky bižutéria'):
			jednaKategoria = str(105)
		elif (jednaKategoria == 'Náramky bižutéria'):
			jednaKategoria = str(106)
		elif (jednaKategoria == 'AKCIA -10%'):
			jednaKategoria = str(21)
		elif (jednaKategoria == 'AKCIA -25%'):
			jednaKategoria = str(22)
		elif (jednaKategoria == 'Ródiované šperky, pozlátené šperky a strieborné šperky'):
			jednaKategoria = str(23)
		elif (jednaKategoria == 'Pozlátené náušnice'):
			jednaKategoria = str(44)
		elif (jednaKategoria == 'Postriebrené šperky'):
			jednaKategoria = str(45)
		elif (jednaKategoria == 'Zirkónové náušnice s kubickým zirkónom'):
			jednaKategoria = str(56)
		elif (jednaKategoria == 'Ródiované náušnice'):
			jednaKategoria = str(59)
		elif (jednaKategoria == 'Strieborné šperky'):
			jednaKategoria = str(61)
		elif (jednaKategoria == 'Prstene z CZ krištáľu a akrylového krištáľu'):
			jednaKategoria = str(62)
		elif (jednaKategoria == 'Ródiované prstene'):
			jednaKategoria = str(64)
		elif (jednaKategoria == 'Ródiované prívesky'):
			jednaKategoria = str(65)
		elif (jednaKategoria == 'Ródiované súpravy'):
			jednaKategoria = str(66)
		elif (jednaKategoria == 'Pozlátené prívesky'):
			jednaKategoria = str(69)
		elif (jednaKategoria == 'Pozlátené náramky'):
			jednaKategoria = str(70)
		elif (jednaKategoria == 'Ródiované náramky'):
			jednaKategoria = str(71)
		elif (jednaKategoria == 'Pozlátené prstene'):
			jednaKategoria = str(72)
		elif (jednaKategoria == 'Ródiovaná retiazka'):
			jednaKategoria = str(73)
		elif (jednaKategoria == 'Pozlátené súpravy'):
			jednaKategoria = str(74)
		elif (jednaKategoria == 'Pozlátené brošne'):
			jednaKategoria = str(94)
		elif (jednaKategoria == 'AKCIA -50%'):
			jednaKategoria = str(24)
		elif (jednaKategoria == 'Akcia'):
			jednaKategoria = str(25)
		elif (jednaKategoria == 'Novinky'):
			jednaKategoria = str(26)
		elif (jednaKategoria == 'Výpredaj'):
			jednaKategoria = str(27)
		elif (jednaKategoria == 'Dámska bižutéria'):
			jednaKategoria = str(28)
		elif (jednaKategoria == 'Náramky'):
			jednaKategoria = str(30)
		elif (jednaKategoria == 'Prstene'):
			jednaKategoria = str(31)
		elif (jednaKategoria == 'Náhrdelníky'):
			jednaKategoria = str(32)	
		elif (jednaKategoria == 'Náušnice'):
			jednaKategoria = str(33)
		elif (jednaKategoria == 'Súpravy'):
			jednaKategoria = str(34)	
		elif (jednaKategoria == 'Šperkovnice'):
			jednaKategoria = str(52)
		elif (jednaKategoria == 'Prívesky'):
			jednaKategoria = str(53)		
		elif (jednaKategoria == 'Brošne'):
			jednaKategoria = str(58)	
		elif (jednaKategoria == 'Iné'):
			jednaKategoria = str(29)	
		elif (jednaKategoria == 'Manžetové gombíky'):
			jednaKategoria = str(35)
		elif (jednaKategoria == 'Škatuľky na šperky'):
			jednaKategoria = str(54)
		
		if(i == 0):
			convertedKategorie = jednaKategoria
		else:
			convertedKategorie = convertedKategorie + "," + jednaKategoria
			
	return convertedKategorie
	
if __name__ == "__main__":
   main(sys.argv[1:])

