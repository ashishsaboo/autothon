Feature: To test Webservice requests

  @webservice
  Scenario Outline: Test add cart request and checkout
    Given Add product "<Product Type>" "<Product>" to cart for user "<User>" - webservice


    Examples:
      | Product Type | Product                          | User  |
      | footwear     | LED Leather Hi-Tops              | guest |
      | housewares   | Coffee Gift Package              | guest |
      | apparel      | Blue Wind Breaker Jacket         | guest |
      | jewelry      | Turquoise Globe Earrings         | guest |
      | beauty       | Vitamin E Oil                    | guest |
      | electronics  | Black Bluetooth Portable Speaker | guest |
      | accessories  | Black Women's Purse              | guest |
      | outdoors     | LED Dog Collar                   | guest |