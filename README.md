# autoTest
API and Web auto test based on Python(keep updating)

These projects are my first efforts. 
Sincerely hope you can give me some advice if you are interested.
email：Spencer.huanhuan@outlook.com

API：-> for [unittest + HTTPTestRunner] and [pytest + allure]
1. Using flask module to mock two api: register and login.
2. Visiting mysql(local database) to insert new user after request register api successfully, checking if user exists in DB.
3. Visiting mysql to assert if user exists and match the password in DB
4. Using excel as the testcase(testData), and generate report by HTTPTestRunner
5. Using yaml file to store the config
6. Finish the optimization
7. Creating another project based on above project, using pytest+allure to working on it

Web: -> for [unittest + HTTPTestRunner] and [pytest_bdd + allure] and [pytest + allure]
1. Using json file as the testcase(testData), and generate report by HTTPTestRunner
2. Using yaml file to maintain every page's elements
3. The optimization of project framework is done
4. Creating another project based on above project, using pytest_bdd+allure to work on it
5. Creating another project based on above project， using pytest + allure to work on it.
