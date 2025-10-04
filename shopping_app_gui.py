import streamlit as st
import uuid

# Demo Databases
if 'users_db' not in st.session_state:
    st.session_state.users_db = {
        'user1': {'password': 'pass123', 'name': 'John Doe'},
        'user2': {'password': 'pass456', 'name': 'Jane Smith'}
    }

if 'admin_db' not in st.session_state:
    st.session_state.admin_db = {
        'admin': {'password': 'admin123', 'name': 'Administrator'}
    }

if 'categories_db' not in st.session_state:
    st.session_state.categories_db = {
        1: 'Boots',
        2: 'Coats',
        3: 'Jackets',
        4: 'Caps'
    }

if 'products_db' not in st.session_state:
    st.session_state.products_db = {
        101: {'name': 'Leather Boots', 'category_id': 1, 'price': 89.99},
        102: {'name': 'Winter Boots', 'category_id': 1, 'price': 79.99},
        103: {'name': 'Rain Coat', 'category_id': 2, 'price': 59.99},
        104: {'name': 'Wool Coat', 'category_id': 2, 'price': 129.99},
        105: {'name': 'Denim Jacket', 'category_id': 3, 'price': 69.99},
        106: {'name': 'Leather Jacket', 'category_id': 3, 'price': 149.99},
        107: {'name': 'Baseball Cap', 'category_id': 4, 'price': 19.99},
        108: {'name': 'Beanie Cap', 'category_id': 4, 'price': 14.99}
    }

if 'cart' not in st.session_state:
    st.session_state.cart = {}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_role' not in st.session_state:
    st.session_state.user_role = None

if 'username' not in st.session_state:
    st.session_state.username = None

if 'next_product_id' not in st.session_state:
    st.session_state.next_product_id = 109

if 'next_category_id' not in st.session_state:
    st.session_state.next_category_id = 5

