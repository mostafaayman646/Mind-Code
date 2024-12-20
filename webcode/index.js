// JavaScript to enhance interactivity on the webpage

// Smooth scrolling for navigation links
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const targetId = event.target.getAttribute('href').substring(1);
        document.getElementById(targetId).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Plot graph as soon as the page loads
document.addEventListener('DOMContentLoaded', () => {
    const time = [0, 1, 2, 3, 4, 5];
    const concentration = [10, 20, 15, 25, 30, 40];

    const trace = {
        x: time,
        y: concentration,
        mode: 'lines+markers',
        type: 'scatter',
        name: 'Tau Protein Concentration'
    };

    const layout = {
        title: 'Tau Protein Concentration Over Time',
        xaxis: { title: 'Time (s)' },
        yaxis: { title: 'Concentration (mol/m^3)' }
    };

    



});


