# **SOFE3650 Project - Social Calendar**

## Introduction

This project is based on the SOFE2720 Final Project, found here: https://github.com/SOFE2720/Social-Calendar-Group-12

The old README can be found ![here](/README_OLD.md)





## Introduction

Attempting to organize and plan events with friends is always a hassle especially when no one knows when anyone else is available. Our new Social Calendar aims to make event planning infinitely easier by allowing you to see your friends’ public events and sending out invites to new events. Social Calendar provides a lightweight user-friendly package for all your planning needs.

![Social Calendar Screenshot](/Design/screenshot.png)

## Description

Social Calendar is a full-stack deployment of a Social Calendar desktop application and backend server.

Frontend stack: Electron (HTML, CSS, JS)

Backend stack: Python (FastAPI), PostgreSQL

## How to Replicate this Project
Requirements:
1. Python 3
2. Node
3. Npm
4. PostgreSQL | **Make sure you write down your master password!!**

Installation Steps:

1. Clone this repository.
2. Open **backend/constants.py** and fill in the required information (User, Password, Port, Database.)
3. Open a terminal window in this repository's folder.
4. Navigate to the 'backend' folder.
5. Install python requirements via pip `$ pip install -r requirements.txt`
6. Once that's done, start the server `$ uvicorn server:app --reload`
7. Navigate to the 'frontend' folder
8. Install npm requirements `$ npm install`
9. Start the application `$ npm start`


