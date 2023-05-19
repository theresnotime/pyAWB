import constants
import dearpygui.dearpygui as dpg
from pwiki.wiki import Wiki


def print_me(sender):
    print(f"Menu Item: {sender}")


def resize():
    print(f"{dpg.get_viewport_height()} x {dpg.get_viewport_width()}")


def do_login():
    print("do_login")
    wiki = Wiki("test.wikipedia.org")
    logged_in = wiki.login(
        dpg.get_value("login_username"), dpg.get_value("login_password")
    )
    dpg.configure_item("login_modal", show=False)


def show_login():
    print("show_login")
    dpg.configure_item("login_modal", show=True)


def create_modals():
    with dpg.window(
        label="login_modal",
        modal=True,
        show=False,
        tag="login_modal",
        no_title_bar=True,
        pos=[300, 200],
    ):
        dpg.add_text("Login")
        dpg.add_input_text(hint="Username", tag="login_username")
        dpg.add_input_text(hint="Password", tag="login_password", password=True)
        with dpg.group(horizontal=True):
            dpg.add_button(label="OK", width=75, callback=do_login)
            dpg.add_button(
                label="Cancel",
                width=75,
                callback=lambda: dpg.configure_item("login_modal", show=False),
            )


def create_window():
    dpg.create_viewport(
        title=f"{constants.SW_NAME} v{constants.SW_VERSION}", width=1024, height=600
    )
    with dpg.window(tag="Primary Window"):
        # dpg.add_text("Hello, world")
        create_menu_bar()
        create_modals()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.set_viewport_resize_callback(callback=resize)
        dpg.start_dearpygui()
        dpg.destroy_context()


def create_menu_bar():
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Login", callback=show_login)

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
                dpg.add_menu_item(label="Setting 2", callback=print_me)

        dpg.add_menu_item(label="Help", callback=print_me)


def main():
    create_window()


if __name__ == "__main__":
    dpg.create_context()
    main()
