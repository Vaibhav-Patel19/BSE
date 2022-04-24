
# Restaurant/Cafe/Bar Order Management App 

![image](https://user-images.githubusercontent.com/72696677/147384776-f1294f06-537e-4f1a-a5e8-d2985f769227.png)

A Web-App for Interactive and Innovative way of Ordering Food/Drinks in a Restaurant.


![image](https://user-images.githubusercontent.com/72696677/147385238-ad4cd89f-69d6-4547-b1b7-5df01b5276ec.png)


- [Objective](#objective)
- [Features](#features)
- [Tools and Technology Used](#tools)
- [Design and Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [List of Tables](#tables)
- [Bug Reporting](#bug)
- [Feature Request](#feature-request)
- [License](#license)

<a id = "objective"></a>

## Objective

+ Trying to create a best End-to-End Solution for a Food/Drinks Ordering App which will be of a great use after Covid19 Pandemic where customers fill unsafe while using a HardCopy Menu.
+ Users no longer have to call a Waiter for Ordering or for doing a Payment.
+ Making the Ordering Drinks Task very Interactive and Innovative by Introducing Dynamic Pricing of Drinks(Prices of drinks change while ordering depending on our Algorithm).

<a id = "features"></a>
## Project Background

- Bar Stock Exchange is Web-Based Mobile Application which can be used in Restaurant-Bars, replacing Hardcopy Menu for Food and Drinks Ordering.

- Whats Unique about this application is that a Stock Market Theme is implemented while ordering any drink using the application. 

- Prices of Drinks increases and Decreases Dynamically(async) while Ordering drinks, backed by algorithms created for changing the prices.

- Implemented Google Sign Up and Sign In with the help of **GMAIL API** to increase customer experience while using the application.

- Implemented functionalities like - Food Items Filtering based on Newest, Most Ordered, Admin Panel, Social-Auth, Smooth Scrolling, Dynamic Pricing, Dynamic Ordered Item Page, End-to-End Payments Solution.

- Three Django Apps were used which are <b> main, registration and payments </b>.

  - Main App includes these Pages and their different views/functionalities – Home, Explore, Menu, Bar menu, Order Page

  - Registration App contains the Landing(index) Page which is used for scanning the QR code which will redirect user to registration page of app.

  - Payments App provides payment of bill facility to a user. Integrated RazorPay Payments Sytems in which user can pay through all Online Payments modes possible.


<a id = "getting-started"></a>
## Getting Started

### Prerequisites

Latest Stable version of Python should be installed, you can download from [here](https://www.python.org/downloads/)


### Instructions of setting up the project on your local machine

1. Open Terminal and Clone the Repo
```
git clone https://github.com/dans77777/Intern-admin-collaboration.git
```
2. Go inside the Project Directory using <b> cd </b> and install the dependencies using the command:

```
pip install -r requirements.txt
```

3. Run Command in the terminal for running the App

```
Python manage.py runserver
```

Your Application Server would be live and you can access the App using url - "http..." 

<a id= "tools"></a>
## Tools and Technology Used

- Front-End Interface - HTML, CSS, JavaScript
- Programming Language - Python(Django)
- Database - sqlite
- Other Technologies - jQuery, Ajax

<a id = "screenshots"></a>
## Few Screenshots

<div align="center">

User Sign Up            |  Home Page
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/72696677/147385255-78a298c0-62df-4f30-a651-463dfe3fbb2c.png)   |  ![image](https://user-images.githubusercontent.com/72696677/147385271-a7d78a9a-86ca-4600-ad7c-1f72e4958f01.png)



Ordered Items Page          |  Bar Menu
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/72696677/147385311-d7518305-809f-410e-8654-99aa2368d16b.png)  |  ![image](https://user-images.githubusercontent.com/72696677/147385284-6b468631-cc66-4cfb-9d06-48bb523898c5.png)

Food Menu <br/>
![image](https://user-images.githubusercontent.com/72696677/147385292-ae0ee4b9-3ce6-4806-99ec-b52673380c8d.png)  

</div>
 
<a id = "tables"></a>

## List of Tables

+ Users - Stores all the User Data. There are two types of User : Admin Staff of Restaurant and a Customer.
+ FoodMenu - Stores all the data related to Food Products offered by a Restaurant.
+ BarMenu -  Stores all the data related to Bar/Drinks offered by a Restaurant.
+ FoodOrder - Stores all the Food Order of a User.
+ BarOrder - Stores all the Bar Order of a User.
+ Payments - Stores details regarding Bill of a User.
+ Social Accounts - Stores all the data regarding the Social Accounts used while Sign Up.

<a id= "bug"></a>

## 🐛 Bug Reporting

Feel free to [open an issue](https://github.com/Vaibhav-Patel19/BSE/issues) on GitHub if you find any bug.

<a id="feature-request"></a>

## ⭐ Feature Request

- Feel free to [Open an issue](https://github.com/Vaibhav-Patel19/BSE/issues) on GitHub to request any additional features you might need for your use case.
- Connect with me on [LinkedIn](https://www.linkedin.com/in/vaibhavpatel19/). I'd love ❤️️ to hear where you are using this library.

<a id= "feature-request"></a>


<a id="license"></a>

## 📜 License

This software is open source, licensed under the [MIT License](https://github.com/Vaibhav-Patel19/BSE/blob/master/LICENSE).

<!-- # https://django-allauth.readthedocs.io/en/latest/installation.html -->
