Feature: Test account creation

#@singleOrder
#Scenario Outline: Test user creation
#Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
#And I Login with "<UserName>" and "<Password>"
#And I select "<Item>" from "<Category>"
#Then I checkout
#Examples:
#	|UserName|Password|Category|Item|
#	|Autothonteam3|Autothonteam@3|Footwear|Light Brown Leather Lace-Up Boot|
	

@multipleOrder
Scenario Outline: Test user creation
Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
And I Login with "<UserName>" and "<Password>"
And I select Item from Category and checkout
	|Category|Item|Quantity|
	|Footwear|Light Brown Leather Lace-Up Boot|5|
	|Footwear|LED Leather Hi-Tops|3|
	
Examples:
	|UserName|Password|
	|Autothonteam3|Autothonteam@3|