async function sendInput() {
    const input = document.getElementById("input").value;

    await fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            input: input
        })
    });
}
