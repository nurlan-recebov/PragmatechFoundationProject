let a = 0

function nurlan() {

    if (a < 100) {
        a++;
        if (a < 100 && a % 3 === 0 && a % 5 === 0) {
            console.log(a);
        }
        nurlan()
    }
}
nurlan()