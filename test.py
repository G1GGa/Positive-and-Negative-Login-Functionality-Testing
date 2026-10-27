from playwright.sync_api import sync_playwright

# Test case 1: Positive LogIn test


def test_positive_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #enter in browser
        page.goto("https://practicetestautomation.com/practice-test-login/")
        # Username
        page.locator("#username").fill("student")
        # Password
        page.locator("#password").fill("Password123")
        #click submit
        page.locator("#submit").click()
        #check positive url address:
        assert "logged-in-successfully" in page.url
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert page.locator("text=Congratulations").is_visible()
        assert "Congratulations" in page.content()
        #latency
        page.wait_for_timeout(3000)

# Test case 2: Negative username test

def test_negative_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #enter in browser
        page.goto("https://practicetestautomation.com/practice-test-login/")
        #Type username incorrectUser into Username field
        page.locator("#username").fill("incorrectUser")
        #password 
        page.locator("#password").fill("Password123")
        #Push Submit button
        page.locator("#submit").click()
        #Verify error message is displayed
        assert page.locator("#error").is_visible()
        #Verify error message text is Your username is invalid!
        assert ("Your username is invalid!"in page.locator("#error").inner_text())
        #latency
        page.wait_for_timeout(3000)

#Test case 3: Negative password test
def test_negative_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #enter in browser
        page.goto("https://practicetestautomation.com/practice-test-login/")
        #Type username student into Username field
        page.locator("#username").fill("student")
        #password
        page.locator("#password").fill("incorrectPassword")
        #Push Submit button
        page.locator("#submit").click()
        #Verify error message is displayed
        assert page.locator("#error").is_visible()
        #Verify error message text is Your password is invalid!
        assert ("Your password is invalid!"in page.locator("#error").inner_text())
        #latency
        page.wait_for_timeout(3000)

test_negative_password()