# Page config
st.set_page_config(page_title="SUPER DECCAN", page_icon="🛒", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2c3e50;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.username = None
    st.session_state.cart = {}
    st.rerun()

def login_page():
    st.markdown('<div class="main-header">🛒 Welcome to SUPER DECCAN</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["👤 User Login", "🔐 Admin Login"])
        
        with tab1:
            st.subheader("User Login")
            username = st.text_input("Username", key="user_username")
            password = st.text_input("Password", type="password", key="user_password")
            
            if st.button("Login as User", key="user_login_btn"):
                if username in st.session_state.users_db and st.session_state.users_db[username]['password'] == password:
                    st.session_state.logged_in = True
                    st.session_state.user_role = 'user'
                    st.session_state.username = username
                    st.success(f"Welcome {st.session_state.users_db[username]['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid credentials!")
        
        with tab2:
            st.subheader("Admin Login")
            admin_username = st.text_input("Username", key="admin_username")
            admin_password = st.text_input("Password", type="password", key="admin_password")
            
            if st.button("Login as Admin", key="admin_login_btn"):
                if admin_username in st.session_state.admin_db and st.session_state.admin_db[admin_username]['password'] == admin_password:
                    st.session_state.logged_in = True
                    st.session_state.user_role = 'admin'
                    st.session_state.username = admin_username
                    st.success(f"Welcome {st.session_state.admin_db[admin_username]['name']}!")
                    st.rerun()
                else:
                    st.error("Invalid admin credentials!")

def view_catalog():
    st.subheader("📦 Product Catalog")
    
    for cat_id, cat_name in sorted(st.session_state.categories_db.items()):
        st.markdown(f"### 🏷️ {cat_name}")
        
        products = [(pid, p) for pid, p in st.session_state.products_db.items() if p['category_id'] == cat_id]
        
        if products:
            cols = st.columns(3)
            for idx, (pid, product) in enumerate(products):
                with cols[idx % 3]:
                    st.info(f"**ID:** {pid}\n\n**{product['name']}**\n\nRs. {product['price']:.2f}")
        else:
            st.write("No products in this category")
        
        st.markdown("---")

def user_dashboard():
    st.markdown('<div class="main-header">🛒 SUPER DECCAN - User Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🚪 Logout"):
            logout()
    
    tab1, tab2, tab3, tab4 = st.tabs(["📦 Catalog", "🛒 Cart", "➕ Add to Cart", "💳 Checkout"])
    
    with tab1:
        view_catalog()
    
    with tab2:
        st.subheader("🛒 Your Shopping Cart")
        if not st.session_state.cart:
            st.info("Your cart is empty")
        else:
            total = 0
            for pid, qty in st.session_state.cart.items():
                if pid in st.session_state.products_db:
                    product = st.session_state.products_db[pid]
                    subtotal = product['price'] * qty
                    total += subtotal
                    
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{product['name']}** x{qty}")
                    with col2:
                        st.write(f"Rs. {subtotal:.2f}")
                    with col3:
                        if st.button("🗑️", key=f"remove_{pid}"):
                            del st.session_state.cart[pid]
                            st.rerun()
            
            st.markdown("---")
            st.subheader(f"**Total: Rs. {total:.2f}**")
    
    with tab3:
        st.subheader("➕ Add to Cart")
        
        col1, col2 = st.columns(2)
        with col1:
            product_id = st.number_input("Product ID", min_value=1, step=1)
        with col2:
            quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
        
        if st.button("Add to Cart"):
            if product_id in st.session_state.products_db:
                if product_id in st.session_state.cart:
                    st.session_state.cart[product_id] += quantity
                else:
                    st.session_state.cart[product_id] = quantity
                st.success(f"Added {quantity} x {st.session_state.products_db[product_id]['name']} to cart!")
            else:
                st.error("Product not found!")
    
    with tab4:
        st.subheader("💳 Checkout")
        
        if not st.session_state.cart:
            st.warning("Your cart is empty!")
        else:
            total = sum(st.session_state.products_db[pid]['price'] * qty 
                       for pid, qty in st.session_state.cart.items())
            
            st.info(f"**Total Amount: Rs. {total:.2f}**")
            
            payment_method = st.radio(
                "Select Payment Method:",
                ["Net Banking", "PayPal", "UPI", "Debit Card"]
            )
            
            if st.button("Complete Payment"):
                st.success(f"You will be redirected to {payment_method} portal to make payment of Rs. {total:.2f}")
                st.balloons()
                st.success("✅ Your order is successfully placed!")
                st.session_state.cart = {}

def admin_dashboard():
    st.markdown('<div class="main-header">🔐 SUPER DECCAN - Admin Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🚪 Logout"):
            logout()
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["📦 Catalog", "➕ Add Product", "✏️ Update Product", 
         "🗑️ Delete Product", "📁 Add Category", "🗑️ Delete Category"]
    )
    
    with tab1:
        view_catalog()
    
    with tab2:
        st.subheader("➕ Add New Product")
        
        name = st.text_input("Product Name")
        category_id = st.selectbox("Category", 
                                   options=list(st.session_state.categories_db.keys()),
                                   format_func=lambda x: st.session_state.categories_db[x])
        price = st.number_input("Price", min_value=0.0, step=0.01)
        
        if st.button("Add Product"):
            if name and price > 0:
                st.session_state.products_db[st.session_state.next_product_id] = {
                    'name': name,
                    'category_id': category_id,
                    'price': price
                }
                st.success(f"Product added! Product ID: {st.session_state.next_product_id}")
                st.session_state.next_product_id += 1
            else:
                st.error("Please fill all fields!")
    
    with tab3:
        st.subheader("✏️ Update Product")
        
        product_id = st.number_input("Product ID to Update", min_value=1, step=1)
        
        if product_id in st.session_state.products_db:
            current = st.session_state.products_db[product_id]
            st.info(f"Current: {current['name']} - Rs. {current['price']}")
            
            new_name = st.text_input("New Name (optional)", value=current['name'])
            new_category = st.selectbox("New Category", 
                                       options=list(st.session_state.categories_db.keys()),
                                       format_func=lambda x: st.session_state.categories_db[x],
                                       index=list(st.session_state.categories_db.keys()).index(current['category_id']))
            new_price = st.number_input("New Price", min_value=0.0, value=current['price'], step=0.01)
            
            if st.button("Update Product"):
                st.session_state.products_db[product_id] = {
                    'name': new_name,
                    'category_id': new_category,
                    'price': new_price
                }
                st.success("Product updated successfully!")
        else:
            st.warning("Product not found!")
    
    with tab4:
        st.subheader("🗑️ Delete Product")
        
        product_id = st.number_input("Product ID to Delete", min_value=1, step=1, key="delete_pid")
        
        if st.button("Delete Product"):
            if product_id in st.session_state.products_db:
                del st.session_state.products_db[product_id]
                st.success("Product deleted successfully!")
            else:
                st.error("Product not found!")
    
    with tab5:
        st.subheader("📁 Add New Category")
        
        category_name = st.text_input("Category Name")
        
        if st.button("Add Category"):
            if category_name:
                st.session_state.categories_db[st.session_state.next_category_id] = category_name
                st.success(f"Category added! Category ID: {st.session_state.next_category_id}")
                st.session_state.next_category_id += 1
            else:
                st.error("Please enter category name!")
    
    with tab6:
        st.subheader("🗑️ Delete Category")
        
        category_id = st.selectbox("Category to Delete", 
                                   options=list(st.session_state.categories_db.keys()),
                                   format_func=lambda x: st.session_state.categories_db[x])
        
        if st.button("Delete Category"):
            products_in_cat = [p for p in st.session_state.products_db.values() 
                              if p['category_id'] == category_id]
            if products_in_cat:
                st.error(f"Cannot delete! {len(products_in_cat)} products exist in this category.")
            else:
                del st.session_state.categories_db[category_id]
                st.success("Category deleted successfully!")

# Main app logic
if not st.session_state.logged_in:
    login_page()
elif st.session_state.user_role == 'user':
    user_dashboard()
elif st.session_state.user_role == 'admin':
    admin_dashboard()
