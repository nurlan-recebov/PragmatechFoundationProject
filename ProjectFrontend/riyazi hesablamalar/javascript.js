let b = 0

function eded() {
    b++
    if (b <= 3000) {
        console.log(b);
        eded()
    }

}
eded()