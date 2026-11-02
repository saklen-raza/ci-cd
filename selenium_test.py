
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

print("Starting TechFest Selenium Tests...")

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor="http://selenium:4444",
    options=options
)

wait = WebDriverWait(driver, 10)

try:
    driver.get("http://event-registration/")

    print("Website opened successfully.")

    name = driver.find_element(By.ID, "name")
    email = driver.find_element(By.ID, "email")
    phone = driver.find_element(By.ID, "phone")
    college = driver.find_element(By.ID, "college")
    event = Select(driver.find_element(By.ID, "event"))

    register = driver.find_element(By.ID, "registerBtn")
    error = driver.find_element(By.ID, "error")
    success = driver.find_element(By.ID, "success")

    # TEST 1: Empty name
    email.send_keys("test@example.com")
    phone.send_keys("9876543210")
    college.send_keys("ABC Engineering College")
    event.select_by_visible_text("Hackathon")

    register.click()

    wait.until(
        lambda d: "Please fill in all the fields" in error.text
    )
    print("TEST 1 PASSED: Empty name is rejected.")

    # TEST 2: Invalid email
    name.send_keys("Saklen Raza")
    email.clear()
    email.send_keys("invalidemail")

    register.click()

    wait.until(
        lambda d: "valid email" in error.text
    )
    print("TEST 2 PASSED: Invalid email is rejected.")

    # TEST 3: Invalid phone number
    email.clear()
    email.send_keys("test@example.com")
    phone.clear()
    phone.send_keys("12345")

    register.click()

    wait.until(
        lambda d: "10-digit" in error.text
    )
    print("TEST 3 PASSED: Invalid phone number is rejected.")

    # TEST 4: Valid registration
    phone.clear()
    phone.send_keys("9876543210")

    register.click()

    wait.until(
        lambda d: "Registration successful" in success.text
    )

    print("TEST 4 PASSED: Valid registration is successful.")

    # TEST 5: Check participant table
    wait.until(
        lambda d: d.find_element(By.ID, "count").text == "1"
    )

    rows = driver.find_elements(
        By.CSS_SELECTOR, "#regTable tbody tr"
    )

    assert len(rows) == 1
    assert rows[0].find_elements(By.TAG_NAME, "td")[1].text == "Saklen Raza"
    assert driver.find_element(By.ID, "count").text == "1"

    print("TEST 5 PASSED: Participant added to table.")

    print("ALL SELENIUM TESTS PASSED!")

finally:
    driver.quit()
