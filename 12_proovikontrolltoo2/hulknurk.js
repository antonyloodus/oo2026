class Hulknurk {
    constructor(xid, yid, hdistance, hcount) {
        this.xid = xid;
        this.yid = yid;
        this.hdistance = hdistance;
        this.hcount = hcount;
    }

    leiaPindala() {
        return 0.5 * this.hcount * (this.hdistance ** 2) * Math.sin(2 * Math.PI / this.hcount);
    }

    draw(ctx) {
        if (this.hcount < 3) return;
        ctx.beginPath();
        for (let i = 0; i < this.hcount; i++) {
            let angle = (2 * Math.PI / this.hcount) * i;
            let px = this.xid + this.hdistance * Math.cos(angle);
            let py = this.yid + this.hdistance * Math.sin(angle);
            if (i === 0) {
                ctx.moveTo(px, py);
            } else {
                ctx.lineTo(px, py);
            }
        }
        ctx.closePath();
        ctx.stroke();
    }

    getPoints() {
    let points = [];
    for (let i = 0; i < this.hcount; i++) {
        let angle = (2 * Math.PI / this.hcount) * i;
        let px = this.xid + this.hdistance * Math.cos(angle);
        let py = this.yid + this.hdistance * Math.sin(angle);
        points.push({ x: px, y: py });
    }
    return points;
    }
}

const slider = document.getElementById("sides");
const text = document.getElementById("sidesCount");
const pindalaSpan = document.getElementById("pindala");

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const hulknurk1 = new Hulknurk(200, 200, 150, parseInt(slider.value));

function update() {
    hulknurk1.hcount = parseInt(slider.value);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    hulknurk1.draw(ctx);
    text.textContent = slider.value;
    pindalaSpan.textContent = hulknurk1.leiaPindala().toFixed(2);

    const coordsDiv = document.getElementById("coords");
    const points = hulknurk1.getPoints();
    coordsDiv.innerHTML = points
        .map((p, i) => `<p>Tipp ${i + 1}: (${p.x.toFixed(1)}, ${p.y.toFixed(1)})</p>`)
        .join("");
}

slider.addEventListener("input", update);
update();