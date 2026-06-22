let winChart = null;

// Pull the live team pool from whatever the server actually rendered into
// the first dropdown — this can never drift out of sync with ratings.csv.
function getTeamPool() {
  const firstSelect = document.querySelector('.team-select');
  return Array.from(firstSelect.options)
    .map(opt => opt.value)
    .filter(v => v !== '');
}

function randomizeBracket() {
  const pool = [...getTeamPool()].sort(() => Math.random() - 0.5);
  document.querySelectorAll('.team-select').forEach((sel, i) => {
    sel.value = pool[i] ?? '';
  });
}

function runSimulation() {
  const selects = document.querySelectorAll('.team-select');
  const bracket = [];

  for (let i = 0; i < selects.length; i++) {
    const val = selects[i].value;
    if (!val) {
      alert('Please select a team for all 32 slots.');
      return;
    }
    bracket.push(val);
  }

  const unique = new Set(bracket);
  if (unique.size !== 32) {
    alert('Each team must appear exactly once. Please check for duplicates.');
    return;
  }

  const btn = document.getElementById('simulate-btn');
  btn.textContent = '⏳ Simulating...';
  btn.disabled = true;

  fetch('/simulate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ bracket })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        alert('Error: ' + data.error);
        btn.textContent = '▶ Run Simulation';
        btn.disabled = false;
        return;
      }
      displayResults(data);
      btn.textContent = '▶ Run Simulation';
      btn.disabled = false;
    })
    .catch(err => {
      alert('Something went wrong: ' + err);
      btn.textContent = '▶ Run Simulation';
      btn.disabled = false;
    });
}

function displayResults(data) {
  const teams = Object.keys(data).sort((a, b) => data[b].W - data[a].W);

  const resultsSection = document.getElementById('results-section');
  resultsSection.classList.add('visible');
  resultsSection.scrollIntoView({ behavior: 'smooth' });

  // Champion card
  const top = teams[0];
  document.getElementById('champion-name').textContent = top;
  document.getElementById('champion-odds').textContent = (data[top].W * 100).toFixed(1) + '%';

  // Chart
  const ctx = document.getElementById('winChart').getContext('2d');
  const winProbs = teams.map(t => (data[t].W * 100).toFixed(1));
  const colors = teams.map((_, i) => `hsl(${45 - i * 1.1}, 85%, ${58 - i * 0.8}%)`);

  if (winChart) winChart.destroy();

  winChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: teams,
      datasets: [{
        label: 'Win Probability (%)',
        data: winProbs,
        backgroundColor: colors,
        borderRadius: 4,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => `${ctx.parsed.y}% chance of winning` }
        }
      },
      scales: {
        x: {
          ticks: { color: '#a39c8c', maxRotation: 45 },
          grid: { color: '#2b2620' }
        },
        y: {
          ticks: { color: '#a39c8c', callback: val => val + '%' },
          grid: { color: '#2b2620' }
        }
      }
    }
  });

  // Table
  const tbody = document.getElementById('results-body');
  tbody.innerHTML = '';

  teams.forEach(team => {
    const d = data[team];
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${team}</td>
      <td>${(d.R16 * 100).toFixed(1)}%</td>
      <td>${(d.QF * 100).toFixed(1)}%</td>
      <td>${(d.SF * 100).toFixed(1)}%</td>
      <td>${(d.F * 100).toFixed(1)}%</td>
      <td><strong>${(d.W * 100).toFixed(1)}%</strong></td>
    `;
    tbody.appendChild(row);
  });
}