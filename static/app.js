document.getElementById("wordsearch-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const matrix = document.getElementById("matrix").value.split("\n");
    const words = document.getElementById("words").value.split(",");
    const response = await fetch("/solve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ matrix, words }),
    });
    const results = await response.json();
    document.getElementById("results").innerHTML = `
        <p>${results.message}</p>
    `;
});
