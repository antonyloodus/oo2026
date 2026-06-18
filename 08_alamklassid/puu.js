"use strict";
class Puuosa {
}
class Leht extends Puuosa {
    varv;
    constructor(varv = "green") {
        super();
        this.varv = varv;
    }
    arv() { return 1; }
    joonista(g, x, y, nurk, pikkus) {
        g.fillStyle = this.varv;
        g.beginPath();
        g.arc(x, y, 4, 0, 2 * Math.PI);
        g.fill();
    }
}
class Oks extends Puuosa {
    suhtelineNurk;
    pikkustegur;
    lapsed = [];
    constructor(suhtelineNurk = 0, pikkustegur = 0.75) {
        super();
        this.suhtelineNurk = suhtelineNurk;
        this.pikkustegur = pikkustegur;
    }
    lisa(osa) {
        this.lapsed.push(osa);
    }
    getSuhtelineNurk() { return this.suhtelineNurk; }
    arv() {
        let n = 1;
        for (let laps of this.lapsed) {
            n += laps.arv();
        }
        return n;
    }
    joonista(g, x, y, nurk, pikkus) {
        const x2 = x + Math.cos(nurk) * pikkus;
        const y2 = y - Math.sin(nurk) * pikkus;
        g.strokeStyle = "saddlebrown";
        g.lineWidth = Math.max(1, pikkus / 12);
        g.beginPath();
        g.moveTo(x, y);
        g.lineTo(x2, y2);
        g.stroke();
        for (let laps of this.lapsed) {
            const lapseNurk = nurk + (laps instanceof Oks ? laps.getSuhtelineNurk() : 0);
            laps.joonista(g, x2, y2, lapseNurk, pikkus * this.pikkustegur);
        }
    }
}
