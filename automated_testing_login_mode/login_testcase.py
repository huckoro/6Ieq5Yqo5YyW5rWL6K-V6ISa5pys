import time

from selenium import webdriver
from base_conf import Conf
import unittest


class XXLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(Conf.url)

    def tearDown(self):
        self.driver.quit()

    def _login(self, username, password):
        self.driver.find_element('link text', '登陆').click()
        self.driver.find_element('xpath', '//*[@id="username"]').send_keys(username)
        self.driver.find_element('id', 'password').send_keys(password)
        self.driver.find_element('css selector', '.sub.login').click()
        login_info = self.driver.find_element('class name', 'login_info').text
        try:
            self.assertEqual(username, login_info)
        except AssertionError:
            print('登陆失败')
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace('.', '-'))
            raise

    def test_login_01_true(self):
        # 数据库存在的用户名/正确的密码
        self._login('admin', '123456')

    def test_login_02_error(self):
        # 数据库不存在的用户名
        self._login('admin01', '123456')
