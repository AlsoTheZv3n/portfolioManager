from customtkinter import CTk, CLabel, CEntry, CButton
import tkinter as tk

class PortfolioManager(CTk):
    def __init__(self):
        super().__init__()

        # Load the black theme
        self.set_custom_theme("theme.json")

        self.title("Portfolio Manager")

        # Portfolio data
        self.portfolio = []

        # GUI components
        self.label_stock = CLabel(self, text="Stock Name:")
        self.label_stock.grid(row=0, column=0)
        self.entry_stock = CEntry(self)
        self.entry_stock.grid(row=0, column=1)

        self.label_quantity = CLabel(self, text="Quantity:")
        self.label_quantity.grid(row=1, column=0)
        self.entry_quantity = CEntry(self)
        self.entry_quantity.grid(row=1, column=1)

        self.label_price = CLabel(self, text="Price:")
        self.label_price.grid(row=2, column=0)
        self.entry_price = CEntry(self)
        self.entry_price.grid(row=2, column=1)

        self.btn_add = CButton(self, text="Add", command=self.add_entry)
        self.btn_add.grid(row=3, columnspan=2)

        self.btn_calculate = CButton(self, text="Calculate Total Value", command=self.calculate_total)
        self.btn_calculate.grid(row=4, columnspan=2)

        self.label_portfolio_count = CLabel(self, text="Portfolio Count: 0")
        self.label_portfolio_count.grid(row=5, columnspan=2)

        self.text_result = tk.Text(self, height=5, width=50)
        self.text_result.grid(row=6, columnspan=2)

    def add_entry(self):
        stock = self.entry_stock.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())
        self.portfolio.append((stock, quantity, price))
        self.entry_stock.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.update_result("Entry added successfully!")
        self.update_portfolio_count()

    def calculate_total(self):
        total_value = sum(quantity * price for _, quantity, price in self.portfolio)
        self.update_result(f"Total Portfolio Value: ${total_value:.2f}")

    def update_result(self, message):
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, message)

    def update_portfolio_count(self):
        self.label_portfolio_count.config(text=f"Portfolio Count: {len(self.portfolio)}")

if __name__ == "__main__":
    app = PortfolioManager()
    app.mainloop()
