from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.headless = True

url = 'https://www.amazon.in/'
search_string = ['Double Sided Clock', 'Railway Clock']

print("Initialising Driver")
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)


try:
    print("Starting Crawler")
    driver.get(url)
    search_box = driver.find_element(By.ID,'twotabsearchtextbox')
    search_box.send_keys(search_string[1])
    search_box.send_keys(Keys.RETURN)

    products = driver.find_elements(By.TAG_NAME, 'span')
    
    count = 0
    print(f"Products = {len(products)} /n {type(products[0])}")
    for p in products:
        print(p.text)
    print(f'{ count = }')

finally:
    print("Closing Driver")
    driver.quit()