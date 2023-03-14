# **API Testing**

## **Table of content**

* [Automated Testing](#automated-testing)
* [Manual Testing](#manual-testing)
    * [Testing Endpoints](#testing-endpoints)
    * [Testing CRUD Functionality](#testing-crud-functionality)
        * [Saves App](#saves-app)
        * [Followers App](#followers-app)
        * [Notes App](#notes-app)
        * [Profiles App](#profiles-app)
        * [Property App](#property-app)
* [Code Validation](#code-validation)


<hr>

## **Automated Testing**

Automated tests were created for the Property app to demonstrate automated testing knowledge of the developer. The following tests carried out demonstrate that only authenticated sellers are able to create, edit and delete property objects.

* Tests created by the developer can be found [here](https://github.com/keironchaudhry/property-andalucia-backend/blob/main/property/test_views.py).

* A separate document for Coverage can be found [here](/documents/coverage.md).

<hr>


## **Manual Testing**

### **Testing Endpoints**

| **URL** | **Passed** |
| --- | --- |
| root | &check; |
| /property/ | &check; |
| /property/:id/ | &check; |
| /property/create/ | &check; |
| /profiles/ | &check; |
| /profiles/:id/ | &check; |
| /notes/ | &check; |
| /notes/:id | &check; |
| /saves/ | &check; |
| /saves/:id/ | &check; |
| /followers/ | &check; |
| /followers/:id/ | &check; |


## **Testing CRUD Functionality**

### **Saves App**

| App | Action | Authenticated | Anonymous | Passed |
| --- | --- | --- | --- | --- |
| Saves | Read (Listed Objects) | Returns array of user-owned saves objects | Returns an empty array | &check; |
| Saves | Read (Object Owner + :id) | Returns detailed saves object | 404 Response | &check; |
| Saves | Read (Not Object Owner + :id) | 404 Response | 404 Response | &check; |
| Saves | Read (Invalid :id) | 404 Response | 404 Response | &check; |
| Saves | Create | 201 Response | Access unavailable | &check; |
| Saves | Delete | 204 Response | Access unavailable | &check; |
| Saves | Update | 200 Response | Access unavailable | &check; |

### **Followers App**

| App | Action | Authenticated | Anonymous | Passed |
| --- | --- | --- | --- | --- |
| Followers | Read (Listed Objects) | Returns array of followers objects | Returns array of owned followers objects | &check; |
| Followers | Read (Object Owner + :id) | Returns detailed followers object | Returns detailed followers object | &check; |
| Followers | Read (Not Object Owner + :id) | Returns detailed followers object | Returns detailed followers object | &check; |
| Followers | Read (Invalid :id) | 404 Response | 404 Response | &check; |
| Followers | Create | 201 Response | Access unavailable | &check; |
| Followers | Delete | 204 Response | Access unavailable | &check; |
| Followers | Update | 200 Response | Access unavailable | &check; |

### **Notes App**

| App | Action | Authenticated | Anonymous | Passed |
| --- | --- | --- | --- | --- |
| Notes | Read (Listed Objects) | Returns array of user-owned notes objects | Returns an empty array | &check; |
| Notes | Read (Object Owner + :id) | Returns detailed notes object | 404 Response | &check; |
| Notes | Read (Not Object Owner + :id) | 404 Response | 404 Response | &check; |
| Notes | Read (Invalid :id) | 404 Response | 404 Response | &check; |
| Notes | Create | 201 Response | Access unavailable | &check; |
| Notes | Delete | 204 Response | Access unavailable | &check; |
| Notes | Update | 200 Response | Access unavailable | &check; |


### **Profiles App**

| App | Action | Authenticated | Anonymous | Passed |
| --- | --- | --- | --- | --- |
| Profile | Read (Listed Objects) | Returns array of profile objects | Returns array of profile objects | &check; |
| Profile | Read (Detail) | Returns detailed profile object | Returns detailed profile object | &check; |
| Profile | Create | Not available | Not available | &check; |
| Profile | Update | 200 Response | Access unavailable | &check; |

### **Property App**

| App | Action | Authenticated | Anonymous | Passed |
| --- | --- | --- | --- | --- |
| Property | Read (Listed Objects) | Returns array of property objects | Returns array of property objects | &check; |
| Property | Read (Detail) | Returns detailed property object | Returns detailed property object | &check; |
| Property | Create | 201 Response | Access unavailable | &check; |
| Property | Update | 200 Response | Access unavailable | &check; |
| Property | Delete | 204 Response | Access unavailable | &check; |

<hr>

## **Code Validation**

The `pycodestyle` package was used to continuously check code during development with the PEP8 Style Convention. 

No validation errors were found at time of deployment.

<hr>
