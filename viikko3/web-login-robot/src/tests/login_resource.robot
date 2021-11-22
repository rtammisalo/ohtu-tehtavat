*** Settings ***
Resource  resource.robot

*** Keywords ***
Login With Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Login Credentials

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open