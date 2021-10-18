Feature: API functionality
  Scenario Outline: /api/v1.0/goatmen
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value | post_endpoint                |  get_endpoint        |   return_fields           |
    | firstName   | Fluffy      | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen   | fullName,firstName        |
    | firstName   | Squiggles   | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen   | fullName,firstName        |
    | firstName   | Flopsy      | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen   | fullName,firstName        |
    | firstName   | Bugsy       | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen   | fullName,firstName        |
    | firstName   | Tooty       | /api/v1.0/goatmen/firstName  |  /api/v1.0/goatmen   | fullName,firstName        |

  Scenario Outline: /api/v1.0/goblin
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value  | post_endpoint                |  get_endpoint       |   return_fields             |
    | firstName   | Barry        | /api/v1.0/goblin/firstName   |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | firstName   | Steve        | /api/v1.0/goblin/firstName   |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | firstName   | Dave         | /api/v1.0/goblin/firstName   |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | firstName   | John         | /api/v1.0/goblin/firstName   |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | firstName   | Lemons       | /api/v1.0/goblin/firstName   |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | lastName    | Clark        | /api/v1.0/goblin/lastName    |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | lastName    | Smith        | /api/v1.0/goblin/lastName    |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | lastName    | Taylor       | /api/v1.0/goblin/lastName    |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | lastName    | Brown        | /api/v1.0/goblin/lastName    |  /api/v1.0/goblin   | fullName,firstName,lastName |
    | lastName    | Ball         | /api/v1.0/goblin/lastName    |  /api/v1.0/goblin   | fullName,firstName,lastName |


  Scenario Outline: /api/v1.0/ogre
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value  | post_endpoint             |  get_endpoint     |   return_fields           |
    | firstName   | Thudd        | /api/v1.0/ogre/firstName  |  /api/v1.0/ogre   | fullName,firstName        |
    | firstName   | Mud          | /api/v1.0/ogre/firstName  |  /api/v1.0/ogre   | fullName,firstName        |
    | firstName   | Uh           | /api/v1.0/ogre/firstName  |  /api/v1.0/ogre   | fullName,firstName        |
    | firstName   | Ug           | /api/v1.0/ogre/firstName  |  /api/v1.0/ogre   | fullName,firstName        |
    | firstName   | Bluh         | /api/v1.0/ogre/firstName  |  /api/v1.0/ogre   | fullName,firstName        |


  Scenario Outline: /api/v1.0/orc
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value   | post_endpoint            |  get_endpoint    |   return_fields               |
    | firstName   | Table         | /api/v1.0/orc/firstName  |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | firstName   | Chair         | /api/v1.0/orc/firstName  |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | firstName   | Roof          | /api/v1.0/orc/firstName  |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | firstName   | Dinner        | /api/v1.0/orc/firstName  |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | firstName   | Bin           | /api/v1.0/orc/firstName  |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | lastName    | The weak      | /api/v1.0/orc/lastName   |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | lastName    | The toothless | /api/v1.0/orc/lastName   |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | lastName    | the Sizzler   | /api/v1.0/orc/lastName   |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | lastName    | the sandwich  | /api/v1.0/orc/lastName   |  /api/v1.0/orc   | fullName,firstName,lastName   |
    | lastName    | the nugget    | /api/v1.0/orc/lastName   |  /api/v1.0/orc   | fullName,firstName,lastName   |

  Scenario Outline: /api/v1.0/skeleton
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value   | post_endpoint                 |  get_endpoint         |   return_fields               |
    | firstName   | Cecil         | /api/v1.0/skeleton/firstName  |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | firstName   | Hugo          | /api/v1.0/skeleton/firstName  |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | firstName   | Sir Lucis     | /api/v1.0/skeleton/firstName  |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | firstName   | Lord          | /api/v1.0/skeleton/firstName  |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | firstName   | Lady          | /api/v1.0/skeleton/firstName  |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | lastName    | Of Sussex     | /api/v1.0/skeleton/lastName   |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | lastName    | Belvoir       | /api/v1.0/skeleton/lastName   |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | lastName    | Glaviston     | /api/v1.0/skeleton/lastName   |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | lastName    | Tudor         | /api/v1.0/skeleton/lastName   |  /api/v1.0/skeleton   | fullName,firstName,lastName   |
    | lastName    | Windsor       | /api/v1.0/skeleton/lastName   |  /api/v1.0/skeleton   | fullName,firstName,lastName   |


  Scenario Outline: /api/v1.0/troll
    Given a <field> of <field_value>
    Then I should be able to POST to <post_endpoint>
    And GET to <get_endpoint> will contain <return_fields>

    Examples:
    |  field      | field_value  | post_endpoint              |  get_endpoint  |   return_fields                    |
    | firstName   | Ivar         | /api/v1.0/troll/firstName  |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | firstName   | Flurg        | /api/v1.0/troll/firstName  |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | firstName   | Orb          | /api/v1.0/troll/firstName  |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | firstName   | Jung         | /api/v1.0/troll/firstName  |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | firstName   | Ulfric       | /api/v1.0/troll/firstName  |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | lastName    | Ivar         | /api/v1.0/troll/lastName   |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | lastName    | Flurg        | /api/v1.0/troll/lastName   |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | lastName    | Orb          | /api/v1.0/troll/lastName   |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | lastName    | Jung         | /api/v1.0/troll/lastName   |  /api/v1.0/troll   | fullName,firstName,lastName    |
    | lastName    | Ulfric       | /api/v1.0/troll/lastName   |  /api/v1.0/troll   | fullName,firstName,lastName    |


