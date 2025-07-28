document.getElementById("checkBtn").addEventListener("click", function () {
  const packaging = document.getElementById("packaging").value;
  const transport = document.getElementById("transport").value;

  const certCheckboxes = document.querySelectorAll('input[name="certs"]:checked');
  const certifications = Array.from(certCheckboxes).map(cb => cb.value);

  fetch("http://localhost:5000/score", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      packaging: packaging,
      transport: transport,
      certifications: certifications
    })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("scoreBox").innerText = "Eco Score: " + data.eco_score;
    })
    .catch(err => {
      document.getElementById("scoreBox").innerText = "Error: " + err.message;
    });
});