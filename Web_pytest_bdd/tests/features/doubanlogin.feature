#noinspection CucumberUndefinedStep,NonAsciiCharacters

Feature: DouBan Login Test
  Test DouBan web login

Background:
  Given Redirect to home page

  Scenario Outline: pwLoginSuccess
    When Select the PW way of loggin
    Then input "<username>" and "<password>"
    Then click Login button
    Then "<expected>" can be found

    Examples:
      | username | password | expected|
      |15122888806|huanhuan350881|{"type":"link_text", "value":"说句话", "text": "说句话"} |

  Scenario Outline: loginPhInc
    When input "<phone>"
    Then click sendSMS button
    Then "<expected>" can be found

    Examples:
      | phone | expected|
      |151228886|{"type":"class_name", "value":"fatal-msg", "text": "请正确填写手机号"}|

  Scenario Outline: loginSmsInc
    When input "<phone>"
    Then input "<smsCode>"
    Then click Login button
    Then "<expected>" can be found

    Examples:
      |phone   |  smsCode | expected|
      |15122888806| 123456|{"type":"class_name", "value":"fatal-msg", "text": "验证码输入错误或已过期"} |

  Scenario Outline: loginPwInc
    When Select the PW way of loggin
    Then input "<username>" and incorrect "<password>"
    Then click Login button
    Then "<expected>" can be found

    Examples:
      | username | password | expected|
      |15122888806|huanhuan35881|{"type":"class_name", "value":"fatal-msg", "text": "用户名或密码错误"} |

  Scenario Outline: logout
    When Select the PW way of loggin
    Then input "<username>" and "<password>"
    Then click Login button
    Then click my account
    Then click logout button
    Then "<expected>" can be found

    Examples:
      | username | password | expected|
      |15122888806|huanhuan350881|{"type":"link_text", "value":"登录豆瓣", "text": "登录豆瓣"} |