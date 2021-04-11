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