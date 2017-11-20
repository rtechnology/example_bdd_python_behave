
Feature: Handling invalid inputs

    @high @negative
    Scenario Outline: Invalid inputs for voter age
         Given default minimum voter age is 18
         And voter age input having <invalid_type>  <value>
         When we check eligibility
         Then error is returned

         Examples: Invalid Input
          |  invalid_type            |  value |
          |  special_character       |  &     |
          |  alpha_character         |  x     |
          |  negative_integer        |  -1    |
          |  decimals                |  5.1   |

    @medium @negative
    Scenario Outline: Invalid inputs for minimum voter age
         Given minimum voter age input having <invalid_type> <value>
         When we change minimum voter age to this invalid value
         Then error is returned

         Examples: Invalid Input
          |  invalid_type            |  value |
          |  special_character       |  &     |
          |  alpha_character         |  x     |
          |  negative_integer        |  -1    |
          |  decimals                |  5.1   |