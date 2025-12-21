from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Label
from textual.containers import Grid, Vertical, Center
import datetime
from textual.screen import Screen

class DayScreen(Screen):
    # screen for day of advent calendar
    
    CSS = """
    #dialog {
        width: 50;
        height: auto;
        border: thick $primary;
        background: $surface;
        padding: 2;
        align: center middle;
    }
    
    #dialog Label {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    
    #dialog Button {
        width: auto;
    }
    """
    
    gifts = {
        1: "React Workshop!",
        2: "Fusering Workshop!",
        3: "Keyring with Onshape!",
        4: "Hono Backend!",
        5: "Full Stack App with Flask!",
        6: "3D Printable Ruler!",
        7: "Interactive Christmas Tree!",
        8: "Automating Cookie Clicker!",
        9: "TUI in Textual!",
        10: "No leeks",
        11: "No leeks",
        12: "No leeks"
    }
    
    def __init__(self, day: int) -> None:
        self.day = day
        super().__init__()
        
    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(f"Here's what's in day {str(self.day)}: {self.gifts.get(self.day)}")
            with Center():
                yield Button("Close", id="close")
                
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss()
        event.stop()
        
        

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
        self.push_screen(DayScreen(int(day)))
        
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
            
def main():
    app = AdventCalendarApp()
    app.run()
    
if __name__ == "__main__":
    main()