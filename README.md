# **SOFE3650 Project - Social Calendar**

This project is based on the SOFE2720 Final Project, found here: https://github.com/SOFE2720/Social-Calendar-Group-12

The old README can be found [here](https://github.com/madlitch/SOFE3650-Project/blob/main/README_OLD.md)

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

![Social Calendar Screenshot](/Requirements/Requirements.png)


### Non-Functional / Quality Requirements

The program must: 

- Be intuitive and easy to use (Usability)
- Must keep data securely (Security)
- Must be cross-platform for desktop applications (Compatibility)

### Progress Report, Use Case Model, Quality Attributes, and System Constraints

Our progress report is available [here](https://github.com/madlitch/SOFE3650-Project/blob/main/Sofe%20Design%20Progress%20Report.pdf)

### ADD Iteration 1

Our ADD Iteration 1 is available [here](https://github.com/madlitch/SOFE3650-Project/blob/c57965bdebc78c8bb19143a94a3d55c7eba8778d/ADD%20Iteration%201.pdf)

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

 ** SKETCHES **

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



