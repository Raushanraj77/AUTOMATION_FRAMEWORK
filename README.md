## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.
Sample test side used in this project is - https://opensource-demo.orangehrmlive.com/

| Package Name          | Latest Version | Release Date |
| --------------------- | -------------- | ------------ |
| allure-behave         | 2.14.2         | May 6, 2025  |
| allure-python-commons | 2.14.2         | May 6, 2025  |
| attrs                 | 25.3.0         | Mar 13, 2025 |
| behave                | 1.2.6          | Feb 25, 2018 |
| iniconfig             | 2.1.0          | Mar 19, 2025 |
| packaging             | 25.0           | Apr 19, 2025 |
| parse                 | 1.20.2         | Jun 10, 2024 |
| parse-type            | 0.6.4          | Oct 3, 2024  |
| pluggy                | 1.3.0          | Mar 20, 2025 |
| py                    | 1.11.0         | Nov 4, 2021  |
| pyparsing             | 3.2.3          | Mar 24, 2025 |
| pytest                | 8.1.1          | Apr 2, 2025  |
| selenium              | 4.21.0         | May 20, 2025 |
| six                   | 1.16.0         | Jun 8, 2021  |
| toml                  | 0.10.2         | Oct 13, 2021 |
| urllib3               | 2.2.1          | May 15, 2025 |

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.

**configuration** directory contains the configuration files

**drivers** directory contains the chrome and firefox driver for mac

**requirements.txt** file contains all the python packages needed to run this framework

**reports** directory contains the json files generated with allure reports



### **Commands to run the tests**

**To run the test with allure report**
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature`

**To run the test with allure report for entire feature**
`behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results features/`


**To run the test without allure report** `behave features/login.feature`

**To generate the html allure report from the json files inside reports folder**
`allure serve reports/`

**Create Virtual Environment**
In terminal navigate to Project folder and type : python3 –m venv venv  and enter one popup will come click on yes. 
For activate Virtual environment : source venv/bin/activate 

**For running using Shell script handling re-run of failed test**
chmod +x retry_runner.sh 
./retry_runner.sh
