import flet as ft    #importing stuff
import time
import pandas as pd
import math
R1 = 0
R2 = 1
R3 = 0
R4 = 1
# НЕ ЗАБУДЬ ПЕРЕВЕСТИ ВСЕХ ИХ В ПЕРЕМЕННЫЕ!!!
def main(page: ft.Page):
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    # page.add(
    #     ft.Container(
    #         bgcolor=ft.colors.GREY_200,
    #         height=1080,
    #         width=1920
    #     )
    # )
    def YES(e):
        print("smth smth its just a placeholder for now")
    def NO(e):
        print("smth smth its just a placeholder for now")
    def OCUROOM1(e):
        if R1 == 1:
            page.add(
                ft.Row(controls=[
                    ft.Text("This room is"),
                    ft.Text("occupied!", color="RED800")
                ])
            )
        else:
            page.add(
                ft.Row(controls=[
                    ft.Text("                                                                               This room is", size=25),
                    ft.Text("free!", color="GREEN800", size=25)

                ]),
                ft.Row(controls=[
                    ft.Text("Claim it? (Price for a day = 20$)"),

                ]),
                ft.Row(controls=[
                    ft.ElevatedButton(text="Yes!", width=120, height=120),
                    ft.ElevatedButton(text="No, thanks!", width=120, height=120),
                ])
            )
    def OCUROOM2(e):
        if R2 == 1:
            page.add(
                ft.Row(controls=[
                    ft.Text("This room is"),
                    ft.Text("occupied!", color="RED800")
                ])
            )
        else:
            page.add(
                ft.Row(controls=[
                    ft.Text("                                                                               This room is", size=25),
                    ft.Text("free!", color="GREEN800", size=25)

                ]),
                ft.Row(controls=[
                    ft.Text("Claim it? (Price for a day = 20$)"),

                ]),
                ft.Row(controls=[
                    ft.ElevatedButton(text="Yes!", width=120, height=120),
                    ft.ElevatedButton(text="No, thanks!", width=120, height=120),
                ])
            )
    def OCUROOM3(e):
        if R3 == 1:
            page.add(
                ft.Row(controls=[
                    ft.Text("This room is"),
                    ft.Text("occupied!", color="RED800")
                ])
            )
        else:
            page.add(
                ft.Row(controls=[
                    ft.Text("                                                                               This room is", size=25),
                    ft.Text("free!", color="GREEN800", size=25)

                ]),
                ft.Row(controls=[
                    ft.Text("Claim it? (Price for a day = 20$)"),

                ]),
                ft.Row(controls=[
                    ft.ElevatedButton(text="Yes!", width=120, height=120),
                    ft.ElevatedButton(text="No, thanks!", width=120, height=120),
                ])
            )
    def OCUROOM4(e):
        if R4 == 1:
            page.add(
                ft.Row(controls=[
                    ft.Text("This room is"),
                    ft.Text("occupied!", color="RED800")
                ])
            )
        else:
            page.add(
                ft.Row(controls=[
                    ft.Text("                                                                               This room is", size=25),
                    ft.Text("free!", color="GREEN800", size=25)

                ]),
                ft.Row(controls=[
                    ft.Text("Claim it? (Price for a day = 20$)"),

                ]),
                ft.Row(controls=[
                    ft.ElevatedButton(text="Yes!", width=120, height=120),
                    ft.ElevatedButton(text="No, thanks!", width=120, height=120),
                ])
            )
    t = ft.Text(size=20)            #adding text.
    page.add(t)
    cl = ft.Column(
        spacing=10,
        height=180,
        width=300,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            ft.Container(
                ft.ElevatedButton(text="Room 1", on_click=OCUROOM1),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.YELLOW_200,
                height=100,
                key="A",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 2", on_click=OCUROOM2),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.YELLOW_200,
                height=100,
                key="B",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 3", on_click=OCUROOM3),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.YELLOW_200,
                height=100,
                key="C",
            ),
            ft.Container(
                ft.ElevatedButton(text="Room 4", on_click=OCUROOM4),
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.YELLOW_200,
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


        #This stuff happens when the button is being clicked, basicly confirmation of login, it will send all this stuff to the next part of code shortly after.
        time.sleep(5)

    t = ft.Text()
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

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
#im so done
