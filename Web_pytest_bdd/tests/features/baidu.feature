#noinspection CucumberUndefinedStep
Features: Baidu search

  Background: Enter into home page
    Given Enter"home page"

 Scenario Outline: Search Success
   When input "<searchValue>" and click "search" button
   Then Show "<message>"

   Examples: Success
      |searchValue|message|
      |python     | html|