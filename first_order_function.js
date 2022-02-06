function my_map(func, my_array) {
    var result = [] //assigning the new empty string in order to append
    for (item in my_array)
        result.push(func(item))
    return result
}

function myfunc(a) {
    return a * a
}

function cubefunc(a) {
    return a * a * a
}

new_func = my_map(myfunc, [1, 2, 3, 4])
console.log(new_func)

new_func = my_map(cubefunc, [1, 2, 3, 4])
console.log(new_func)