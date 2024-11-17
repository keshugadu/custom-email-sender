async function fetchAnalytics() {
    const response = await fetch('/analytics');
    const data = await response.json();
    document.getElementById('total-sent').textContent = data.total_sent;
}

setInterval(fetchAnalytics, 5000); // Refresh analytics every 5 seconds