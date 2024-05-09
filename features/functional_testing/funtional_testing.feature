Feature: Login to Dealsdray Panel
  Scenario: User logs in with valid credentials
    Given I am on the Dealsdray login page
    Then I enter the username "prexo.mis@dealsdray.com" and password "prexo.mis@dealsdray.com"
    Then I click the "Login" button
    Then I click the "Order" element
    Then I click the "orders" link
    Then I click the "Add Bulk Orders" button
    Then I click the "Import" button to upload the "D:\\Rahesh_Automation\\demo-data.xlsx" file
    Then I click the "Validate" button
    Then check the response