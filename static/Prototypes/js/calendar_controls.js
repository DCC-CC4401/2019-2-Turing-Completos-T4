document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['timeGrid', 'bootstrap', 'dayGrid'],
        defaultView: 'timeGridWeek',
        themeSystem: 'bootstrap',
        allDaySlot: false,
        nowIndicator: true,
        locale: 'es',
        header: false,
        firstDay: 1,
        columnHeaderFormat: {weekday: 'long'},
        slotLabelFormat: {
            hour: '2-digit',
            minute: '2-digit'
        }
    });
    calendar.render();
    let initialDate = calendar.getDate();
    changeDate(initialDate);


    let prevWeek = document.getElementById("prevWeek");
    let nextWeek = document.getElementById("nextWeek");
    let prevMonth = document.getElementById("prevMonth");
    let nextMonth = document.getElementById("nextMonth");

    prevWeek.addEventListener("click", function () {
        calendar.prev();
        changeDate(calendar.getDate())
    });
    nextWeek.addEventListener("click", function () {
        calendar.next();
        changeDate(calendar.getDate())
    });
    prevMonth.addEventListener("click", function () {
        calendar.prev();
        calendar.prev();
        calendar.prev();
        calendar.prev();
        changeDate(calendar.getDate())
    });
    nextMonth.addEventListener("click", function () {
        calendar.next();
        calendar.next();
        calendar.next();
        calendar.next();
        changeDate(calendar.getDate())
    });
});

function changeDate(Date) {
    let options = {weekday: 'long', month: 'long', day: 'numeric', year: 'numeric', formatMatcher: 'basic'};
    document.getElementById("week").innerText = "Semana del " + Date.toLocaleDateString("es-ES", options);
}


