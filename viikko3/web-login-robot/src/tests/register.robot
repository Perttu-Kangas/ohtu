*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testuser
    Set Password  testpass1
    Set Password Confirmation  testpass1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  tes
    Set Password  testpass1
    Set Password Confirmation  testpass1
    Submit Credentials
    Register Should Fail With Message  Username has to be at least 3 chars and [a-z]

Register With Valid Username And Too Short Password
    Set Username  testuser
    Set Password  testpas
    Set Password Confirmation  testpas
    Submit Credentials
    Register Should Fail With Message  Password has to be 8 chars and contain numbers or uppercase

Register With Nonmatching Password And Password Confirmation
    Set Username  testuser
    Set Password  testpass1
    Set Password Confirmation  testpass2
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  testuser
    Set Password  testpass1
    Set Password Confirmation  testpass1
    Submit Credentials

    Go To Login Page
    Set Username  testuser
    Set Password  testpass1
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  tes
    Set Password  testpass1
    Set Password Confirmation  testpass1
    Submit Credentials

    Go To Login Page
    Set Username  tes
    Set Password  testpass1
    Click Button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
