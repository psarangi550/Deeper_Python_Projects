def sent_gen(value):
    for item in value.split():
        yield item

sent_gen_obj=sent_gen("My Name is Pratik")

for item in sent_gen_obj:
    print(item)