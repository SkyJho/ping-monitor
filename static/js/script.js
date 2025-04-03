async function adicionarSite() {
    const urlInput = document.getElementById("urlInput").value;
    if (!urlInput) {
        alert("Digite uma URL válida.");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/adicionar_site", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ urls: [urlInput] })
    });

    if (response.ok) {
        atualizarLista();
    } else {
        alert("Erro ao adicionar site.");
    }
}

async function atualizarLista() {
    const response = await fetch("http://127.0.0.1:8000/sites");
    const data = await response.json();
    
    const lista = document.getElementById("listaSites");
    lista.innerHTML = "";

    for (const [url, status] of Object.entries(data.sites)) {
        const li = document.createElement("li");
        li.textContent = `${url} - ${status}`;
        lista.appendChild(li);
    }
}

async function atualizarStatus() {
    try {
        let response = await fetch("/status");
        let sites = await response.json();
        
        let tabela = document.getElementById("statusTabela");
        tabela.innerHTML = "<tr><th>Site</th><th>Status</th><th>Caiu em</th><th>Voltou em</th></tr>";

        for (let site in sites) {
            let status = sites[site].online ? "🟢 Online" : "🔴 Offline";
            let caiuEm = sites[site].caiu_em || "-";
            let voltouEm = sites[site].voltou_em || "-";

            let row = `<tr>
                <td>${site}</td>
                <td>${status}</td>
                <td>${caiuEm}</td>
                <td>${voltouEm}</td>
            </tr>`;
            
            tabela.innerHTML += row;
        }
    } catch (error) {
        console.error("Erro ao buscar status dos sites:", error);
    }
}

// Atualiza a cada 5 segundos
setInterval(atualizarStatus, 5000);

setInterval(atualizarLista, 5000); // Atualiza a lista a cada 5 segundos
