let chronometer = document.getElementById("chronometer");
let startButton = document.getElementById('startButton');
let stopButton = document.getElementById("stopButton");
let date, time;
let sButtonState = 0;
let pauseTime = 0;

// Event listener to check the button to start an activity
startButton.addEventListener("click", function () {
    //the state of the button is 0 if it's running or just initialized
    if (sButtonState === 0) {
        startButton.textContent = "Pausar";
        startButton.classList.remove("btn-info", "btn-warning", "btn-success");
        startButton.classList.add("btn-success");
        sButtonState = 1;
        date = new Date;
        startChronometer();
    } else {
        startButton.textContent = "Reanudar";
        startButton.classList.remove("btn-info", "btn-warning", "btn-success");
        startButton.classList.add("btn-warning");
        sButtonState = 0;
        pauseTime = (new Date) - date;
        pauseChronometer();
    }
});

// Event listener to check the button to stop an activity
stopButton.addEventListener("click", function () {
    startButton.textContent = "Iniciar";
    startButton.classList.remove("btn-info", "btn-warning", "btn-success");
    startButton.classList.add("btn-primary");
    restartChronometer();
    pauseChronometer();
});

//Function to update the chronometer, it uses a Date object to ensure there is no desync
function runChronometer() {
    let currentDate = new Date;
    let timeElapsed = currentDate - date + pauseTime;
    let seconds = Math.floor(timeElapsed / 1000) % 60;
    let minutes = Math.floor(timeElapsed / (1000 * 60)) % 60;
    let hours = Math.floor(timeElapsed / (1000 * 60 * 60));
    let secondsString = checkZero(seconds);
    let minutesString = checkZero(minutes);
    chronometer.innerText = hours + ":" + minutesString + ":" + secondsString;
}

//starts the chronometer
function startChronometer() {
    time = setInterval(runChronometer, 100);
}

//pauses the Chronometer
function pauseChronometer() {
    clearInterval(time);
}

//restarts the chronometer to the initial state
function restartChronometer() {
    clearInterval(time);
    chronometer.innerText = "0:00:00";
    date = new Date;
    sButtonState = 0;
    pauseTime = 0;
}

//adds a 0 if number is just a digit (for formatting purposes)
function checkZero(number) {
    if (number < 10) {
        return "0" + number;
    }
    return number;
}