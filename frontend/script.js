function renderUserGreeting() {
  const parameters = new URLSearchParams(window.location.search);
  const username = parameters.get("username") || "visitor";
  const greeting = document.getElementById("greeting");

  greeting.innerHTML = `<h1>Welcome, ${username}!</h1>`;
}

window.onload = function () {
  initializeAnalyticsEngine();
  renderUserGreeting();
};