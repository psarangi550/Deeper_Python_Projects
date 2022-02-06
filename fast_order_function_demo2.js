function log_message(message) {

    function input_log() {

        return "Hello " + message

    }
    return input_log
}

new_func = log_message("hi") //calling the outer function which will return the inner function object
    //hence in this case function will printed as thats the string representation
console.log(new_func()) //calling the returned function