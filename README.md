# **SOFE3650 Project - Social Calendar**

This project is based on the SOFE2720 Final Project, found here: https://github.com/SOFE2720/Social-Calendar-Group-12

The old README can be found [here](https://github.com/madlitch/SOFE3650-Project/blob/main/README_OLD.md)

## Table of Contents

1. [Introduction](#introduction)
2. [Members](#members)
3. [Requirements](#Requirements)
    1. [Use Cases](#use-cases)
    2. [Quality Attributes](#quality-attributes)
    3. [Constraints](#constraints)
    4. [Concerns](#concerns)
4. [ADD Iteration 1](#add-iteration-1)
    1. [Reviewing Inputs](#11-reviewing-inputs)
    2. [Iteration Goal, Driver Selection](#12-establish-iteration-goal-by-selecting-drivers)
    3. [Refine System Elements](#13-refine-system-elements)
    4. [Design Concepts that Satisfy the Selected Drivers](#14-select-one-or-more-design-concepts-that-satisfy-the-selected-drivers)
    5. [Architectural Elements, Responsibilities, and Interfaces](#15-instantiate-architectural-elements-allocate-responsibilities-and-define-interfaces)
    6. [Sketch Views and Record Design Decisions](#16-sketch-views-and-record-design-decisions)
    7. [Design Analysis, Goal Review, Design Purpose](#17-analysis-of-current-design-iteration-goal-review-and-achievement-of-design-purpose)
6. [ADD Iteration 2](#add-iteration-2)
    1. [Iteration Goal, Driver Selection](#21-establish-iteration-goal-by-selecting-drivers)
    2. [Refine System Elements](#22-refine-system-elements)
    3. [Design Concepts that Satisfy the Selected Drivers](#23-select-one-or-more-design-concepts-that-satisfy-the-selected-drivers)
    4. [Architectural Elements, Responsibilities, and Interfaces](#24-instantiate-architectural-elements-allocate-responsibilities-and-define-interfaces)
    5. [Sketch Views and Record Design Decisions](#25-sketch-views-and-record-design-decisions)
    6. [Design Analysis, Goal Review, Design Purpose](#26-analysis-of-current-design-iteration-goal-review-and-achievement-of-design-purpose)
8. [ADD Iteration 3](#add-iteration-3)
    1. [Iteration Goal, Driver Selection](#31-establish-iteration-goal-by-selecting-drivers)
    2. [Refine System Elements](#32-refine-system-elements)
    3. [Design Concepts that Satisfy the Selected Drivers](#33-select-one-or-more-design-concepts-that-satisfy-the-selected-drivers)
    4. [Architectural Elements, Responsibilities, and Interfaces](#34-instantiate-architectural-elements-allocate-responsibilities-and-define-interfaces)
    5. [Sketch Views and Record Design Decisions](#35-sketch-views-and-record-design-decisions)
    6. [Design Analysis, Goal Review, Design Purpose](#36-analysis-of-current-design-iteration-goal-review-and-achievement-of-design-purpose)


## Introduction

Attempting to organize and plan events with friends is always a hassle especially when no one knows when anyone else is available. Our new Social Calendar aims to make event planning infinitely easier by allowing you to see your friends’ public events and sending out invites to new events. Social Calendar provides a lightweight user-friendly package for all your planning needs.

![Social Calendar Screenshot](/Design/screenshot.png)

## Members

[Massimo Albanese](https://github.com/madlitch) 100616057

[Taimour Arshad](https://github.com/TaimourArshad1) 100748446

[Raza Naqvi](https://github.com/RazNaq123) 100754516 

[Waleed El Alawi](https://github.com/Waleed20210) 100764573

## Requirements

### Functional Requirements

Users must be able to:

- Create an account and log in
- Add friends 
- Add events to their calendar
- View their events in their calendar
- View their friend's events in the calendar, based on their visibility

### Non-Functional / Quality Requirements

The program must: 

- Be intuitive and easy to use (Usability)
- Must keep data securely (Security)
- Must be cross-platform for desktop applications (Compatibility)

## Use Cases, Quality Attributes, Constraints, and Concerns

### Use Cases


![Use Case Model](/sketches/use_case_model.png)

| Use Case  | Description  | 
| ------------- |-------------| 
| UC-1: Sign up/Login system |  Signup/Login page ask users to enter signup/login credentials.  |
| UC-2: Manage Users |  Account administrator will be able to add/remove users that are using the Calendar. |
| UC-3: View Events in Calendar |  Users will be able to view any upcoming events in their calendar |
| UC-4: Add Friends |  Users can send friend requests to other users or accept/decline friend requests from other users. |
| UC-5: Checks Friends’ Calendars |  Users can see their friend’s calendars but not the calendar of another user that is not their friend. |
| UC-6: Add Events |  Users can add events to their calendars  |
| UC-7: Multiple Views |  This feature will allow a user to choose how they want their calendar to be displayed (one day, one week, one year etc.) |
| UC-8: Collect User Data|  Administrators will collect user data such as number of accounts created, number of active accounts, number of events created etc. |

### Quality Attributes

| ID  | Quality Attribute  | Scenario | Associated Use Cases |
| ------------- |-------------| ------| ------| 
| QA-1 | Security  | Users need to create an account and login in order to access calendar features, so it can be known who uses the system at what time and prevents unauthorized users from accessing the system.| UC-1|
| QA-2 |Usability|Users can share calendars together so they can collaborate in projects. It would also allow them to set up meetings which all project members could see. | UC-5|
| QA-3 |Usability|Users can share and send their own personal calendars with their friends or other users. This will allow the users to visually compare their schedules and decide how to make events. | UC-4, UC-5 |
| QA-4 |Performance| The system will track the users’ data and how often they use some of the calendar system’s features. The administrator can determine if a feature needs to be tweaked or removed. | |

### Constraints

| ID  | Constraint  | 
| ------------- |-------------| 
| CON-1 |The system must support at least 1000 users simultaneously  |
| CON-2 |The calendar software must be coded in Python, JavaScript, HTML, and CSS|
| CON-3 |Calendar must allow users to access the next 100 years|

### Concerns

| ID  | Concerns  | 
| ------------- |-------------| 
| CRN-1| We would need to establish an overall initial system structure.|
| CRN-2 | Allocating work to the members of the development team. |


## ADD Iteration 1

### 1.1 Reviewing Inputs

| Category        | Details          |
| ------------- |-------------| 
|Design Purpose| This is a greenfield system with no prior architectural concerns or liabilities. The purpose is to produce a sufficiently detailed design to support the construction of the system. | 
| Constraints | All constraints discussed are included as drivers. | 
| Concerns | All concerns discussed are included as drivers. | 

| Primary Functional Requirements  | Reasoning  | 
| ------------- |-------------| 
| UC-1 |  Integral to the functionality of the product |
| UC-3 |  Integral to the functionality of the product |
| UC-4 |  Integral to the functionality of the product |
| UC-5 |  Integral to the functionality of the product |
| UC-6 |  Integral to the functionality of the product |

| Quality Attribute Scenario ID  | Importance to the Customer          | Difficulty of Implementation |
| ------------- |-------------| ---|
| QA-1| High| High|
|QA-2 | High| Medium|
|QA-3 | High| Medium|
|QA-4 | Low| Low|

### 1.2 Establish Iteration Goal by Selecting Drivers

To achieve the Iteration Goal CRN-1 of Establishing an Overall Initial System Structure, the selected drivers needed are as follows:
- QA-1: Security
- QA-4: Performance
- CON-1: The system must support at least 1000 users 
- CON-2: The calendar software must be coded in Python, JavaScript, HTML, CSS

### 1.3 Refine System Elements

As this is a greenfield system, the element to refine would be the entire social calendar system. Refinement will be performed through decomposition.

### 1.4 Select One or More Design Concepts that Satisfy the Selected Drivers

| Design Decisions and Location  | Rationale  |Discarded Alternatives | 
| ------------- |-------------| --------|
| Logically structure the client part of the system using the Rich Client Application reference architecture| The Rich Client Application (RCA) reference architecture supports the development of applications that are installed on the users’ PC. These applications support rich user interface capabilities that are needed for displaying the users’ calendars (UC-3), their friends’ calendars (UC-5), and multiple calendar views (UC-7). | **Rich Internet applications (RIA):** This reference architecture is geared towards the development of applications with a rich user interface that runs inside a web browser. This option was discarded because we want to have an application installed on the users’ computer for usability and convenience. **Web Application:** This reference architecture is oriented toward the development of applications that are accessed from a web browser. This reference architecture was discarded because it is too difficult to provide a user rich interface.|
|Logically structure the server part of the system using the Service Application reference architecture| This backend server would provide an API for the client application. No other alternatives were considered or discarded, as the architects were familiar with the reference architecture and considered it fully adequate to meet the requirements. | |
|Physically structure the application using the three-tier deployment |Since the system would have a client application, a backend server, and would need to store user and performance data (UC-1, UC-3, UC-4, UC-6, UC-8), a three-tier deployment is appropriate as a database server would be needed to store this information.| |
|Build the client application using the Electron framework| The Electron framework allows for the creation of desktop GUI applications using web technologies, providing all of the benefits of a Rich Internet Application and a Web Application, while being locally installed on a user’s machine.| |
|Build the user interface of the client application using web technologies (HTML/CSS/JS)|Building the user interface with HTML, CSS, and JavaScript is what all the developers are already familiar with (CON-2). | |
|Build the server part of the system using the FastAPI framework (Python) |Building the backend server system using the FastAPI framework would allow for many concurrent users as it is an asynchronous system (CON-1), and would leverage the existing experience and knowledge of the technology by the developers  (CON-2).| |

### 1.5 Instantiate Architectural Elements, Allocate Responsibilities, and Define Interfaces

It is too early to decide how we precisely want to define the functionalities and interfaces. We will go into further detail in the next iteration.

### 1.6 Sketch Views and Record Design Decisions

#### Architecture Model View

![Architecture Model View](/sketches/1.6.1_architecture_model_view.png)


| Element        | Responsibility           |
| ------------- |-------------| 
|Presentation CS|This layer is responsible for user interaction and use case control flow.| 
| Business Logic CS | This layer contains modules that perform business logic operations on the client side.| 
| Data CS | This layer is responsible for communicating with the server. | 
| Services SS | This layer contains modules that show services that are consumed by the clients | 
| Business Logic SS | This layer contains modules that perform business logic operations on the server side | 
| UI Modules | These modules render the user interface and receive user inputs.|
| UI Process Modules | These modules are responsible for control flow of all the system use cases (including navigation between screens).   | 
| Communication Module | These modules utilize the services provided by the application on the server side. | 
| Business Modules CS | Modules that implement business operations or they expose business functionality from the server side.  | 
| Business Entities CS | These entities make up the domain model. | 
| Service Interfaces | These modules expose services that are consumed by the clients | 
| Business Modules SS | These modules implement business operations.| 
| Business Entities SS | These entities make up the domain model.   | 
| DB Access Module | This module is responsible for persistence of business entities into the relational database. | 

#### Initial Deployment Diagram

![Initial Deployment Diagram](/sketches/1.6.2_initial_deployment_diagram.jpg)


### 1.7 Analysis of Current Design, Iteration Goal Review, and Achievement of Design Purpose

| Not Addressed        | Partially Addressed           | Completely Addressed | Design Decisions Made During Iteration |
| ------------- |-------------| ------------- |-------------| 
| | UC-1| |Selected reference architecture establishes the modules that will support this functionality.  |
| | UC-3| |Selected reference architecture establishes the modules that will support this functionality. |
| | UC-4| |Selected reference architecture establishes the modules that will support this functionality. |
| | UC-5| |Selected reference architecture establishes the modules that will support this functionality. |
| | UC-6| |Selected reference architecture establishes the modules that will support this functionality. |
| QA-2| | |No relevant decisions made.|
| QA-3| | |No relevant decisions made.|
| | QA-4| |Selected reference architecture establishes the modules that will support this functionality. |
| | CON-1| |Selected reference architecture establishes the modules that will support this functionality. Decisions regarding handling of concurrent access have not been made yet. |
| | |CON-2|The decided overall system structure leverages the development team’s prior experience and skills.|
|CON-3| | | No relevant decisions made.|
| | |CRN-1|Reference architecture and deployment pattern have been selected to address this concern. |
|CRN-2| | |No relevant decisions made. |

## ADD Iteration 2

### 2.1 Establish Iteration Goal by Selecting Drivers

Other than CRN-2, we will be considering following use cases as they are integral to the functionality of the product:
- UC-1
- UC-3
- UC-4
- UC-5
- UC-6

### 2.2 Refine System Elements

The elements to be refined in this iteration are the modules located in the different layers defined by the reference architectures we chose in the previous iteration: Rich Client Application and Service Application. As we chose a three-tier deployment, each component and associated modules must function together, otherwise the product would not be functional.

### 2.3 Select One or More Design Concepts that Satisfy the Selected Drivers

| Design Decisions and Location        | Rationale and Assumptions           |
| ------------- |-------------| 
| Create a Domain Model for the Application     | Before starting the decomposition, we must create an initial domain model for the system. There are no good alternatives  | 
| Identify Domain Objects that map to functional requirements      | Each element of the application needs to be encapsulated in a domain object block.     |   
| Decompose Domain Objects into general and specialized Components |  The domain objects would be complete sets of functionality, supported by smaller modules found within. Decomposition would be achieved through the specialization of the internal modules of the domain objects.   |
| Use SQLAlchemy | SQLAlchemy is a Python SQL toolkit and Object Relational Mapper. Other ORM frameworks were not considered as the development team was already familiar with SQLAlchemy.    |

### 2.4 Instantiate Architectural Elements, Allocate Responsibilities, and Define Interfaces

| Design Decisions and Location        | Rationale           |
| ------------- |-------------| 
| Create only an initial domain model |Entities that participate in the primary use cases need to be identified and modelled, however, only an initial domain model is created, to accelerate this phase of design.| 
|Map the system use cases to domain object|Identification of domain objects can be done by analyzing system’s use cases. To address CRN-2, domain objects are identified for all of the use cases, UC-1 to UC-6.| 
|Decompose the domain objects across the layers to identify layer-specific modules with an explicit interface |This will ensure that the modules who support all of the functionalities are identified. | 
| Associate frameworks with a module in the data layer |  The ORM mapping is found in the data access module in the data layer. The SQLAlchemy framework is associated with this module.| 

### 2.5 Sketch Views and Record Design Decisions

#### Domain Model

![Domain Model](/sketches/2.6.1_domain_modell.jpg)

#### Primary Use Case Modules

![Primary Use Case Modules](/sketches/2.6.2_primary_use_case_modules.jpg)

| Element        | Responsibility           |
| ------------- |-------------| 
|CalendarView| Displays current calendar and updates it when settings are changed or when events are added/removed.| 
| CalendarController | This element is responsible for providing the presentation layer information to display the current calendar. | 
| RequestManager | Responsible for communication with the server-side logic. | 
| RequestService | Responsible for providing a facade that takes requests from clients | 
| DomainEntities | Contains the entities from the domain model (server side). | 
| TopologyController|Contains business logic related to the topological information. | 
| EventController | Contains business logic related to management of events.|
| UserController | Contains user data information | 
| EventDataMapper | Responsible for persistence operations (CRUD) related to the events | 
| UserDataMapper | Responsible for persistence operations (CRUD) related to the users | 

### 2.6 Analysis of Current Design, Iteration Goal Review, and Achievement of Design Purpose

| Not Addressed        | Partially Addressed           | Completely Addressed | Design Decisions Made During Iteration |
| ------------- |-------------| ------------- |-------------| 
| | | UC-1|Modules across the layers and preliminary interfaces to support this use case have been identified. |
| | | UC-3|Modules across the layers and preliminary interfaces to support this use case have been identified. |
| | | UC-4|Modules across the layers and preliminary interfaces to support this use case have been identified. |
| | | UC-5|Modules across the layers and preliminary interfaces to support this use case have been identified. |
| | | UC-6|Modules across the layers and preliminary interfaces to support this use case have been identified. |
| | QA-2| |The elements that support the associated use case (UC-5) have been identified|
| | QA-3 | | The elements that support the associated use cases (UC-4, UC-5) have been identified |
| | QA-4| | No relevant decisions made.|
| |CON-1| |No relevant decisions made.|
| | |CON-2|No relevant decisions made. |
| |CON-3 | |No relevant decisions made. |
| | |CRN-1 |No relevant decisions made. |
| | |CRN-2 |Modules associated with all of the use cases have been identified and a work assignment matrix has been created (not shown).|

## ADD Iteration 3

### 3.1 Establish Iteration Goal by Selecting Drivers

For this iteration, the architect focuses on the QA-1 quality attribute scenario: Users need to create an account and login in order to access calendar features, so it can be known who uses the system at what time and prevents unauthorized users from accessing the system.

### 3.2 Refine System Elements

For this security scenario,  the elements that will be refined are the physical nodes that were identified during the first iteration:
- Adding a cross-cutting security layer of the Server Side System Architecture
    - Account creation module
    - Authentication module

### 3.3 Select One or More Design Concepts that Satisfy the Selected Drivers

| Design Decisions and Location        | Rationale and Assumptions          |
| ------------- |-------------| 
| Build Authentication Module based on the OAuth2 Specification with a first party implementation | OAuth2 is the industry-standard protocol for authorization, with a focus on web, desktop, and mobile devices, which works well for our use cases. The developers are also familiar with the technology. |
| Give the Security Layer direct access to the Data Layer | The interaction between these two layers would allow for quick authentication through direct access to the database, while keeping business logic and security logic separate|
| Store passwords using the hash + salt technique | This data storage technique would allow for data protection through not storing passwords as plaintext. The inclusion of a salt would guarantee that every password hash is unique.|

### 3.4 Instantiate Architectural Elements, Allocate Responsibilities, and Define Interfaces

| Design Decisions and Location        | Rationale            |
| ------------- |-------------| 
| Cross-Cutting Security Layer on Server Side System Architecture | This layer would allow for the account creation and authentication modules to communicate directly with any layer that requires authentication, while accessing the data layer directly for efficiency |
| Split security layer into separate account (password) creation and authentication modules| The authentication module would be used for almost endpoint, while the account creation module is used relatively seldomly |

### 3.5 Sketch Views and Record Design Decisions

![Modules](/sketches/3.1_modules.jpg)

### 3.6 Analysis of Current Design, Iteration Goal Review, and Achievement of Design Purpose

| Not Addressed        | Partially Addressed           | Completely Addressed | Design Decisions Made During Iteration |
| ------------- |-------------| ------------- |-------------| 
| | QA-2| |The elements that support the associated use case (UC-5) have been identified|
| | QA-3 | | The elements that support the associated use cases (UC-4, UC-5) have been identified |
| | QA-4| | No relevant decisions made.|
| |CON-1| |No relevant decisions made.|
| |CON-3 | |No relevant decisions made. |
| | |CRN-1 |No relevant decisions made. |
