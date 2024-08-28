export const doMap = (vector, work) => {
  const newVector = []

  for (let i of vector){
      newVector.push(work(i))
  }
  return newVector
}

export const doFilter = (vector, work) => {
  const newVector = []

  for (let i of vector){
      if (work(i)){
          newVector.push(i)
      }
  }
  return newVector
}

export const doReduce = (vector, work) => {
  const newVector = []

  for (let i of vector){
      if (work(i)){
          newVector.push(i)
      }
  }
  return newVector
}


let list = [1,2,3,4,5]

console.log(doFilter(list, n => n > 1))