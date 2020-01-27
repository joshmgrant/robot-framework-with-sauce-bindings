*** Settings ***
Library               SauceActions.py

*** Test Cases ***
Open and Close Sauce Demo
	Start Session
	Go to Demo
	Stop Session
