function decor_func(msg) {
    message = msg //free variable that exist on the js function decor_func which is dynamically generated

    function wrapper(name) { //innner function as a wrapper

        return `${msg} ${name} ` //adding up both the args of outer and inner functions

    }
    return wrapper
}

new_function1 = decor_func("Hello Good Afternoon")
console.log(new_function1("Abismruta"))

new_function2 = decor_func("Hello Good Night")
console.log(new_function2("Rika"))