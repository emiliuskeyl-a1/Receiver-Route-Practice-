document.getElementById("btn").addEventListener("click", async () => {
  const res = await fetch("https://footballrouteapi.onrender.com/random_play");
  const data = await res.json();
  document.getElementById("output").textContent = JSON.stringify(data, null, 2);
});
