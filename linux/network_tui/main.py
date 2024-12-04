from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Placeholder, DataTable, Input, Button
from textual.containers import Container, VerticalGroup
from wireless import get_networks, connect

class NetworkApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "NetworkApp.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Container(
            Placeholder('Status', id='p1'),
            DataTable(id='p2'),
            VerticalGroup(
                Input(placeholder='Network name', id='i1'),
                Input(placeholder='Passphrase', password=True, id='i2'),
                Button("Connect"),
                id='p3'
            )
        )
        yield Footer()

    def on_mount(self) -> None:

        ROWS = get_networks()
        table = self.query_one(DataTable)
        table.cursor_type = 'row'
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_data_table_row_selected(self, message: DataTable.RowSelected) -> None:
        network_name = self.query_one('#i1')
        network_name.insert_text_at_cursor(message.data_table.get_row_at(message.cursor_row)[0])
        network_name.focus()

    def on_button_pressed(self, _: Button.Pressed):
        network_name = self.query_one('#i1').value
        passphrase = self.query_one('#i1').value
        connect(network_name, passphrase)

if __name__ == "__main__":
    app = NetworkApp()
    app.run()