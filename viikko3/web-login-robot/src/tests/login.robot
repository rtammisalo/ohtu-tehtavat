*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Login With Credentials  kalle  kalle123
    Login Should Succeed

Login With Incorrect Password
    Login With Credentials  kalle  kalle456
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Login With Credentials  olematon  olematon11
    Login Should Fail With Message  Invalid username or password
