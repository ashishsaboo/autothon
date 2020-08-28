@run2
Feature: add product and order entry

  @multipleOrder
  Scenario Outline: add prduct and order
    Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
    And I Login with "<UserName>" and "<Password>"
    And I select Item from Category and checkout for "<UserName>"
      | Category | Item                             | Quantity |
      | Footwear | Light Brown Leather Lace-Up Boot | 5        |
      | Beauty   | Watermelon Flavored Lip Balm     | 4        |

    Examples:
      | UserName | Password |
      | *****    | *****    |

#  @multipleOrder
#  Scenario Outline: Order 3 products having difference in 0.01 in total order
#    Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
#    And I Login with "<UserName>" and "<Password>"
#    And I select Item from Category and checkout for "<UserName>"
#      | Category | Item                             | Quantity |
#      | Footwear | Light Brown Leather Lace-Up Boot | 1        |
#      | Footwear | LED Leather Hi-Tops              | 3        |
#      | Apparel  | Accent Scarf                     | 2        |
#
#    Examples:
#      | UserName | Password |
#      | ****     | ******   |

  @createUserAccount
  Scenario Outline: Create Test user
    Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
    And I enter "<username>", "<Password>", "<Email>", "<CountryCode>", "<Mobile>" and "<ExpectedResult>"
    Examples:
      | username | Password      | Email           | CountryCode | Mobile     | ExpectedResult                                                                |
      | krishna  | Abc@123456258 | abcde@gmail.com | India (+91) | 1111111111 |                                                                               |
      |          | Abc@123456258 | abcde@gmail.com | India (+91) | 1111111111 | The following fields must be completed: Username                              |
      | Gururaj  |               | abcde@gmail.com | India (+91) | 1111111111 | The following fields must be completed: Password                              |
      | Asis     | Abc@123456258 |                 | India (+91) | 1111111111 | The following fields must be completed: Email                                 |
#      | Krishna  | Abc@123456258 | abcde@gmail.com | India (+91) |            | The following fields must be completed: Mobile                                |
      | krishna  | abc@123456258 | abcde@gmail.com | India (+91) | 1111111111 | Password did not conform with policy: Password must have uppercase characters |
#      | Asis     | Abc@123456258 | abcdef@         | India (+91) | 1111111111 | Email did not conform with policy                                             |

#  @searchProduct
#  Scenario Outline: Search Product
#    Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
#    And I entered "<productname>"
#    Examples:
#      | productname         |
#      | Exercise Headphones |
#
#  @custSupport
#  Scenario: Customer SupportHelp
#    Given I open "http://d8d7d73w3pkup.cloudfront.net/#/"
#    And I clicked on Help