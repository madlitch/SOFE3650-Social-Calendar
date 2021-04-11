const $ = require('jquery');


'use strict';


$(document).ready(function() {
    $('#current-user-btn').on('click', async () => {
        getCurrentUser()
    });

    $('#login-btn').on('click', async () => {
        let form = document.getElementById('login-form');
        loginUser(form);
    });

    $('#friends-btn').on('click', async () => {
        getFriends()
    });

    $('#add-friend-btn').on('click', async () => {
        let form = document.getElementById('new-user-form');
        addFriend(form);
    });

    $('#events-btn').on('click', async () => {
        getUsersEvents()
    });

    $('#new-user-btn').on('click', async () => {
        let form = document.getElementById('new-user-form');
        createUser(form);
    });

    $('#teapot-btn').on('click',async()=>{
       getTeapot()
    });

    $('#add-event-btn').on('click', async () =>{
        let form = document.getElementById('add-event-form');
        createEvent(form);
    })
});

