import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_loginPage(self):
        driver = self.driver

        Current_URL = driver.current_url
        time.sleep(2)
        assert Current_URL == f'{conftest.setup.domain}/assets/welcome.html'

    def test_login(self):
        driver = self.driver

        driver.find_element(By.ID, "email").send_keys("admin@kaymera.com")
        driver.find_element(By.ID, "password").send_keys("password")
        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()

        driver.find_element(By.ID, "accessCode").send_keys("")
        sendAccessCode = driver.find_element(By.ID, "submit")
        sendAccessCode.click()

        # ------------- Dashboard page --------------------------------------------FAil when internet il low
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Dashboard"))
        )
        print(element.text)  # 'value not used ' solution

        time.sleep(2)
        Current_URL = driver.current_url
        assert Current_URL == f'{conftest.setup.domain}/assets/index.html#/dashboard/system'

    # -------------Devices----------------------------------------------------

    def test_Devices(self):
        driver = self.driver
        action = ActionChains(driver)

        devicesButton = driver.find_element(By.LINK_TEXT, "Devices")
        action.move_to_element(devicesButton).click().perform()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button"))
        )
        print(element.text)  # 'value not used ' solution

        Current_URL = driver.current_url
        assert Current_URL == f'{conftest.setup.domain}/assets/index.html#/devices/list/org/57d686cce4b046fcd03efcc6/detailed'

    def test_addDeviceDropDownMenu(self):
        driver = self.driver
        action = ActionChains(driver)

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span"))
        )
        print(element.text)  # 'value not used ' solution

        AddDevice = driver.find_element(By.XPATH,
                                        "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button/span")
        action.move_to_element(AddDevice).click().perform()

        expected_list = ["Add CipherFort 2.0", "Add CipherFort", "Add CipherBond", "Add CipherWatch", "Upload CSV"]
        curent_list = [element.text for element in
                       driver.find_elements(By.XPATH, '//ul[@class="dropdown-menu right"]/li')]

        assert expected_list == curent_list

    def test_addBond(self):
        driver = self.driver

        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        #     (By.XPATH, "//div[@class='dropdown km-animated-dropdown ng-scope'][2]/button"))
        # )
        # print(element.text)  # 'value not used ' solution

        addBond = driver.find_element(By.LINK_TEXT, "Add CipherBond")
        addBond.click()

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='First Name']"))
        )
        element.send_keys("Bond")

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Last Name']"))
        )
        element.send_keys("CreatedBy_Postman")

        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Email']"))
        )
        element.send_keys("svetlana.kalchenko@kaymera.com")

        driver.find_element(By.ID, "group").click()
        groupName = driver.find_element(By.XPATH, "//*[@id='group']/option[18]")
        groupName.click()

        driver.find_element(By.ID, "config").click()
        config = driver.find_element(By.XPATH, "//*[@id='config']/option[27]")
        config.click()

        driver.find_element(By.ID, "expirationDateSelection").click()
        expDate = driver.find_element(By.XPATH, "//*[@id='expirationDateSelection']/option[2]")
        expDate.click()

        ok = driver.find_element(By.XPATH, "//div[@class='modal-footer ng-scope']/button[1]")
        ok.click()

    def test_findByEmail(self):
        driver = self.driver

        searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-search']/div/form/input")))

        searchField.send_keys("svetlana.kalchenko@kaymera.com")

    # TODO! add assertion

    # def test_DeleteByEmail(self):
    #     driver = self.driver
    #
    #     checkBox=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")
    #     checkBox.click()

    # bulk_Change=driver.find_element(By.XPATH,"//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
    # bulk_Change.click()

    # TODO! no option to delete

    def test_resetSIM(self):
        driver = self.driver

        checkbox = driver.find_element(By.XPATH,
                                       "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/i")

        actions = ActionChains(driver)
        actions.move_to_element(checkbox).perform()
        driver.execute_script("arguments[0].click();", checkbox)

        bulk_Change = driver.find_element(By.XPATH,
                                          "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[1]/span[2]/ksc-bulk-operations/button")
        bulk_Change.click()

        reset_Sim = driver.find_element(By.XPATH, "// ul[@class='list-unstyled'][1]/li[4]")
        reset_Sim.click()

        alertOK = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
        alertOK.click()

    def test_editBond(self):
        driver = self.driver

        deviceBond = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='edit-devices']/ui-view/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]")))
        deviceBond.click()

        editButton = driver.find_element(By.XPATH, "//*[@id='device-details']/div/div[1]/span[2]/div/button[2]")
        editButton.click()

        lastNameInput = driver.find_element(By.XPATH, "//input[@id='lastname']")
        lastNameInput.clear()
        lastNameInput.send_keys("updatedBy_Postman")

        saveButton = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[3]/button[1]")
        saveButton.click()

        fullName = driver.find_element(By.XPATH,
                                       "//*[@id='device-details']/div/div[2]/div/div/div[1]/div[2]/label[1]/span")
        updatedName = fullName.text

        assert updatedName == "Bond updatedBy_Postman"
