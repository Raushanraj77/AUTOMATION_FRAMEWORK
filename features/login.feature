Feature: Validate the login feature

  Background:
    #Given Launch the browser #Handled as befor scenario
    When Open the url
    Then The login portal has been opened

  @valid_login
  Scenario: Login with valid credentials    
    Given Provide the username and password
    When Click on the Login button
    Then Login is successful and dashboard is opened
    And Close the browser

  Scenario Outline: Login with invalid credentials
    Given Provide the username "<username>" and password "<password>"
    When Click on the Login button
    Then Login is failed and invlid credential error is displayed
    And Close the browser
    Examples:
      | username | password |
      | abcd     | 1234     |
      | 35473    | afsdf    |

  Scenario: Login with empty username
    Given Provide the password "admin123"
    When Click on the Login button
    Then Login is failed and empty username error is displayed
    And Close the browser

  Scenario: Login with empty password
    Given Provide the username "Admin"
    When Click on the Login button
    Then Login is failed and empty password error is displayed
    And Close the browser