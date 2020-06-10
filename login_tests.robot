*** Settings ***
Library   SauceLabs.py
Library   LoginPage.py            

*** Test Cases ***
Valid Login Case
    Start Session
    Go To Demo
    Login As  standard_user  secret_sauce
    Verify User Is Logged In
    Stop Session

Invalid Login Case
    Start Session
    Go To Demo
    Login As  invalid  invalid
    Verify User Is Not Logged In
    Stop Session
