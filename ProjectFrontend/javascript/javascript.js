function toplama() {
    let a = 5;
    let b = 6;
    let c = a + b;
    console.log(c)
}

// toplama();

function range(baslangic, son) {
    let cariDeyer = baslangic;
    if (baslangic === son) {
        console.log(cariDeyer);
        return;
    }

    console.log(cariDeyer);

    cariDeyer++;
    range(cariDeyer, son);
}

range(1, 3000);

console.log(5 == "5");
console.log(5 === "5");