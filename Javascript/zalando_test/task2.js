function solution(a,b){
	const maxRange = b/2
	let count = 0
	for (let i = 2; i <= maxRange; i++){
		const product = i*(i+1)
		if (product >= a && product <= b){
			++count
		} else if(product > b){
			break
		}
	}
	return count
}