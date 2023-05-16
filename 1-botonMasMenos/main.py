import flet as ft

def main(page: ft.Page):
    page.title="contador mas menos"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    txt_contador= ft.TextField(value="7",text_align=ft.TextAlign.RIGHT,width=100)


    def minus_click(e):
        txt_contador.value= str(int(txt_contador.value)-1)
        page.update()

    def plus_click(e):
        txt_contador.value= str(int(txt_contador.value)+1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE,on_click=minus_click),
                txt_contador,
                ft.IconButton(ft.icons.ADD,on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)