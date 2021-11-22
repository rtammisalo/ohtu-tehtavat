*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register With Credentials  niina  niina123  niina123
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register With Credentials  ni  niina123  niina123
    Register Should Fail With Message  Username must be at least 3 characters long with letters a-z

Register With Valid Username And Too Short Password
    Register With Credentials  niina  ni123  ni123
    Register Should Fail With Message  Password must be at least 8 characters long and contain more than letters

Register With Nonmatching Password And Password Confirmation
    Register With Credentials  niina  niina123  niina456
    Register Should Fail With Message  Password must match the password confirmation

Login After Successful Registration
    Register With Credentials  niina  niina123  niina123
    Register Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Login With Credentials  niina  niina123
    Login Should Succeed

Login After Failed Registration
    Register With Credentials  niina  n123  n123
    Register Should Fail With Message  Password must be at least 8 characters long and contain more than letters
    Go To Login Page
    Login Page Should Be Open
    Login With Credentials  niina  n123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register With Credentials
    [Arguments]  ${username}  ${password}  ${password confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password confirmation}
    Submit Credentials

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
