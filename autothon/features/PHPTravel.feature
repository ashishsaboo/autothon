Feature: Test  Login Page of php travels

@example3
Scenario Outline: Test php travels Demo website
Given I get "https://www.orangehrm.com/"
And I login to Application using "<User>" and "<Password>"
Examples:
	|User|Password|
	|user@phptravels.com|demouser|