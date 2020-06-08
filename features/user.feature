Feature: User authentication, sign up, sign out, and profile features

  Scenario Outline: The user wants to sign in to the platform
      Given a the selection of a <sign in method>
      And the <username>, the <email>
      And the user <password>
      When the user sign in
      Then the system stores the user basic account information
      And the system encripts the password
      And the system sends a email confirmation request to the user
    Examples: User information
      | sign in method | username | email                   | password |
      | basic          | user     | user@email.com          | 1234     |
      | google         | user     | user@gmail.com          | 1234     |
      | facebook       | user     | user_facebook@gmail.com | 1234     |