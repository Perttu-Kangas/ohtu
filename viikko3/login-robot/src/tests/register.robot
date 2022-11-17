*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testuser  testuser123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testuser123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input Credentials  te  testuser123
    Output Should Contain  Username has to be at least 3 chars and [a-z]

Register With Valid Username And Too Short Password
    Input Credentials  testuser  testuse
    Output Should Contain  Password has to be 8 chars and contain numbers or uppercase
    
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testuser  testuserr
    Output Should Contain  Password has to be 8 chars and contain numbers or uppercase

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
