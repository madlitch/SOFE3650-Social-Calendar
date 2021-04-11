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
    for (let i=0;i<6;i++){
        let row=document.createElement("tr");

        for (let j=0;j<7;j++){
            if (i===0&&j<firstDay){
                cell=document.createElement("td");
                cellText=document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }else if (date>daysInMonth(month, year)){
                break;
            }else{
                cell=document.createElement("td");
                cellText=document.createTextNode(date);
                if (date===today.getDate()){
                    cell.classList.add("bg-info");
                }
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }
            tbl.appendChild(row);
        }
    }
    //console.log(tbl.children[x].children[y].innerHTML) x is the week, y is the day
}

function daysInMonth(inMonth, inYear){
    return 32-new Date(inYear, inMonth, 32).getDate();
}