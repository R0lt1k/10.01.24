import docx

def create_word_file():
    user_text = input("Введите текст: ")

    doc = docx.Document()
    doc.add_paragraph(user_text)
    doc.save("user_text.docx")
    print(f"Word-файл 'user_text.docx' успешно создан.")

create_word_file()
