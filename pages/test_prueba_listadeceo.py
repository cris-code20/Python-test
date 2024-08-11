# from selenium import webdriver
# from selenium.webdriver.common.by import By

# def test_perfilUser():
#     driver = webdriver.Chrome()
#     driver.get("https://www.domestika.org/auth/login?locale=es")    
    
#     driver.implicitly_wait(15)
#     driver.find_element(By.ID , "user_email").send_keys("202010703@itla.edu.do")
#     driver.find_element(By.ID, "user_password").send_keys("Metano04")
    
#     driver.find_element(By.CLASS_NAME, " lazyloaded").click()
    
#     driver.find_element(By.CSS_SELECTOR, ".ListItem-LeftContainer.w-full").click()
    
#     driver.save_screenshot('./data/Listado.jpg')
    
#     driver.quit();