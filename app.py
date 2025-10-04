import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import uuid

# Demo Databases
users_db = {
    'user1': {'password': 'pass123', 'name': 'John Doe'},
    'user2': {'password': 'pass456', 'name': 'Jane Smith'}
}

admin_db = {
    'admin': {'password': 'admin123', 'name': 'Administrator'}
}

categories_db = {
    1: 'Boots',
    2: 'Coats',
    3: 'Jackets',
    4: 'Caps'
}

products_db = {
    101: {'name': 'Leather Boots', 'category_id': 1, 'price': 89.99},
    102: {'name': 'Winter Boots', 'category_id': 1, 'price': 79.99},
    103: {'name': 'Rain Coat', 'category_id': 2, 'price': 59.99},
    104: {'name': 'Wool Coat', 'category_id': 2, 'price': 129.99},
    105: {'name': 'Denim Jacket', 'category_id': 3, 'price': 69.99},
    106: {'name': 'Leather Jacket', 'category_id': 3, 'price': 149.99},
    107: {'name': 'Baseball Cap', 'category_id': 4, 'price': 19.99},
    108: {'name': 'Beanie Cap', 'category_id': 4, 'price': 14.99}
}

cart_db = {}
sessions_db = {}

class ShoppingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Demo Marketplace")
        self.root.geometry("900x600")
        self.root.configure(bg='#f0f0f0')
        
        self.current_session = None
        self.next_product_id = max(products_db.keys()) + 1
        self.next_category_id = max(categories_db.keys()) + 1
        
        self.show_welcome_screen()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_welcome_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#2c3e50')
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Welcome to the Demo Marketplace", 
                font=('Arial', 24, 'bold'), bg='#2c3e50', fg='white').pack(pady=50)
        
        btn_frame = tk.Frame(frame, bg='#2c3e50')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="User Login", font=('Arial', 14), 
                 bg='#3498db', fg='white', width=15, command=self.show_user_login).pack(pady=10)
        tk.Button(btn_frame, text="Admin Login", font=('Arial', 14), 
                 bg='#e74c3c', fg='white', width=15, command=self.show_admin_login).pack(pady=10)
        tk.Button(btn_frame, text="Exit", font=('Arial', 14), 
                 bg='#95a5a6', fg='white', width=15, command=self.root.quit).pack(pady=10)
    
    def show_user_login(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#ecf0f1')
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="User Login", font=('Arial', 20, 'bold'), 
                bg='#ecf0f1').pack(pady=30)
        
        tk.Label(frame, text="Username:", font=('Arial', 12), bg='#ecf0f1').pack(pady=5)
        username_entry = tk.Entry(frame, font=('Arial', 12), width=30)
        username_entry.pack(pady=5)
        
        tk.Label(frame, text="Password:", font=('Arial', 12), bg='#ecf0f1').pack(pady=5)
        password_entry = tk.Entry(frame, font=('Arial', 12), width=30, show='*')
        password_entry.pack(pady=5)
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            
            if username in users_db and users_db[username]['password'] == password:
                self.current_session = str(uuid.uuid4())
                sessions_db[self.current_session] = {'username': username, 'role': 'user'}
                cart_db[self.current_session] = {}
                messagebox.showinfo("Success", f"Welcome {users_db[username]['name']}!")
                self.show_user_menu()
            else:
                messagebox.showerror("Error", "Invalid credentials!")
        
        tk.Button(frame, text="Login", font=('Arial', 12), bg='#3498db', 
                 fg='white', width=15, command=login).pack(pady=20)
        tk.Button(frame, text="Back", font=('Arial', 12), bg='#95a5a6', 
                 fg='white', width=15, command=self.show_welcome_screen).pack(pady=5)
    
    def show_admin_login(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#ecf0f1')
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Admin Login", font=('Arial', 20, 'bold'), 
                bg='#ecf0f1').pack(pady=30)
        
        tk.Label(frame, text="Username:", font=('Arial', 12), bg='#ecf0f1').pack(pady=5)
        username_entry = tk.Entry(frame, font=('Arial', 12), width=30)
        username_entry.pack(pady=5)
        
        tk.Label(frame, text="Password:", font=('Arial', 12), bg='#ecf0f1').pack(pady=5)
        password_entry = tk.Entry(frame, font=('Arial', 12), width=30, show='*')
        password_entry.pack(pady=5)
        
        def login():
            username = username_entry.get()
            password = password_entry.get()
            
            if username in admin_db and admin_db[username]['password'] == password:
                self.current_session = str(uuid.uuid4())
                sessions_db[self.current_session] = {'username': username, 'role': 'admin'}
                cart_db[self.current_session] = {}
                messagebox.showinfo("Success", f"Welcome {admin_db[username]['name']}!")
                self.show_admin_menu()
            else:
                messagebox.showerror("Error", "Invalid admin credentials!")
        
        tk.Button(frame, text="Login", font=('Arial', 12), bg='#e74c3c', 
                 fg='white', width=15, command=login).pack(pady=20)
        tk.Button(frame, text="Back", font=('Arial', 12), bg='#95a5a6', 
                 fg='white', width=15, command=self.show_welcome_screen).pack(pady=5)
    
    def show_user_menu(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#ecf0f1')
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="User Menu", font=('Arial', 20, 'bold'), 
                bg='#ecf0f1').pack(pady=20)
        
        btn_frame = tk.Frame(frame, bg='#ecf0f1')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="View Catalog", font=('Arial', 12), 
                 bg='#3498db', fg='white', width=20, command=self.view_catalog).pack(pady=5)
        tk.Button(btn_frame, text="View Cart", font=('Arial', 12), 
                 bg='#2ecc71', fg='white', width=20, command=self.view_cart).pack(pady=5)
        tk.Button(btn_frame, text="Add to Cart", font=('Arial', 12), 
                 bg='#f39c12', fg='white', width=20, command=self.add_to_cart).pack(pady=5)
        tk.Button(btn_frame, text="Remove from Cart", font=('Arial', 12), 
                 bg='#e67e22', fg='white', width=20, command=self.remove_from_cart).pack(pady=5)
        tk.Button(btn_frame, text="Checkout", font=('Arial', 12), 
                 bg='#9b59b6', fg='white', width=20, command=self.checkout).pack(pady=5)
        tk.Button(btn_frame, text="Logout", font=('Arial', 12), 
                 bg='#95a5a6', fg='white', width=20, command=self.logout).pack(pady=5)
    
    def show_admin_menu(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#ecf0f1')
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Admin Menu", font=('Arial', 20, 'bold'), 
                bg='#ecf0f1').pack(pady=20)
        
        btn_frame = tk.Frame(frame, bg='#ecf0f1')
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="View Catalog", font=('Arial', 12), 
                 bg='#3498db', fg='white', width=20, command=self.view_catalog).pack(pady=5)
        tk.Button(btn_frame, text="Add Product", font=('Arial', 12), 
                 bg='#2ecc71', fg='white', width=20, command=self.add_product).pack(pady=5)
        tk.Button(btn_frame, text="Update Product", font=('Arial', 12), 
                 bg='#f39c12', fg='white', width=20, command=self.update_product).pack(pady=5)
        tk.Button(btn_frame, text="Delete Product", font=('Arial', 12), 
                 bg='#e74c3c', fg='white', width=20, command=self.delete_product).pack(pady=5)
        tk.Button(btn_frame, text="Add Category", font=('Arial', 12), 
                 bg='#9b59b6', fg='white', width=20, command=self.add_category).pack(pady=5)
        tk.Button(btn_frame, text="Delete Category", font=('Arial', 12), 
                 bg='#c0392b', fg='white', width=20, command=self.delete_category).pack(pady=5)
        tk.Button(btn_frame, text="Logout", font=('Arial', 12), 
                 bg='#95a5a6', fg='white', width=20, command=self.logout).pack(pady=5)
    
    def view_catalog(self):
        window = tk.Toplevel(self.root)
        window.title("Product Catalog")
        window.geometry("700x500")
        
        tk.Label(window, text="Product Catalog", font=('Arial', 18, 'bold')).pack(pady=10)
        
        text_area = scrolledtext.ScrolledText(window, font=('Courier', 10), width=80, height=25)
        text_area.pack(pady=10)
        
        for cat_id, cat_name in sorted(categories_db.items()):
            text_area.insert(tk.END, f"\n[Category: {cat_name}]\n")
            for prod_id, prod_info in products_db.items():
                if prod_info['category_id'] == cat_id:
                    text_area.insert(tk.END, 
                        f"  ID: {prod_id} | {prod_info['name']} | Rs. {prod_info['price']:.2f}\n")
        
        text_area.config(state='disabled')
    
    def view_cart(self):
        if not self.is_user():
            messagebox.showerror("Error", "Only users can view cart!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Shopping Cart")
        window.geometry("600x400")
        
        tk.Label(window, text="Your Cart", font=('Arial', 18, 'bold')).pack(pady=10)
        
        text_area = scrolledtext.ScrolledText(window, font=('Courier', 11), width=70, height=15)
        text_area.pack(pady=10)
        
        if not cart_db[self.current_session]:
            text_area.insert(tk.END, "Your cart is empty")
        else:
            total = 0
            for prod_id, quantity in cart_db[self.current_session].items():
                if prod_id in products_db:
                    prod = products_db[prod_id]
                    subtotal = prod['price'] * quantity
                    total += subtotal
                    text_area.insert(tk.END, 
                        f"{prod['name']} x{quantity} = Rs. {subtotal:.2f}\n")
            text_area.insert(tk.END, f"\nTotal: Rs. {total:.2f}")
        
        text_area.config(state='disabled')
    
    def add_to_cart(self):
        if not self.is_user():
            messagebox.showerror("Error", "Only users can add to cart!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Add to Cart")
        window.geometry("400x250")
        
        tk.Label(window, text="Add to Cart", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Product ID:", font=('Arial', 11)).pack(pady=5)
        prod_entry = tk.Entry(window, font=('Arial', 11), width=20)
        prod_entry.pack(pady=5)
        
        tk.Label(window, text="Quantity:", font=('Arial', 11)).pack(pady=5)
        qty_entry = tk.Entry(window, font=('Arial', 11), width=20)
        qty_entry.pack(pady=5)
        
        def add():
            try:
                prod_id = int(prod_entry.get())
                quantity = int(qty_entry.get())
                
                if prod_id not in products_db:
                    messagebox.showerror("Error", "Product not found!")
                    return
                
                if quantity <= 0:
                    messagebox.showerror("Error", "Quantity must be positive!")
                    return
                
                if prod_id in cart_db[self.current_session]:
                    cart_db[self.current_session][prod_id] += quantity
                else:
                    cart_db[self.current_session][prod_id] = quantity
                
                messagebox.showinfo("Success", 
                    f"Added {quantity} x {products_db[prod_id]['name']} to cart!")
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Add", font=('Arial', 11), bg='#2ecc71', 
                 fg='white', width=15, command=add).pack(pady=10)
    
    def remove_from_cart(self):
        if not self.is_user():
            messagebox.showerror("Error", "Only users can remove from cart!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Remove from Cart")
        window.geometry("400x200")
        
        tk.Label(window, text="Remove from Cart", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Product ID:", font=('Arial', 11)).pack(pady=5)
        prod_entry = tk.Entry(window, font=('Arial', 11), width=20)
        prod_entry.pack(pady=5)
        
        def remove():
            try:
                prod_id = int(prod_entry.get())
                
                if prod_id in cart_db[self.current_session]:
                    del cart_db[self.current_session][prod_id]
                    messagebox.showinfo("Success", 
                        f"Removed {products_db[prod_id]['name']} from cart!")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Product not in cart!")
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Remove", font=('Arial', 11), bg='#e74c3c', 
                 fg='white', width=15, command=remove).pack(pady=10)
    
    def checkout(self):
        if not self.is_user():
            messagebox.showerror("Error", "Only users can checkout!")
            return
        
        if not cart_db[self.current_session]:
            messagebox.showwarning("Warning", "Your cart is empty!")
            return
        
        total = sum(products_db[pid]['price'] * qty 
                   for pid, qty in cart_db[self.current_session].items())
        
        window = tk.Toplevel(self.root)
        window.title("Checkout")
        window.geometry("450x350")
        
        tk.Label(window, text="Checkout", font=('Arial', 16, 'bold')).pack(pady=20)
        tk.Label(window, text=f"Total Amount: Rs. {total:.2f}", 
                font=('Arial', 14)).pack(pady=10)
        
        tk.Label(window, text="Select Payment Method:", 
                font=('Arial', 12)).pack(pady=10)
        
        payment_var = tk.StringVar(value="UPI")
        
        tk.Radiobutton(window, text="Net Banking", variable=payment_var, 
                      value="Net Banking", font=('Arial', 11)).pack()
        tk.Radiobutton(window, text="PayPal", variable=payment_var, 
                      value="PayPal", font=('Arial', 11)).pack()
        tk.Radiobutton(window, text="UPI", variable=payment_var, 
                      value="UPI", font=('Arial', 11)).pack()
        tk.Radiobutton(window, text="Debit Card", variable=payment_var, 
                      value="Debit Card", font=('Arial', 11)).pack()
        
        def complete():
            method = payment_var.get()
            messagebox.showinfo("Success", 
                f"You will be redirected to {method} portal to make payment of Rs. {total:.2f}\n\n" +
                "Your order is successfully placed!")
            cart_db[self.current_session] = {}
            window.destroy()
        
        tk.Button(window, text="Complete Payment", font=('Arial', 11), 
                 bg='#2ecc71', fg='white', width=20, command=complete).pack(pady=20)
    
    def add_product(self):
        if not self.is_admin():
            messagebox.showerror("Error", "Only admin can add products!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Add Product")
        window.geometry("400x300")
        
        tk.Label(window, text="Add New Product", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Product Name:", font=('Arial', 11)).pack(pady=5)
        name_entry = tk.Entry(window, font=('Arial', 11), width=25)
        name_entry.pack(pady=5)
        
        tk.Label(window, text="Category ID:", font=('Arial', 11)).pack(pady=5)
        cat_entry = tk.Entry(window, font=('Arial', 11), width=25)
        cat_entry.pack(pady=5)
        
        tk.Label(window, text="Price:", font=('Arial', 11)).pack(pady=5)
        price_entry = tk.Entry(window, font=('Arial', 11), width=25)
        price_entry.pack(pady=5)
        
        def add():
            try:
                name = name_entry.get()
                cat_id = int(cat_entry.get())
                price = float(price_entry.get())
                
                if cat_id not in categories_db:
                    messagebox.showerror("Error", "Invalid category ID!")
                    return
                
                products_db[self.next_product_id] = {
                    'name': name,
                    'category_id': cat_id,
                    'price': price
                }
                messagebox.showinfo("Success", 
                    f"Product added! Product ID: {self.next_product_id}")
                self.next_product_id += 1
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Add Product", font=('Arial', 11), 
                 bg='#2ecc71', fg='white', width=15, command=add).pack(pady=10)
    
    def update_product(self):
        if not self.is_admin():
            messagebox.showerror("Error", "Only admin can update products!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Update Product")
        window.geometry("400x350")
        
        tk.Label(window, text="Update Product", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Product ID:", font=('Arial', 11)).pack(pady=5)
        id_entry = tk.Entry(window, font=('Arial', 11), width=25)
        id_entry.pack(pady=5)
        
        tk.Label(window, text="New Name (optional):", font=('Arial', 11)).pack(pady=5)
        name_entry = tk.Entry(window, font=('Arial', 11), width=25)
        name_entry.pack(pady=5)
        
        tk.Label(window, text="New Category ID (optional):", font=('Arial', 11)).pack(pady=5)
        cat_entry = tk.Entry(window, font=('Arial', 11), width=25)
        cat_entry.pack(pady=5)
        
        tk.Label(window, text="New Price (optional):", font=('Arial', 11)).pack(pady=5)
        price_entry = tk.Entry(window, font=('Arial', 11), width=25)
        price_entry.pack(pady=5)
        
        def update():
            try:
                prod_id = int(id_entry.get())
                
                if prod_id not in products_db:
                    messagebox.showerror("Error", "Product not found!")
                    return
                
                if name_entry.get():
                    products_db[prod_id]['name'] = name_entry.get()
                if cat_entry.get():
                    cat_id = int(cat_entry.get())
                    if cat_id in categories_db:
                        products_db[prod_id]['category_id'] = cat_id
                if price_entry.get():
                    products_db[prod_id]['price'] = float(price_entry.get())
                
                messagebox.showinfo("Success", "Product updated successfully!")
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Update", font=('Arial', 11), 
                 bg='#f39c12', fg='white', width=15, command=update).pack(pady=10)
    
    def delete_product(self):
        if not self.is_admin():
            messagebox.showerror("Error", "Only admin can delete products!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Delete Product")
        window.geometry("400x200")
        
        tk.Label(window, text="Delete Product", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Product ID:", font=('Arial', 11)).pack(pady=5)
        id_entry = tk.Entry(window, font=('Arial', 11), width=25)
        id_entry.pack(pady=5)
        
        def delete():
            try:
                prod_id = int(id_entry.get())
                
                if prod_id in products_db:
                    del products_db[prod_id]
                    messagebox.showinfo("Success", "Product deleted successfully!")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Product not found!")
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Delete", font=('Arial', 11), 
                 bg='#e74c3c', fg='white', width=15, command=delete).pack(pady=10)
    
    def add_category(self):
        if not self.is_admin():
            messagebox.showerror("Error", "Only admin can add categories!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Add Category")
        window.geometry("400x200")
        
        tk.Label(window, text="Add New Category", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Category Name:", font=('Arial', 11)).pack(pady=5)
        name_entry = tk.Entry(window, font=('Arial', 11), width=25)
        name_entry.pack(pady=5)
        
        def add():
            name = name_entry.get()
            if name:
                categories_db[self.next_category_id] = name
                messagebox.showinfo("Success", 
                    f"Category added! Category ID: {self.next_category_id}")
                self.next_category_id += 1
                window.destroy()
            else:
                messagebox.showerror("Error", "Please enter category name!")
        
        tk.Button(window, text="Add Category", font=('Arial', 11), 
                 bg='#9b59b6', fg='white', width=15, command=add).pack(pady=10)
    
    def delete_category(self):
        if not self.is_admin():
            messagebox.showerror("Error", "Only admin can delete categories!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Delete Category")
        window.geometry("400x200")
        
        tk.Label(window, text="Delete Category", font=('Arial', 16, 'bold')).pack(pady=20)
        
        tk.Label(window, text="Category ID:", font=('Arial', 11)).pack(pady=5)
        id_entry = tk.Entry(window, font=('Arial', 11), width=25)
        id_entry.pack(pady=5)
        
        def delete():
            try:
                cat_id = int(id_entry.get())
                
                if cat_id in categories_db:
                    products_in_cat = [p for p in products_db.values() 
                                      if p['category_id'] == cat_id]
                    if products_in_cat:
                        messagebox.showerror("Error", 
                            f"Cannot delete! {len(products_in_cat)} products in this category.")
                    else:
                        del categories_db[cat_id]
                        messagebox.showinfo("Success", "Category deleted successfully!")
                        window.destroy()
                else:
                    messagebox.showerror("Error", "Category not found!")
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")
        
        tk.Button(window, text="Delete", font=('Arial', 11), 
                 bg='#c0392b', fg='white', width=15, command=delete).pack(pady=10)
    
    def logout(self):
        if self.current_session:
            if self.current_session in cart_db:
                del cart_db[self.current_session]
            if self.current_session in sessions_db:
                del sessions_db[self.current_session]
            self.current_session = None
        messagebox.showinfo("Success", "Logged out successfully!")
        self.show_welcome_screen()
    
    def is_user(self):
        if not self.current_session or self.current_session not in sessions_db:
            return False
        return sessions_db[self.current_session]['role'] == 'user'
    
    def is_admin(self):
        if not self.current_session or self.current_session not in sessions_db:
            return False
        return sessions_db[self.current_session]['role'] == 'admin'

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingAppGUI(root)
    root.mainloop()