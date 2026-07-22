from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_dashboard(local_data: dict, network_data: dict):
    console.print("\n[bold cyan]SYSPULSE[/bold cyan] [dim]v0.1.0 - System & Network Extractor[/dim]\n")

    sys_table = Table(show_header=True, header_style="bold magenta", expand=True)
    sys_table.add_column("Property", style="bold white", width=18)
    sys_table.add_column("Value", style="green")

    for key, val in local_data.items():
        sys_table.add_row(key, str(val))

    net_table = Table(show_header=True, header_style="bold yellow", expand=True)
    net_table.add_column("Network Field", style="bold white", width=18)
    net_table.add_column("Details", style="cyan")

    for key, val in network_data.items():
        net_table.add_row(key, str(val))

    console.print(Panel(sys_table, title="[bold magenta]💻 Local System Details[/bold magenta]", border_style="magenta"))
    console.print(Panel(net_table, title="[bold yellow]🌐 Public Network & Geolocation[/bold yellow]", border_style="yellow"))
