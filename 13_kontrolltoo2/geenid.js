class Alleel {
    constructor(nimetus, positiivne) {
        this.nimetus = nimetus;
        this.positiivne = positiivne;
    }
}

class Geen {
    constructor(alleel1, alleel2) {
        this.alleel1 = alleel1;
        this.alleel2 = alleel2;
        this.nimetus = alleel1.nimetus;
    }

    onPositiivne() {
        return this.alleel1.positiivne || this.alleel2.positiivne;
    }

    randomAlleel() {
        return Math.random() < 0.5 ? this.alleel1 : this.alleel2;
    }
}

class GeenidApp {
    constructor() {
        this.geenid = [];
        this.järglased = [];
        this.valitudVanemad = [];
    }

    lisaGeen(nimetus, a1Positiivne, a2Positiivne) {
        const geen = new Geen(
            new Alleel(nimetus, a1Positiivne),
            new Alleel(nimetus, a2Positiivne)
        );
        this.geenid.push(geen);
        return geen;
    }

    otsiGeene(nimetus) {
        return this.geenid.filter(g =>
            g.nimetus.toLowerCase().includes(nimetus.toLowerCase())
        );
    }

    valiVanem(geen) {
        if (this.valitudVanemad.length >= 2) return false;
        if (this.valitudVanemad.includes(geen)) return false;
        this.valitudVanemad.push(geen);
        return true;
    }

    tühjendaValik() {
        this.valitudVanemad = [];
    }

    kombineeri() {
        if (this.valitudVanemad.length !== 2) {
            throw new Error("Kombineerimseks on vaja täpselt 2 vanemat");
        }
        const [v1, v2] = this.valitudVanemad;
        const järglane = new Geen(v1.randomAlleel(), v2.randomAlleel());
        this.järglased.push(järglane);
        this.tühjendaValik();
        return järglane;
    }

    kustutaJärglane(index) {
        this.järglased.splice(index, 1);
    }
}