const $ = require('jquery');


'use strict';


$(document).ready(function() {
    let friendModal = document.getElementById('friend-modal');
    let eventModal = document.getElementById('event-modal');
    let registerModal = document.getElementById('register-modal');

    $('#current-user-btn').on('click', async () => {
        getCurrentUser()
    });

    $('#login-btn').on('click', async () => {
        let form = document.getElementById('login-form');
        loginUser(form);
    });

    $('#logout-btn').on('click', async () => {
        logout();
    });

    $('#previous').on('click', async () => {
        previous();
    });

    $('#next').on('click', async () => {
        next();
    });

    $('#friend-btn').on('click', async () => {
        friendModal.style.display = 'block';
    });

    $('#close-friend-modal-btn').on('click', async () =>{
        friendModal.style.display = 'none';
    });

    $('#add-friend-btn').on('click', async () => {
        let form = document.getElementById('add-friend-form');
        addFriend(form);
    });

    $('#events-btn').on('click', async () => {
        refreshEvents();
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
    });

    $('#new-event-btn').on('click', async () =>{
        eventModal.style.display = 'block';
    });

    $('#close-event-modal-btn').on('click', async () =>{
        eventModal.style.display = 'none';
    });

    $('#create-user-btn').on('click', async () =>{
        registerModal.style.display = 'block';
    });

    $('#close-register-modal-btn').on('click', async () =>{
        registerModal.style.display = 'none';
    });

});

