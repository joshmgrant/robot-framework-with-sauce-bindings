*** Settings ***
Library               SauceLabs.py

*** Test Cases ***
Open and Close Sauce Demo
	Start Session
	Go to Demo
	Stop Session

Verify Title
	Start Session
	Go To Demo
	Title is Correct
	Stop Session
