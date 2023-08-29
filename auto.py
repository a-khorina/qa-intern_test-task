from selenium import webdriver
from selenium.webdriver.common.by import By 


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")

    element = driver.find_element(By.CLASS_NAME, 'desktop-usq1f1')
    element.click()