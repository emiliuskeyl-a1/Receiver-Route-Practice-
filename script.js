document.getElementById("generate").addEventListener("click", async () => {
    try {
        const response = await fetch("/random_play");
        const data = await response.json();
        document.getElementById("output").innerText = data.playcall;
    } catch (error) {
        document.getElementById("output").innerText = "Fehler beim Laden!";
        console.error(error);
    }
});
