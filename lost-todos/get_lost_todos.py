# write script that scrapes todos from old rails logs in 'lost_todos.txt'


f = open('lost_todos.txt', 'r')
content = f.read()
for line in content.split('\n'):
    if 'Create' in line and 'todos' in line:
        todo_from_name = line.split('[["name", "')[1]
        todo_name_text = todo_from_name.split(', ["importance",')[0]
        split_name_text = todo_name_text.split('"], ["')
        print(split_name_text[0])
        if 'text' in split_name_text[1]:
            if split_name_text[1].split('text", ')[1] != '""]':
                print(split_name_text[1].split('text", ')[1])

        



f.close()