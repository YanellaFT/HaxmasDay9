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
        1: "It's finally December! Let's count down to Christmas together. \n🎄🎄🎄",
        2: "Sign up for Aces :)",
        3: "Get someone to sign up for Aces",
        4: "Which one of Santa's reindeer has bad manners? \nRude-olph! \n🦌🦌🦌",
        5: "Sing some of your favorite holiday songs with your friends! \n🎶🎶🎶",
        6: "Go treat yourself to some hot cocoa! \n🍫🥛",
        7: "What do Santa's helpers lean in school? \nthe elf-abet!",
        8: "Bake some holiday cookies! \n🍪🍪🍪",
        9: "What holiday song do wolves sing? \nWe wish y-ooooooooo-u a merry Christmas!",
        10: "Create a holiday card for someone you care about! \n💝💝💝",
        11: "How do snowmen shop online? \nThey use the winter-net! \n⛄⛄⛄",
        12: "Do something to get you hyped for Haxmas starting tomorrow!",
        13: "React Workshop! \nHaxmas has started!",
        14: "Fusering Workshop! \nHaxmas Day 2",
        15: "Keyring with Onshape! \nHaxmas Day 3",
        16: "Hono Backend! \nHaxmas Day 4",
        17: "Full Stack App with Flask! \nHaxmas Day 5",
        18: "3D Printable Ruler! \nHaxmas Day 6",
        19: "Interactive Christmas Tree! \nHaxmas Day 7",
        20: "Automating Cookie Clicker! \nHaxmas Day 8",
        21: "TUI in Textual! \nHaxmas Day 9",
        22: "No leeks :3 \nHaxmas Day 10",
        23: "No leeks <3 \nHaxmas Day 11",
        24: "No leeks \nHaxmas Day 12 \nMerry Christmas!"
    }
    
    def __init__(self, day: int) -> None:
        self.day = day
        super().__init__()
        
    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(f"Dec {str(self.day)}, 2025: \n{self.gifts.get(self.day)}")
            with Center():
                yield Button("Close", id="close")
                
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss()
        event.stop()
        
        

class AdventCalendarApp(App):
    # A textual app for an advent calendar
    
    CSS = """
    Grid {
        grid-size: 5 5;
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
    
    BINDINGS = [("d", "toggle_dark", "Toggle Dark/Light Mode"), ("c", "action_countdown", "Show Countdown")]
    
    START_DATE = datetime.date(2025, 12, 1)
    CHRISTMAS_DATE = datetime.date(2025, 12, 25)
    
    def compose(self) -> ComposeResult:
        # create child widgets for app
        yield Header()
        with Grid():
            for day in range(1, 26):
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
        
    def action_countdown(self) -> None:
        days_left = 25 - datetime.date.today().days
        self.notify(f"{days_left} days until Christmas!")
        
            
def main():
    app = AdventCalendarApp()
    app.run()
    
if __name__ == "__main__":
    main()