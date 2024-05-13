import flet as ft    #importing stuff
import time
import math
import random
R1 = 0
R2 = 1
R3 = 0
R4 = 1
C1 = 19             #Variables for info redacting
C2 = 21
C3  = 30
C4 = 1337
RoomNum = int(random.randint(1, 9999))              #Random var for Room number
RoomNum = str()

def main(page: ft.Page):
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    # page.add(
    #     ft.Container(
    #         bgcolor=ft.colors.GREY_200,
    #         height=1080,
    #         width=1920
    #     )
    # )
    RESTEXT = ft.Text("You can pay for the room when you arrive! your room number is: 2183", size=25)

    OCUTEXT = ft.Row(controls=[
            ft.Text("This room is"),
            ft.Text("occupied!", color="RED800")
        ])
    FREETEXT = ft.Row(controls=[
            ft.Text("                                                                               This room is",
                    size=25),
            ft.Text("free!", color="GREEN800", size=25)                             #Variables for text and info for user

        ])
    CASHTEXT = ft.Row(controls=[
            ft.Text("Claim it? (Price for a day = 20$)"),

        ])
    ROOM1 = ft.Row(controls =[
            ft.Text('Description: Average room, 1 window, a balcony, 37 square meters, bathroom and kitchen.', size=25)
        ])
    ROOM2 = ft.Row(controls =[
            ft.Text('Description: Small room, 1 window, 25 square meters, bathroom.', size=25)                          #Description redaction of rooms
        ])
    ROOM3 = ft.Row(controls =[
            ft.Text('Description: Big room, 2 windows, a balcony, 52 square meters, bathroom and kitchen.', size=25)
        ])
    ROOM4 = ft.Row(controls =[
            ft.Text('Description: Average room, 2 windows, 40 square meters, bathroom and kitchen.', size=25)
        ])






    def NO(e):
        e.control.page.remove(e.control)
        e.control.page.update()

    NOBUT = ft.ElevatedButton(text="No, thanks!", width=120, height=120, on_click=NO)
    page.update()
    def YES(e):
        page.add(RESTEXT)                                                       #Buttons yes/no


    YESBUT = ft.ElevatedButton(text="Yes!", width=120, height=120, on_click=YES)
    page.update()



    def OCUROOM1(e):
        if R1 == 1:
            page.add(OCUTEXT)

        else:
            page.add(FREETEXT,ROOM1, CASHTEXT, NOBUT, YESBUT,)
            page.update()
    def OCUROOM2(e):
        if R2 == 1:
            page.add(OCUTEXT)

        else:
            page.add(FREETEXT,ROOM2, CASHTEXT, NOBUT, YESBUT)
            page.update()
    def OCUROOM3(e):
        if R3 == 1:
            page.add(OCUTEXT)                                               #Room buttons

        else:
            page.add(FREETEXT,ROOM3, CASHTEXT, NOBUT, YESBUT)
            page.update()
    def OCUROOM4(e):
        if R4 == 1:
            page.add(OCUTEXT)

        else:
            page.add(FREETEXT,ROOM4, CASHTEXT, NOBUT, YESBUT)
            page.update()
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
                key="B",                                                #making a cool container
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
                            ),                                                                                     #Scrolling buttons
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