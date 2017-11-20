
Feature: Validate voter eligibility when minimum voter age has non-default value

    Background: Changing minimum voter age to non-default value 21
      Given default minimum voter age is 18
      And we change minimum voter age to 21

    @medium  @positive
    Scenario: Voter older than 21 is found eligible
        Given valid age 22
        when we check eligibility
        then voter is found eligible

    @medium @positive
    Scenario: Voter age 21 is found eligible
        Given valid age 21
        when we check eligibility
        then voter is found eligible

    @medium @positive
    Scenario: Voter younger than 21 is found ineligible
        Given valid age 20
        when we check eligibility
        then voter is found ineligible


                      |