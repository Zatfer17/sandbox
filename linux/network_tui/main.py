from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, Vertical, Horizontal
from textual.widgets import Label, Button, SelectionList, Footer


class NetworkTUI(App):

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("Hello, world!", id='a')
            yield Label("Hello, world 2!", id='b')
            yield Label("Hello, world 3!", id='c')
        with SelectionList
        yield Footer()


if __name__ == "__main__":
    app = NetworkTUI()
    app.run()