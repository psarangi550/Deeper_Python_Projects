function decor1(func) { //defing the function which takes another function as an args
    function wrapper(name) {
        result = func(name) + " Good Afternoon"
        return result
    }
    return wrapper
}

function my_func(name) {
    return "Hello " + name
}

new_func = decor1(my_func)
console.log(new_func("prarik"))