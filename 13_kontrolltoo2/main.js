const app = new GeenidApp();

app.lisaGeen("A", true, false);
app.lisaGeen("A", false, false);
app.lisaGeen("B", true, true);

function lisaGeen() {
    const nimetus = document.getElementById("uusNimetus").value.trim();
    if (!nimetus) return alert("Sisesta nimetus");
    app.lisaGeen(
        nimetus,
        document.getElementById("a1").value === "1",
        document.getElementById("a2").value === "1"
    );
    document.getElementById("uusNimetus").value = "";
    kuvaNimekiri();
}

function kuvaNimekiri() {
    const q = document.getElementById("otsing").value;
    const geenid = app.otsiGeene(q);
    const ul = document.getElementById("geeninimekiri");
    ul.innerHTML = "";

    geenid.forEach(geen => {
        const valitudIndex = app.valitudVanemad.indexOf(geen);
        const li = document.createElement("li");
        li.textContent = `${geen.nimetus} (${geen.alleel1.positiivne ? "+" : "-"}/${geen.alleel2.positiivne ? "+" : "-"})`;

        if (valitudIndex !== -1) {
            li.textContent += ` ← Vanem ${valitudIndex + 1}`;
        }

        li.onclick = () => {
            app.valiVanem(geen);
            kuvaNimekiri();
            kuvavanemad();
        };
        ul.appendChild(li);
    });
}

function kuvavanemad() {
    const v = app.valitudVanemad;
    const tekst = v.map((g, i) =>
        `Vanem ${i + 1}: ${g.nimetus} (${g.alleel1.positiivne ? "+" : "-"}/${g.alleel2.positiivne ? "+" : "-"})`
    ).join("  ×  ");
    document.getElementById("valituInfo").textContent = "Valitud vanemad: " + (tekst || "-");
}

function kombineeri() {
    try {
        app.kombineeri();
        kuvaNimekiri();
        kuvavanemad();
        kuvaJärglased();
    } catch (e) {
        alert(e.message);
    }
}

function kuvaJärglased() {
    const ul = document.getElementById("järglased");
    ul.innerHTML = "";
    app.järglased.forEach((laps, index) => {
        const li = document.createElement("li");
        li.textContent = `${laps.nimetus} (${laps.alleel1.positiivne ? "+" : "-"}/${laps.alleel2.positiivne ? "+" : "-"}) — ${laps.onPositiivne() ? "positiivne" : "negatiivne"}`;
        const btn = document.createElement("button");
        btn.textContent = "Kustuta";
        btn.onclick = () => {
            app.kustutaJärglane(index);
            kuvaJärglased();
        };
        li.appendChild(btn);
        ul.appendChild(li);
    });
}

kuvaNimekiri();