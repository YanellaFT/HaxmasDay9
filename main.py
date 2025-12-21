from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button
from textual.containers import Grid
import datetime

class AdventCalendarApp(App):
    # A textual app for an advent calendar
    
    CSS = """
    Grid {
        grid-size: 4 3;
        grid-gutter: 1 2;
    }
    Grid Button {
        width: 100%;
        height: 100%;
    }
    Grid Button:hover {
        background:$secondary;
    }
    Grid Button.opened {
        background: $success;
    }
    """
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    START_DATE = datetime.date(2025, 12, 13)
    
    def compose(self) -> ComposeResult:
        # create child widgets for app
        yield Header()
        with Grid():
            for day in range(1, 13):
                yield Button(str(day), id=f"day-{day}")
        yield Footer()
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button = event.button
        day = str(button.label)
        unlock_day = self.START_DATE + datetime.timedelta(days=int(day)-1)
        
        if datetime.date.today() < unlock_day:
            self.notify(f"You will be able to unlock day {day} on {unlock_day}")
            return None
        
        if not button.has_class("opened"):
            button.add_class("opened")
            day = button.label
            self.notify(f"Day {day} opened!")
        
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
            
def main():
    app = AdventCalendarApp()
    app.run()
    
if __name__ == "__main__":
    main()