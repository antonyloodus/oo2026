class Resistor{
    protected width: number;
    constructor(protected name: string, protected g: any,
                protected x: number, protected y: number){
        this.width = name.length > 10 ? 60 : 50;
        this.draw();
    }
    draw(){
        this.g.beginPath();
        this.g.rect(this.x, this.y, this.width, 30);
        this.g.stroke();
        this.g.fillText(this.name, this.x + 5, this.y + 18);
    }
}
