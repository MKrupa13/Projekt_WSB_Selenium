import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.mantoshop.pl/pol_m_NA-CO-DZIEN-252.html')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_ASortName(self):
        driver = self.driver
        cookie = driver.find_element_by_id('ckdsclmrshtdwn_v2')
        cookie.click()
        select_category = driver.find_element_by_link_text('NA CO DZIEŃ')
        select_category.click()
        change_quantity = driver.find_element_by_id('s_setting_1')
        change_quantity.click()
        quantity_60 = driver.find_element_by_partial_link_text('Pokaż 60')
        quantity_60.click()
        click_sort = driver.find_element_by_id('s_setting_0')
        click_sort.click()
        sort_by_name_descending = driver.find_element_by_xpath('//a[@data-index="1"]')
        sort_by_name_descending.click()
        products_name = list()
        product_name = driver.find_elements_by_class_name("product-name")
        for product in product_name:
            products_name.append(product.text)
       # print(products_name)
        products_name_2 = products_name.copy()
        products_name_2.sort(reverse=True)
       # print(products_name_2)
        self.assertListEqual(products_name, products_name_2)

    def test_Menu1(self):
        driver = self.driver
        move_mouse_to_element = driver.find_element_by_link_text('NA CO DZIEŃ')
        Hover = ActionChains(driver).move_to_element(move_mouse_to_element)
        Hover.perform()
        menu_is_showed = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][1]//ul[@class="navbar-subnav"]')
        self.assertTrue(menu_is_showed.is_displayed())

    def test_Menu2(self):
        driver = self.driver
        move_mouse_to_element = driver.find_element_by_link_text('ODZIEŻ TRENINGOWA')
        Hover = ActionChains(driver).move_to_element(move_mouse_to_element)
        Hover.perform()
        menu_is_showed = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][2]//ul[@class="navbar-subnav"]')
        self.assertTrue(menu_is_showed.is_displayed())

    def test_Menu3(self):
        driver = self.driver
        move_mouse_to_element = driver.find_element_by_link_text('SPRZĘT TRENINGOWY')
        Hover = ActionChains(driver).move_to_element(move_mouse_to_element)
        Hover.perform()
        menu_is_showed = driver.find_element_by_xpath('//div[@id="menu_navbar"]//li[@class="nav-item"][3]//ul[@class="navbar-subnav"]')
        self.assertTrue(menu_is_showed.is_displayed())

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
        information_string = 'Podany login lub hasło nie jest poprawne.'
        self.assertEqual(information, information_string)





if __name__ == "__main__":
    unittest.main(verbosity=2)

