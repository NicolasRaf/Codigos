
function quickSort(vector){
    if (vector.length <= 1) {
        return vector;
    }

    const pivot = vector[0];
    const left = []
    const right = []

    for (let number of vector.slice(1)) { 
        if (number < pivot) {
            left.push(number); 
        } else {
            right.push(number); 
        }
    }

    return [...quickSort(left), pivot, ...quickSort(right)];
}

function main(){
    let vec = [34,1,323,5,6,8,90,0,1]

    let vecQuick = quickSort(vec)
    console.log(`${vec}`)
    console.log(`${vecQuick}`)
}

main()