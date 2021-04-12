let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();

let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

let monthAndYear = document.getElementById('month-and-year');

function next() {
    currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
    currentMonth = (currentMonth + 1) % 12;
    showCalendar(currentMonth, currentYear);
}

function previous() {
    currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
    currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
    showCalendar(currentMonth, currentYear);
}

function showCalendar(month, year) {
    const firstDay = (new Date(year, month)).getDay();

    const tbl = document.getElementById('calendar-body');

    tbl.innerHTML = '';

    monthAndYear.innerHTML = months[month] + " " + year;

    let date = 1;
    let actualDate = 0;
    for (let i = 0; i < 6; i++) {
        const row = document.createElement('tr');
        let cell;
        let cellText;
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                cell = document.createElement('td');
                cellText = document.createTextNode('');
                cell.appendChild(cellText);
                row.appendChild(cell);
            } else if (date > daysInMonth(month, year) && j === 0) {
                break;
            } else if (date > daysInMonth(month, year)) {
                actualDate += 1;
                cell = document.createElement('td');
                cell.setAttribute('id', `${currentYear}${months[currentMonth]}${(`00${actualDate}`).slice(-2)}`);
                cellText = document.createTextNode('');
                cell.appendChild(cellText);
                row.appendChild(cell);
            } else {
                actualDate += 1;
                cell = document.createElement('td');

                cell.setAttribute('id', `${currentYear}${months[currentMonth]}${(`00${actualDate}`).slice(-2)}`);
                cellText = document.createTextNode(date);
                if (date === today.getDate() && currentMonth === today.getMonth() && currentYear === today.getFullYear()) {
                    cell.classList.add('bg-info');
                }
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }
            tbl.appendChild(row);
        }
    }
}

function daysInMonth(inMonth, inYear) {
    return 32 - new Date(inYear, inMonth, 32).getDate();
}

function listFriend(username, name, id) {
    const list = document.getElementById('friend-group');
    const len = list.getElementsByTagName('li').length;
    const newF = document.createElement('li');
    newF.setAttribute('class', 'list-group-item');
    newF.setAttribute('id', `${len + 1}`);
    console.log(id);
    const friendText = document.createTextNode(name + " - " + username);
    newF.appendChild(friendText);
    list.appendChild(newF);
}

function login() {
    console.log('hello');
    const y = document.getElementById('login-btn');
    const j = document.getElementById('loginScreen');
    const x = document.getElementById('hideIt');
    y.style.display = 'none';
    j.style.display = 'none';
    if (x.style.display === 'block') {
        x.style.display = 'none';
    } else {
        x.style.display = 'block';
    }
}

function logout() {
    document.getElementById("friend-group").innerHTML = "";
    const u = document.getElementById('login-form');
    const y = document.getElementById('login-btn');
    const j = document.getElementById('loginScreen');
    const x = document.getElementById('hideIt');
    x.style.display = 'none';
    y.style.display = 'block';
    j.style.display = 'block';
    u.reset();
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function showMessage(isErr, message) {
    const box = document.getElementById('message-box');
    const text = document.getElementById('message');
    text.innerText = message.charAt(0).toUpperCase() + message.slice(1);
    if (isErr === true) {
        text.style.backgroundColor = "red";
    } else {
        text.style.backgroundColor = "green";
    }
    box.style.bottom = '10px';
    await sleep(3000);
    box.style.bottom = '-100px';
}

