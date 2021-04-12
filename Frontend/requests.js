
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

function stringifyForm(data) {
    return JSON.stringify(Object.fromEntries(data.entries()));
}

// -------------------- User Functions --------------------

function loginUser(form) {
    let data = new FormData(form);
    httpPost(url, "/token", false, data, async function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
        if (result.status === 200) {
            token = response["access_token"];
            getCurrentUser();
            getFriends();
            login();
            await showMessage(false, "Successful Login");
        } else {
            if (typeof response.detail === 'object') {
                await showMessage(true, response.detail[0].msg);
            } else {
                await showMessage(true, response.detail);
            }
        }
    });
}

function createUser(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/users/create", false, stringifyForm(data), async function (result) {
        let response = JSON.parse(result.response);
        if (result.status === 200) {
            await showMessage(false, "Success!");
        } else {
            await showMessage(true, response.detail);
        }
    });
}

function getCurrentUser() {
    httpGet(url, "/v1/users/me", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
        document.getElementById('current-user-name').innerText = response.first_name + " " + response.last_name;
        document.getElementById('current-user-username').innerText = response.username;
    });
}

// -------------------- Friend Functions --------------------

function getFriends() {
    httpGet(url, "/v1/friends", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response);
        response.forEach(friend => {
            listFriend(friend.username, friend.first_name + " " + friend.last_name, friend.id);
        });
    });
}

function addFriend(form) {
    let data = new FormData(form);
    httpPost(url, "/v1/friends/create", true, stringifyForm(data), async function (result) {
        let response = JSON.parse(result.response);
        if (result.status === 200) {
            await showMessage(false, "Success!");
        } else {
            await showMessage(true, response.detail);
        }
    });
}

// -------------------- Event Functions --------------------

function getPublicEvents() {
    httpGet(url, "/v1/events/public", true,function (result) {
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

function getPrivateEvents() {
    httpGet(url, "/v1/events/private", true,function (result) {
        let response = JSON.parse(result.response);
        console.log(response)
    });
}

function createEvent(form) {
    let data = new FormData(form);
    let date = new Date(data.get('time').toString());
    data.set('time', date.toISOString());
    httpPost(url, "/v1/events/create", true, stringifyForm(data), async function (result) {
        let response = JSON.parse(result.response);
        if (result.status === 200) {
            await showMessage(false, "Success!");
        } else {
            await showMessage(true, response.detail);
        }
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

// -------------------- Teapot Function :) ------------------

function getTeapot() {
    httpGet(url, "/v1/teapot",false, function (result){
       let response = JSON.parse(result.response);
       console.log(response.detail);
       document.getElementById("teapot-btn").innerHTML=(response.detail);
    });
}
