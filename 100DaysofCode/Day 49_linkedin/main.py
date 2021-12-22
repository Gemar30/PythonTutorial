from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/gemarusi/Downloads/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

linked_in_site = driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2838311860&f_AL=true&keywords=database%20administration")

button = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
button.click()

email = driver.find_element_by_id("username")
email.send_keys("")

password = driver.find_element_by_id("password")
password.send_keys("")
password.send_keys(Keys.ENTER)

apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

next_button = driver.find_element_by_css_selector(".display-flex button")
next_button.click()
next_button.click()

db_work_exp = driver.find_element_by_id("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2838311860,39740965,numeric)")
db_work_exp.send_keys("1")



