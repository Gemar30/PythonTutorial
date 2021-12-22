from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/gemarusi/Downloads/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.send_keys("Gemar")

lname = driver.find_element_by_name("lName")
lname.send_keys("Usi")

email = driver.find_element_by_name("email")
email.send_keys("ramegusi@gmail.com")

button = driver.find_element_by_css_selector("form button")
button.click()


# wiki = driver.find_element_by_css_selector("#articlecount a")
# # wiki.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)

