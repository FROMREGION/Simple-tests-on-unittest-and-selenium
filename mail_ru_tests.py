# pip install unittest
# pip install selenium

import unittest
from selenium import webdriver

WORK_DIR = r'D:\Python Projects\Auto_test_1\'

# №1
# Make screenshot in search 'test'
class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    # Testing Single Input Field.
    def test_singleInputField(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = driver.find_element_by_id("q")
        eleUserMessage.clear()
        eleUserMessage.send_keys("test")

        # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="search:submit"]')
        eleShowMsgBtn.click()

        driver.save_screenshot("search_input_test.png")

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №2
# ClickHomeBTN
class ClickHomeBTN(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickHomeBTN(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Finding
        homebtn = driver.find_element_by_xpath(r'//*[@id="portal-headline"]/table/tbody/tr/td[1]/a[1]')
        homebtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №3
# ClickCOVID
class ClickCOVID(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickCOVID(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[3]/div[2]/div[1]/a[2]')
        eleShowMsgBtn.click()

    # Closing the browser.

    def tearDown(self):
        self.driver.close()

# №4
# Click Облако
class ClickCLOUD(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickCLOUD(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[1]/div[2]/div/a[1]/div/h3')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №5
# ClickTV
class ClickTV(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickTV(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[1]/div[2]/div/a[5]/div/h3')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №6
# Click Delivery
class ClickDELIVERY(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickDELIVERY(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[1]/div[2]/div/a[4]/div/h3')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №7
# ClickICQ
class ClickISQ(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickISQ(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[1]/div[2]/div/a[2]/div')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №8
# ClickREGISTRATION
class ClickRegistration(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickRegistration(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="PH_regLink"]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №9
# Click login
class ClickLogIN(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickLogIN(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = driver.find_element_by_id("q")
        eleUserMessage.clear()
        eleUserMessage.send_keys("test")

        # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="PH_authLink"]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №10
# ClickNews
class ClickNews(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickNews(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="portal-headline"]/table/tbody/tr/td[1]/a[6]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №11
# ClickMoscow
class ClickMoscow(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickMoscow(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[3]/div[2]/div[1]/a[3]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №12
# ClickAboutCompany
class ClickAboutCompany(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickAboutCompany(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="footer"]/a[1]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №13
# ClickHelp
class ClickHelp(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickHelp(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="footer"]/a[3]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №14
# ClickMyWorld
class ClickMyWorld(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickMyWorld(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="ph_my"]/span')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# №15
# ClickAuto
class ClickAuto(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(WORK_DIR + 'chromedriver.exe')

    def test_ClickAuto(self):
        pageUrl = "http://mail.ru"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        eleShowMsgBtn = driver.find_element_by_xpath(r'//*[@id="jAdfx1f"]/div[3]/div[2]/div[1]/a[6]')
        eleShowMsgBtn.click()

    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.


if __name__ == "__main__":
    unittest.main()
