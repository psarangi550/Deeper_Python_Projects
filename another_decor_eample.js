function tag_along(tag) {
    function input_msg(msg) {
        // return '<' + tag + '>' + msg + '< /' + tag + '>';
        return `<${tag}>${msg}</${tag}>`; //Es6 standard
    }
    return input_msg
}

input_msg_obj = tag_along("h1") //this is called as closure
console.log(input_msg_obj)
console.log(input_msg_obj("Hello world!"))


input_msg_obj = tag_along("p") //this is called as closure
console.log(input_msg_obj)
console.log(input_msg_obj("Hello Good Afternoon!"))