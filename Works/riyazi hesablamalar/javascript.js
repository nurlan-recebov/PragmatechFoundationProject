var b = 0

function eded() {
    b++
    if (b <= 300) {
        console.log(b);
        eded()
    }

}



eded()
let a = 0;

function or() {
    a++
    if (a < 20) {

        console.log("nurlan");
        or(a)
    }

}
or()
let c = ["alma", "armud", "heyva"]

function nurlan() {

    for (let i = 0; i < c.length; i++) {
        console.log(c[i]);
    }

}
nurlan()