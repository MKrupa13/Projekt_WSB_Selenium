# import unittest
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
#
# driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
# # driver.get('https://www.mantoshop.pl/')
# driver.get('https://www.mantoshop.pl/pol_m_NA-CO-DZIEN-252.html')
# driver.maximize_window()
# # cookie = driver.find_element_by_id('ckdsclmrshtdwn_v2')
# # cookie.click()
# # otworz_kategorie = driver.find_element_by_xpath('//a[@title="NA CO DZIEŃ"]')
# # otworz_kategorie.click()
# # produkty_ilosc = driver.find_element_by_id('s_setting_1')
# # produkty_ilosc.click()
# # prod_90 = driver.find_element_by_xpath('//ul[@aria-labelledby="s_setting_1"]//a[@data-value="90"]')
# # prod_90.click()
# kliknij_sortuj = driver.find_element_by_id('s_setting_0')
# kliknij_sortuj.click()
# #sortuj_od = driver.find_element_by_xpath('//a[@data-index="3"]')
# sortuj_od = driver.find_element_by_xpath('//a[@data-index="1"]')
# sortuj_od.click()
#
# ceny = list()
# #ceny_produktow = driver.find_elements_by_xpath('//span[@class="price"][text()]')
# ceny_produktow = driver.find_elements_by_class_name("product-name")
# for produkt in ceny_produktow:
#     ceny.append(produkt.text)
# print(ceny)
# tasuj = ceny
# tasuj.sort(reverse=True)
# print(tasuj)
#
# if ceny == tasuj:
#     print('Sortowanie działa prawidłowo :)')
# else:
#     print('Sortowanie działa nieprawidłowo')
#
# najedz_na_element = driver.find_element_by_xpath('//a[@class="nav-link active"]')
# Hover = ActionChains(driver).move_to_element(najedz_na_element)
# Hover.perform()
# element = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][1]//ul[@class="navbar-subnav"]')
# if element.is_displayed():
#     print('Widac')
# else:
#     print('Nie widac')
#
# najedz_na_element_dwa = driver.find_element_by_xpath('//a[@title="ODZIEŻ TRENINGOWA"]')
# Hover = ActionChains(driver).move_to_element(najedz_na_element_dwa)
# Hover.perform()
# element_dwa = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][2]//ul[@class="navbar-subnav"]')
#
# if element_dwa.is_displayed():
#     print('Widac')
# else:
#     print('Nie widac')
#

import unittest
from time import sleep
from typing import List, Any
from xmlrpc.client import boolean

from Tools.scripts.which import msg
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# driver.get('https://www.mantoshop.pl/pol_m_NA-CO-DZIEN-252.html')


class MojTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.mantoshop.pl/pol_m_NA-CO-DZIEN-252.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_SortName(self):
        driver = self.driver
        cookie = driver.find_element_by_id('ckdsclmrshtdwn_v2')
        cookie.click()
        select_category = driver.find_element_by_xpath('//a[@title="NA CO DZIEŃ"]')
        select_category.click()
        change_quantity = driver.find_element_by_id('s_setting_1')
        change_quantity.click()
        quantity_60 = driver.find_element_by_xpath('//ul[@aria-labelledby="s_setting_1"]//a[@data-value="60"]')
        quantity_60.click()
        click_sort = driver.find_element_by_id('s_setting_0')
        click_sort.click()
        sort_by_name_descending = driver.find_element_by_xpath('//a[@data-index="1"]')
        sort_by_name_descending.click()
        products_name = list()
        product_name = driver.find_elements_by_class_name("product-name")
        for product in product_name:
            products_name.append(product.text)
        print(products_name)
        products_name_2 = products_name.copy()
        products_name_2.sort(reverse=True)
        print(products_name_2)
        self.assertListEqual(products_name, products_name_2)

    def test_Menu1(self):
        driver = self.driver
        najedz_na_element = driver.find_element_by_xpath('//a[@class="nav-link active"]')
        Hover = ActionChains(driver).move_to_element(najedz_na_element)
        Hover.perform()
        wyskakujace_menu1 = driver.find_element_by_xpath(
            '//div[@id="menu_navbar"]//li[@class="nav-item"][1]//ul[@class="navbar-subnav"]')
        # if wyskakujace_menu.is_displayed():
        #     print('jest widoczne')
        # else:
        #     print('nie')
        self.assertTrue(wyskakujace_menu1.is_displayed())
        # element = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][1]//ul[@class="navbar-subnav"]')

    def test_Menu2(self):
        driver = self.driver
        najedz_na_element_2 = driver.find_element_by_xpath('//a[@title="ODZIEŻ TRENINGOWA"]')
        Hover = ActionChains(driver).move_to_element(najedz_na_element_2)
        Hover.perform()
        wyskakujace_menu2 = driver.find_element_by_xpath(
            '//div[@id="menu_navbar"]//li[@class="nav-item"][2]//ul[@class="navbar-subnav"]')
        # if wyskakujace_menu.is_displayed():
        #     print('jest widoczne')
        # else:
        #     print('nie')
        self.assertTrue(wyskakujace_menu2.is_displayed())

    def test_Login(self):
        driver = self.driver
        sign_in = driver.find_element_by_xpath('//div/a[@title="Twoje konto "]')
        sign_in.click()
        login_name = driver.find_element_by_id('user_login')
        login_name.send_keys('wsbwroclaw@gmail.com')
        password = driver.find_element_by_id('user_pass')
        password.send_keys('wyzszaszkolabankowa')
        sign_in_button = driver.find_element_by_xpath('//div[@class="signin_buttons col-md-10 col-xs-12"]/button[@class="btn signin_button"]')
        sign_in_button.click()
        information = driver.find_element_by_xpath('//div[@class="n54531_outline_sub menu_messages_error"]').text
        information_string = 'Nasz system zablokował Twoje IP z uwagi na zbyt wiele wywołań formularzy, co najczęściej ma miejsce gdy robot spamujący lub łamiący siłowo zabezpieczenia, wywołuje formularz wiele razy. Jeżeli nasz system zadziałał błędnie, serdecznie Cię przepraszamy i prosimy o spróbowanie ponownie później, gdy blokada zostanie automatycznie zdjęta.'

        self.assertEqual(information, information_string)





if __name__ == "__main__":
    unittest.main(verbosity=2)

# verbosity=2
