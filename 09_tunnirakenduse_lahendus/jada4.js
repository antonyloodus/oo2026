"use strict";
class AbstractResistor {
}
class Resistor extends AbstractResistor {
    name;
    r;
    width = 70;
    constructor(name, r) {
        super();
        this.name = name;
        this.r = r;
    }
    getR() { return this.r; }
    getWidth() { return this.width; }
    draw(g, startx, y) {
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.width / 4, y);
        g.rect(startx + this.width / 4, y - 10, this.width / 2, 20);
        g.moveTo(startx + this.width * 3 / 4, y);
        g.lineTo(startx + this.width, y);
        g.stroke();
        g.fillText(this.name, startx + this.width / 4 + 1, y - 12);
        g.fillText(this.r + " Ω", startx + this.width / 4 + 1, y + 3);
    }
}
class SeriesCircuit extends AbstractResistor {
    name;
    items = [];
    constructor(name) {
        super();
        this.name = name;
    }
    push(item) {
        this.items.push(item);
    }
    getR() {
        let sum = 0;
        for (let it of this.items) {
            sum += it.getR();
        }
        return sum;
    }
    getWidth() {
        let w = 0;
        for (let it of this.items) {
            w += it.getWidth();
        }
        return w + 10;
    }
    draw(g, startx, y) {
        let x = startx;
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke();
        let areaStartX = x;
        for (let it of this.items) {
            it.draw(g, x, y);
            x += it.getWidth();
        }
        g.strokeStyle = "lightgray";
        g.beginPath();
        g.rect(areaStartX, y - 20, x - areaStartX, 40);
        g.stroke();
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke();
        g.fillText(this.name + ": " + this.getR() + " Ω", areaStartX, y + 32);
    }
}
