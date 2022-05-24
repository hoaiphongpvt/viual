const canvas = document.getElementById('canvas')
const ctx = canvas.getContext("2d")

let cw = window.innerWidth
let ch = window.innerHeight

let charArr = ['N', 'G', 'U', 'Y', 'E', 'N', 'H', 'O', 'A', 'I','P', 'H', 'O', 'N', 'G']

let maxCharCount = 1000
let fallingCharArr = []
let fontSize = 15
let maxColums = cw/fontSize
canvas.width = cw
canvas.height = ch

let frame = 0

class FallingChar {
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    draw(ctx){
        this.value = charArr[Math.floor(Math.random() * (charArr.length - 1))].toUpperCase()
        this.speed = Math.random() * fontSize * 3/4 + fontSize * 3/4

        ctx.fillStyle = "rgba(0,255,0)"
        ctx.font = fontSize + "px san-serif"
        ctx.fillText(this.value, this.x, this.y)
        this.y += this.speed;
    }
}

let update = () => {
    if(fallingCharArr.length < maxCharCount) {
        let fallingChar = new FallingChar(Math.floor(Math.random() * maxColums) * fontSize, Math.random() * ch/2 - 50)
        fallingCharArr.push(fallingChar)
    }
    ctx.fillStyle = "rgba(0,0,0,0.05)"
    ctx.fillRect(0,0,cw,ch)
    for(let i = 0; i < fallingCharArr.length && frame % 2 == 0; i++) {
        fallingCharArr[i].draw(ctx);
    }

    requestAnimationFrame(update);
    frame++;
};

update();