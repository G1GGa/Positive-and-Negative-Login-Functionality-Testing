Test Case: Login Page Authentication Suite
Description: Verify that the login page correctly authenticates valid users and displays appropriate error messages for invalid credentials (invalid username and invalid password).

Pre-conditions: Browser is open and the Practice Test Automation login page URL is loaded.

Test Steps:

Navigate to https://practicetestautomation.com/practice-test-login/

Enter username and password.

Click the Submit button.

Expected Results:

Positive Scenario: Successful login, redirection to the logged-in success page URL, and visibility of the confirmation text ("Congratulations").

Negative Username Scenario: Error message container is displayed with the exact text: "Your username is invalid!"

Negative Password Scenario: Error message container is displayed with the exact text: "Your password is invalid!"
