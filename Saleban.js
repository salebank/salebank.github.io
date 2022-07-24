const daysEl = document.getElementById('days');
const hoursEl = document.getElementById('hours');
const minsEl = document.getElementById('mins');
const SecondsEl = document.getElementById('Seconds');

const BirthYearDate = '29 June 2023';


function countdown() {
    const birthdayDate = new Date(BirthYearDate);
    const currentDate = new Date();
    const totalSeconds = (birthdayDate - currentDate) / 1000;

    const days = Math.floor(totalSeconds / 3600 / 24);
    const hours = Math.floor(totalSeconds / 3600) % 24;
    const mins = Math.floor(totalSeconds / 60) % 60;
    const Seconds = Math.floor(totalSeconds) % 60;


    //console.log(days, hours, mins, Seconds)
    

    
 
    daysEl.innerHTML = days;
    hoursEl.innerHTML = hours;
    minsEl.innerHTML = mins;
    SecondsEl.innerHTML = Seconds; 


    
}


function formatTime(time) {
    
}




//initial.call
countdown();

setInterval(countdown, 1000);
