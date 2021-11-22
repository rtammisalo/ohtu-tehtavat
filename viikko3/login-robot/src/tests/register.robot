*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  muumuu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  muumuu123
    Input Credentials  kalle  maamaa456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  passw0rd
    Output Should Contain  Username must be at least 3 characters long with letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  passw0
    Output Should Contain  Password must be at least 8 characters long and contain more than letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  password
    Output Should Contain  Password must be at least 8 characters long and contain more than letters

*** Keywords ***
Input New Command
    Input  new
