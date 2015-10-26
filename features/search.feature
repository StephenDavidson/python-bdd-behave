Feature: Search

  Background: User visits the home page
    Given I visit the home page


  Scenario: User would like to search for a topic
    When I search for test
    Then I should be on the results page
    And the first search result should be visible