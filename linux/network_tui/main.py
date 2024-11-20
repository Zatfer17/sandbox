from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListItem, ListView, Label, Switch

from wireless import get_networks


class NetworkListApp(App):

    def compose(self) -> ComposeResult: 
        networks = get_networks()

        list_items = []
        for ssid, signal in networks:

            list_items.append(
                ListItem(
                    Horizontal(
                        Label(f"{ssid} - {signal} dBm"),
                        Switch()
                    )
                )
            )

        yield ListView(*list_items)


if __name__ == "__main__":
    app = NetworkListApp()
    app.run()