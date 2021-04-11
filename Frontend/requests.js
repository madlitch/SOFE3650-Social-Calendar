
const url = 'http://127.0.0.1:8000';
let token;

/* httpPost & httpGet
url: localhost constant
endpoint: end of url
locked: if the endpoint needs authorization (user has to be logged in, locked endpoints have the padlock on the right in the
    fastapi docs(http://127.0.0.1:8000/docs#/))
callback: function to be executed after the request is performed
 */

function httpGet(url, endpoint, locked, callback) {
    let http = new XMLHttpRequest();
    http.open( "GET", url + endpoint, true );
    if (locked === true) {
        http.setRequestHeader("Authorization", 'Bearer ' + token);
    }
    http.send( null );
    http.onload = function () {
        callback(http);
    };
}

function httpPost(url, endpoint, locked, data, callback) {
    let http = new XMLHttpRequest();
    http.open( "POST", url + endpoint, true );
    if (locked === true) {
        http.setRequestHeader("Authorization", 'Bearer ' + token);
    }
    http.send(data);
    http.onload = function () {
        callback(http);
    };
}

/* stringifyForm
turns form data into api url friendly string
 */

function stringifyForm(data) {
    return JSON.stringify(Object.fromEntries(data.entries()));
}

// -------------------- User Functions --------------------

function loginUser(form) {
    let data = new FormData(form);
    httpPost(url, "/token", false, data, function (result) {
        let response = JSON.parse(result.response);
        if (result.status === 200) {
            token = response["access_token"];
            console.log(result.status);
        }
    });
}

function createUser(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/users/create", false, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

function getCurrentUser() {
    httpGet(url, "/v1/users/me", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response)
    });
}

// -------------------- Friend Functions --------------------

function getFriends() {
    httpGet(url, "/v1/friends", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response)
    });
}

function addFriend(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/friends/create", false, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

function updateFriendRelationship(form) { // This "form" should not be visible to the user
    let data = new FormData(form);
    httpPost(url, "/v1/friends/update", false, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

// -------------------- Event Functions --------------------

function getUsersEvents() {
    httpGet(url, "/v1/events", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response)
    });
}

function getFriendsEvents() {
    httpGet(url, "/v1/events/friends", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response)
    });
}

function createEvent(form) {
    let data = new FormData(form);
    let date = new Date(data.get('time').toString());
    data.set('time', date.toISOString());
    console.log(stringifyForm(data));
    httpPost(url, "/v1/events/create", true, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

function joinEvent(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/events/join", true, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

function updateEventUsers(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/events/update/users", true, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

function updateEventRelationship(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/events/update/relationship", true, stringifyForm(data), function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
    });
}

// -------------------- Teapot Function :) ------------------

function getTeapot() {
    httpGet(url, "/v1/teapot",false, function (result){
       let response = JSON.parse(result.response);
       console.log(response.detail);
       document.getElementById("teapot-btn").innerHTML=(response.detail);
    });
}