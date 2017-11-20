
Feature: Validate voter eligibility when minimum voter age has default value

    Background: Keeping default value of minimum voter age
        Given default minimum voter age is 18

    @high @positive
    Scenario: Voter older than 18 is found eligible
        Given valid age 19
        When we check eligibility
        Then voter is found eligible

    @high @positive
    Scenario: Voter age 18 is found eligible
        Given valid age 18
        When we check eligibility
        Then voter is found eligible

    @high @positive
    Scenario: Voter younger than 18 is found ineligible
        Given valid age 17
        When we check eligibility
        Then voter is found ineligible

