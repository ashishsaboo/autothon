Feature: To test Webservice requests

  @webservice
  Scenario Outline: Test all category webservices
    Given Check category "<Category Name>" response - webservice

    Examples:
      | Category Name |
      | footwear      |
      | housewares    |
      | apparel       |
      | jewelry       |
      | beauty        |
      | electronics   |
      | accessories   |
      | outdoors      |

  @webservice
  Scenario Outline: Test all products webservices
    Given Check category "<Category Name>" products response - webservice

    Examples:
      | Category Name |
      | footwear      |
      | housewares    |
      | apparel       |
      | jewelry       |
      | beauty        |
      | electronics   |
      | accessories   |
      | outdoors      |

  @webservice
  Scenario Outline: Test add cart request and checkout
    Given Add product "<Product Type>" "<Product>" "<Quantity>" to cart for user "<User>" - webservice

    Examples:
      | Product Type | Product                          | Quantity | User     |
      | footwear     | LED Leather Hi-Tops              | 2        | abcdefgh |
      | housewares   | Coffee Gift Package              |          | abcdefgh |
      | apparel      | Blue Wind Breaker Jacket         | 1        | abcdefgh |
      | jewelry      | Turquoise Globe Earrings         | 1        | abcdefgh |
      | beauty       | Vitamin E Oil                    | 1        | abcdefgh |
      | electronics  | Black Bluetooth Portable Speaker | 1        | abcdefgh |
      | accessories  | Black Women's Purse              | 1        | abcdefgh |
      | outdoors     | LED Dog Collar                   |          | abcdefgh |

  @webservice
  Scenario Outline: Test all products webservices
    Given Check Orders response for user "<User Name>" - webservice

    Examples:
      | User Name |
      | abcdefgh  |

