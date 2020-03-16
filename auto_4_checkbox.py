from selenium import webdriver
import os, time


class Soulution:
    def __init__(self):
        driver = webdriver.Chrome()
        file_path = 'file:///' + os.path.abspath('checkbox.html')
        driver.get(file_path)
        # inputs = driver.find_elements_by_tag_name('input')
        # for input in inputs:
        #     if input.get_attribute('type') == 'checkbox':
        #         input.click()
        # time.sleep(5)
        #
        # driver.quit()

        checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')

        for checkbox in checkboxes:
            checkbox.click()

        print(len(checkboxes))
        driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

        time.sleep(5)
        driver.quit()


Soulution()
