import flet as ft    #importing stuff
import time
import math
def main(page: ft.Page):
    t = ft.Text(size=20)            #adding text.
    page.add(t)
    cl = ft.Column(
        spacing=10,
        height=180,
        width=300,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Container(
                ft.ElevatedButton(text="Room 1"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.RED_200,
                height=100,
                key="A",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 2"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.GREEN_200,
                height=100,
                key="B",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 3"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.GREEN_200,
                height=100,
                key="C",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 4"),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.RED_200,
                height=100,
                key="D",
            ),
        ],
    )

    for i in range(2):
        t.value = "Loading..."
        page.update()
        time.sleep(1)               #Fake loading >:))
    t.value = "Done!"
    page.update()


    def button_clicked(e):
        t.value = f"You are signed in as:  '{Login.value}'."
        page.update()
        e.control.page.controls.remove(butt)
        e.control.page.controls.remove(Login)
        e.control.page.controls.remove(Password)
        page.add(
            ft.Row(controls=[
                ft.Text(f"You are signed in as:  '{Login.value}'.", size=20),  # Its just a lil text

            ]),
            ft.Row(controls=[
                ft.Text("                                                  PICK A NOT OCCUPIED ROOM", size=30),  # Its just a lil text

            ])
        )
        page.add(
            ft.Container(cl, border=ft.border.all(1)),
            ft.Column(
                [
                    ft.Text("Scroll to:"),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Room 1",
                                on_click=lambda _: cl.scroll_to(key="A", duration=1000),
                            ),
                            ft.ElevatedButton(
                                "Room 2",
                                on_click=lambda _: cl.scroll_to(key="B", duration=1000),
                            ),
                            ft.ElevatedButton(
                                "Room 3",
                                on_click=lambda _: cl.scroll_to(key="C", duration=1000),
                            ),
                            ft.ElevatedButton(
                                "Room 4",
                                on_click=lambda _: cl.scroll_to(key="D", duration=1000),
                            ),
                        ]
                    ),
                ]
            ),
        )

        page.update()


        #This stuff happens when the button is being clicked, bassicly confirmation of login, it will send all this stuff to the next part of code shortly after.
        time.sleep(5)

    t = ft.Text()
    Room1 = ft.ElevatedButton(text="Room 1")
    Room2 = ft.ElevatedButton(text="Room 2")
    Room3 = ft.ElevatedButton(text="Room 3")
    Room4 = ft.ElevatedButton(text="Room 4")
    Room5 = ft.ElevatedButton(text="Room 5")
    Login = ft.TextField(label="Name")
    Password = ft.TextField(label="Password")              #Giving variables some meaning, like, making them a button??
    butt = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(
        ft.Row(controls=[
            ft.Text("Sign in")  # Its just a lil text

        ])
    )

    page.add(Login, Password, butt)           #working with the variables i commentated earlier...
    page.update()

ft.app(target=main)
#im so fucking done