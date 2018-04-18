Feature: Fetch a coloured animal
  In order to understand how to use Concourse in SDC
  As an SDC developer
  I want to see an example pipeline

  Scenario: The one where the application returns a colour and an animal
    When I request a response for "R" and "C"
    Then the response should be "Red Cat"