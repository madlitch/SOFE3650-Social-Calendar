let today=new Date();
let currentMonth=today.getMonth();
let currentYear=today.getFullYear();

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

monthAndYear=document.getElementById("month-and-year");
showCalendar(currentMonth, currentYear);

function next(){
    currentYear=(currentMonth===11)?currentYear+1:currentYear;
    currentMonth=(currentMonth+1)%12;
    showCalendar(currentMonth,currentYear);
}

function previous(){
    currentYear=(currentMonth===0)?currentYear-1:currentYear;
    currentMonth=(currentMonth===0)?11:currentMonth-1;
    showCalendar(currentMonth,currentYear);
}

function showCalendar(month, year){
    let firstDay=(new Date(year, month)).getDay();

    let tbl = document.getElementById("calendar-body");

    tbl.innerHTML="";

    monthAndYear.innerHTML=months[month]+" "+year;

    let date=1;
    let actualDate=0;
    for (let i=0;i<6;i++){
        let row=document.createElement("tr");
        let cell;
        let cellText;
        for (let j=0;j<7;j++){
            if (i===0&&j<firstDay){
                cell=document.createElement("td");
                cellText=document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }else if (date>daysInMonth(month, year)&&j===0){
                break;
            }else if (date>daysInMonth(month, year)){
                actualDate+=1;
                cell=document.createElement("td");
                cell.setAttribute("id", ""+currentYear+""+months[currentMonth]+""+(('00'+actualDate).slice(-2)));
                cellText=document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }else{
                actualDate+=1;
                cell=document.createElement("td");

                cell.setAttribute("id", ""+currentYear+""+months[currentMonth]+""+(('00'+actualDate).slice(-2)));
                cellText=document.createTextNode(date);
                if (date===today.getDate()&&currentMonth===today.getMonth()&&currentYear===today.getFullYear()){
                    cell.classList.add("bg-info");
                }
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }
            tbl.appendChild(row);
        }
    }
}

function daysInMonth(inMonth, inYear){
    return 32-new Date(inYear, inMonth, 32).getDate();
}

let modal = document.getElementById("eventModal");
let btn=document.getElementById("eventAdd");
let span=document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
};

span.onclick = function() {
    modal.style.display = "none";
};

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

let modal2 = document.getElementById("userModal");
let btn2=document.getElementById("userAdd");
let span2=document.getElementsByClassName("close2")[0];

btn2.onclick = function() {
    modal2.style.display = "block";
};

span2.onclick = function() {
    modal2.style.display = "none";
};

window.onclick = function(event) {
    if (event.target === modal2) {
        modal2.style.display = "none";
    }
};

function addFriend(){
    let list=document.getElementById("friend-group");
    let len=list.getElementsByTagName("li").length;
    let newF=document.createElement("li");
    newF.setAttribute("class","list-group-item");
    newF.setAttribute("id",""+(len+1));
    let friendText=document.createTextNode("Friend: "+(len+1));
    newF.appendChild(friendText);
    list.appendChild(newF);
}
function hideCal() {
    let y=document.getElementById("login-btn");
    let j=document.getElementById("loginScreen");
    let x = document.getElementById("hideIt");
    y.style.display="none";
    j.style.display="none";
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}
function loginSo() {
    let u=document.getElementById("login-form");
    let y=document.getElementById("login-btn");
    let j=document.getElementById("loginScreen");
    let x = document.getElementById("hideIt");
    let p=document.getElementById("error1");
    x.style.display = "none";
    y.style.display ="block";
    j.style.display="block";
    p.style.display="none";
    u.reset();
}
function noLogin(){
    let y=document.getElementById("error1");
    y.style.display="block";
}
