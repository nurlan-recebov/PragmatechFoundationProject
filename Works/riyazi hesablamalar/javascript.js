var b = 0

function eded() {
    b++
    if (b <= 300) {
        console.log(b);
        eded()
    }

}



eded()