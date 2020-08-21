Feature: Test  Login Page functionality

@example
Scenario Outline: Login with user and password
Given I login with "<User>" and "<Password>"
Examples:
|User|Password|
|test_user1|test_password1|

@example
Scenario: Login with credentials
Given login with credential
	|User|Password|
	|test_user2|test_password2|
