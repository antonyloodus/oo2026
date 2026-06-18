// ühine baasklass: nii üksik takisti kui jadaühendus on "abstraktne takisti".
// tänu sellele saab jadaühendusse panna nii Resistor- kui SeriesCircuit-objekte
// (kompositsioonimuster) ehk jada jadasse.
abstract class AbstractResistor{
    abstract getR(): number;
    abstract getWidth(): number;
    abstract draw(g: any, startx: number, y: number): void;
}

class Resistor extends AbstractResistor{
    readonly width: number = 70;
    constructor(protected name: string, protected r: number){
        super();
    }
    getR(){ return this.r; }
    getWidth(){ return this.width; }
    draw(g: any, startx: number, y: number){
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(startx, y);
        g.lineTo(startx + this.width/4, y);
        g.rect(startx + this.width/4, y - 10, this.width/2, 20);
        g.moveTo(startx + this.width*3/4, y);
        g.lineTo(startx + this.width, y);
        g.stroke();
        g.fillText(this.name, startx + this.width/4 + 1, y - 12);
        g.fillText(this.r + " Ω", startx + this.width/4 + 1, y + 3);
    }
}

class SeriesCircuit extends AbstractResistor{
    protected items: AbstractResistor[] = [];
    constructor(protected name: string){
        super();
    }
    push(item: AbstractResistor){
        this.items.push(item);
    }
    getR(){
        let sum = 0;
        for(let it of this.items){ sum += it.getR(); }
        return sum;
    }
    getWidth(){
        let w = 0;
        for(let it of this.items){ w += it.getWidth(); }
        return w + 10;   // 5px sissejuhtiv + 5px väljajuhtiv juhe
    }
    draw(g: any, startx: number, y: number){
        let x = startx;
        g.strokeStyle = "black";
        g.beginPath();
        g.moveTo(x, y);
        x += 5;
        g.lineTo(x, y);
        g.stroke();
        let areaStartX = x;
        for(let it of this.items){
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
