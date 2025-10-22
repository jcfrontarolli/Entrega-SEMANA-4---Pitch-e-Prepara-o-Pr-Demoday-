async function fetchData() {
  const r = await fetch('/api/sensordata');
  const d = await r.json();
  ["temperature","humidity","ph","gas"].forEach(k => {
    document.getElementById(k).textContent = d[k] ?? "—";
  });
  const ul = document.getElementById('alerts');
  ul.innerHTML = "";
  (d.alerts || []).forEach(a => {
    const li = document.createElement('li'); li.textContent = a; ul.appendChild(li);
  });
  document.getElementById('updated').textContent = "Atualizado: " + new Date().toLocaleString();
}
fetchData();
setInterval(fetchData, 5000);
document.getElementById('clear').onclick = async () => {
  await fetch('/api/clearalerts', { method: 'POST' });
  fetchData();
};