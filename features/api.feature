Feature: API functionality
  Scenario Outline: /api/v1.0/goatmen
    Given a first name of <first_name>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <fields>

    Examples:
    | first_name  | post_endpoint                |  get_endpoint      |   fields           |
    | Fluffy      | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen | fullName,firstName |
    | Squiggles   | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen | fullName,firstName |
    | Flopsy      | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen | fullName,firstName |