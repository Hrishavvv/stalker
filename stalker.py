import whois
from rich.console import Console
from rich.progress import Progress, BarColumn
from rich.panel import Panel
from rich.text import Text

# Initialize the Rich Console
console = Console()

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)

        console.print(Panel(f"[bold cyan]Domain Information[/bold cyan]:", title="[bold cyan]Domain Details[/bold cyan]", style="bold"))
        for key, value in domain_info.items():
            if isinstance(value, list):
                value = ', '.join(str(v) for v in value)
            console.print(f"[bold]{key}[/bold]: {value}")

        console.print("\n[bold cyan]Made by Hrishav Sanyal[/bold cyan]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def main():
    try:
        # Displaying ASCII art before input
        ascii_art = r'''
         ____    __             ___    __                      
        /\  _`\ /\ \__         /\_ \  /\ \                     
        \ \,\L\_\ \ ,_\    __  \//\ \ \ \ \/'\      __   _ __  
         \/_\__ \\ \ \/  /'__`\  \ \ \ \ \ , <    /'__`\/\`'__\
           /\ \L\ \ \ \_/\ \L\.\_ \_\ \_\ \ \\`\ /\  __/\ \ \/ 
           \ `\____\ \__\ \__/.\_\/\____\\ \_\ \_\ \____\\ \_\ 
            \/_____/\/__/\/__/\/_/\/____/ \/_/\/_/\/____/ \/_/ 
        '''
        console.print(Text(ascii_art, style="cyan"))

        # Input prompt in default color
        domain_name = console.input("Enter the domain name: ").strip()

        with Progress(
            "{task.description}",
            BarColumn(bar_width=None),
            console=console,
        ) as progress:
            task = progress.add_task("[bold cyan]Fetching Domain Information...[/bold cyan]", total=1)
            get_domain_info(domain_name)
            progress.update(task, advance=1)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]User cancelled the operation.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
                
