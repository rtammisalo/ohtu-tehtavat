*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  niina
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ni
    Set Password  niina123
    Set Password Confirmation  niina123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long with letters a-z

Register With Valid Username And Too Short Password
    Set Username  niina
    Set Password  ni123
    Set Password Confirmation  ni123
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long and contain more than letters

Register With Nonmatching Password And Password Confirmation
    Set Username  niina
    Set Password  niina123
    Set Password Confirmation  niina456
    Submit Credentials
    Register Should Fail With Message  Password must match the password confirmation

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
