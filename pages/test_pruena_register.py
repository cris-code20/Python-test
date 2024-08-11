# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def test_Reister():
#     driver = webdriver.Chrome()
#     driver.get("https://www.domestika.org/auth/sign_up?locale=es")
    
#     driver.implicitly_wait(10)
    
#     driver.find_element(By.ID, "user_email").send_keys("chrisoleman@kukuma.com")
#     driver.find_element(By.ID, "user_password").send_keys("2w3frdfgtd")
   
#     buton = driver.find_element(By.CSS_SELECTOR, ".a-button.a-button--block.js-signup-submit.a-button-md--inline")
#     buton.click()
    
#     driver.save_screenshot('./data/RegistroNegativo.jpg')
    
#     driver.quit();