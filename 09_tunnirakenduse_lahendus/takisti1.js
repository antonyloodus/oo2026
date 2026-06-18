"use strict";
class Resistor {
    name;
    g;
    x;
    y;
    width;
    constructor(name, g, x, y) {
        this.name = name;
        this.g = g;
        this.x = x;
        this.y = y;
        this.width = name.length > 10 ? 60 : 50;
        this.draw();
    }
    draw() {
        this.g.beginPath();
        this.g.rect(this.x, this.y, this.width, 30);
        this.g.stroke();
        this.g.fillText(this.name, this.x + 5, this.y + 18);
    }
}
