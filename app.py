import streamlit as st
import uuid

# Initialize session state
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
        101: {'name': 'Leather Boots', 'category_id': 1, 'price': 89.99, 'image': 'https://images.unsplash.com/photo-1605348532760-6753d2c43329?w=400'},
        102: {'name': 'Winter Boots', 'category_id': 1, 'price': 79.99, 'image': 'https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=400'},
        103: {'name': 'Rain Coat', 'category_id': 2, 'price': 59.99, 'image': 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=400'},
        104: {'name': 'Wool Coat', 'category_id': 2, 'price': 129.99, 'image': 'https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=400'},
        105: {'name': 'Denim Jacket', 'category_id': 3, 'price': 69.99, 'image': 'https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400'},
        106: {'name': 'Leather Jacket', 'category_id': 3, 'price': 149.99, 'image': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400'},
        107: {'name': 'Baseball Cap', 'category_id': 4, 'price': 19.99, 'image': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=400'},
        108: {'name': 'Beanie Cap', 'category_id': 4, 'price': 14.99, 'image': 'https://images.unsplash.com/photo-1576871337622-98d48d1cf531?w=400'}
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

# Page configuration
st.set_page_config(
    page_title="SUPER DECCAN",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .product-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .product-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        padding: 12px;
        font-weight: bold;
    }
    .category-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0 10px 0;
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
        st.markdown("### 🔐 Login to Continue")
        
        login_type = st.radio("Select Login Type:", ["👤 User Login", "🔐 Admin Login"], horizontal=True)
        
        st.markdown("---")
        
        if login_type == "👤 User Login":
            st.subheader("User Login")
            with st.form("user_login_form"):
                username = st.text_input("Username", placeholder="Enter username")
                password = st.text_input("Password", type="password", placeholder="Enter password")
                submit = st.form_submit_button("🚀 Login as User", use_container_width=True)
                
                if submit:
                    if username in st.session_state.users_db and st.session_state.users_db[username]['password'] == password:
                        st.session_state.logged_in = True
                        st.session_state.user_role = 'user'
                        st.session_state.username = username
                        st.success(f"✅ Welcome {st.session_state.users_db[username]['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials!")
            
            st.info("💡 Demo User: username=`user1`, password=`pass123`")
        
        else:
            st.subheader("Admin Login")
            with st.form("admin_login_form"):
                admin_username = st.text_input("Admin Username", placeholder="Enter admin username")
                admin_password = st.text_input("Admin Password", type="password", placeholder="Enter admin password")
                submit = st.form_submit_button("🔐 Login as Admin", use_container_width=True)
                
                if submit:
                    if admin_username in st.session_state.admin_db and st.session_state.admin_db[admin_username]['password'] == admin_password:
                        st.session_state.logged_in = True
                        st.session_state.user_role = 'admin'
                        st.session_state.username = admin_username
                        st.success(f"✅ Welcome {st.session_state.admin_db[admin_username]['name']}!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid admin credentials!")
            
            st.info("💡 Demo Admin: username=`admin`, password=`admin123`")

def view_catalog():
    st.subheader("📦 Product Catalog")
    
    for cat_id, cat_name in sorted(st.session_state.categories_db.items()):
        st.markdown(f'<div class="category-header">🏷️ {cat_name}</div>', unsafe_allow_html=True)
        
        products = [(pid, p) for pid, p in st.session_state.products_db.items() if p['category_id'] == cat_id]
        
        if products:
            cols = st.columns(3)
            for idx, (pid, product) in enumerate(products):
                with cols[idx % 3]:
                    with st.container():
                        # Display product image
                        if 'image' in product and product['image']:
                            st.image(product['image'], use_container_width=True)
                        else:
                            st.image('https://via.placeholder.com/400x300?text=No+Image', use_container_width=True)
                        
                        st.markdown(f"**{product['name']}**")
                        st.markdown(f"**ID:** {pid}")
                        st.markdown(f"**Price:** Rs. {product['price']:.2f}")
                        st.markdown("---")
        else:
            st.info("No products in this category")

def user_dashboard():
    st.markdown('<div class="main-header">🛒 SUPER DECCAN - User Dashboard</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.users_db[st.session_state.username]['name']}")
        st.markdown("**Role:** User")
        st.markdown("---")
        
        cart_count = sum(st.session_state.cart.values())
        st.metric("🛒 Items in Cart", cart_count)
        
        if st.session_state.cart:
            total = sum(st.session_state.products_db[pid]['price'] * qty 
                       for pid, qty in st.session_state.cart.items() 
                       if pid in st.session_state.products_db)
            st.metric("💰 Cart Total", f"Rs. {total:.2f}")
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    # Main content
    tab1, tab2, tab3, tab4 = st.tabs(["📦 Browse Catalog", "🛒 My Cart", "➕ Add to Cart", "💳 Checkout"])
    
    with tab1:
        view_catalog()
    
    with tab2:
        st.subheader("🛒 Your Shopping Cart")
        
        if not st.session_state.cart:
            st.info("🛍️ Your cart is empty. Start shopping!")
        else:
            total = 0
            
            for pid, qty in list(st.session_state.cart.items()):
                if pid in st.session_state.products_db:
                    product = st.session_state.products_db[pid]
                    subtotal = product['price'] * qty
                    total += subtotal
                    
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    with col1:
                        st.write(f"**{product['name']}**")
                    with col2:
                        st.write(f"Qty: {qty}")
                    with col3:
                        st.write(f"Rs. {subtotal:.2f}")
                    with col4:
                        if st.button("🗑️ Remove", key=f"remove_{pid}"):
                            del st.session_state.cart[pid]
                            st.rerun()
                    
                    st.markdown("---")
            
            st.markdown(f"### **Total: Rs. {total:.2f}**")
    
    with tab3:
        st.subheader("➕ Add Items to Cart")
        
        with st.form("add_to_cart_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                product_id = st.number_input("Product ID", min_value=1, step=1, help="Enter the product ID from catalog")
            
            with col2:
                quantity = st.number_input("Quantity", min_value=1, value=1, step=1)
            
            submitted = st.form_submit_button("🛒 Add to Cart", use_container_width=True)
            
            if submitted:
                if product_id in st.session_state.products_db:
                    if product_id in st.session_state.cart:
                        st.session_state.cart[product_id] += quantity
                    else:
                        st.session_state.cart[product_id] = quantity
                    st.success(f"✅ Added {quantity} x {st.session_state.products_db[product_id]['name']} to cart!")
                    st.rerun()
                else:
                    st.error("❌ Product not found! Please check the Product ID.")
        
        st.info("💡 Tip: View the catalog to see available Product IDs")
    
    with tab4:
        st.subheader("💳 Checkout")
        
        if not st.session_state.cart:
            st.warning("⚠️ Your cart is empty! Add items before checkout.")
        else:
            total = sum(st.session_state.products_db[pid]['price'] * qty 
                       for pid, qty in st.session_state.cart.items()
                       if pid in st.session_state.products_db)
            
            st.markdown(f"### **Total Amount: Rs. {total:.2f}**")
            st.markdown("---")
            
            st.markdown("#### Select Payment Method")
            payment_method = st.radio(
                "Choose your preferred payment option:",
                ["💰 Net Banking", "💳 PayPal", "📱 UPI", "💳 Debit Card"],
                label_visibility="collapsed"
            )
            
            st.markdown("---")
            
            if st.button("✅ Complete Payment", use_container_width=True, type="primary"):
                st.success(f"🎉 You will be redirected to {payment_method.split()[1]} portal to make payment of Rs. {total:.2f}")
                st.balloons()
                st.success("✅ Your order is successfully placed!")
                st.info("📧 Order confirmation has been sent to your email.")
                st.session_state.cart = {}
                st.rerun()

def admin_dashboard():
    st.markdown('<div class="main-header">🔐 SUPER DECCAN - Admin Dashboard</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 🔐 {st.session_state.admin_db[st.session_state.username]['name']}")
        st.markdown("**Role:** Administrator")
        st.markdown("---")
        
        st.metric("📦 Total Products", len(st.session_state.products_db))
        st.metric("📁 Total Categories", len(st.session_state.categories_db))
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    # Main content
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["📦 View Catalog", "➕ Add Product", "✏️ Update Product", 
         "🗑️ Delete Product", "📁 Add Category", "🗑️ Delete Category"]
    )
    
    with tab1:
        view_catalog()
    
    with tab2:
        st.subheader("➕ Add New Product")
        
        with st.form("add_product_form"):
            name = st.text_input("Product Name", placeholder="e.g., Nike Shoes")
            
            category_id = st.selectbox(
                "Category",
                options=list(st.session_state.categories_db.keys()),
                format_func=lambda x: st.session_state.categories_db[x]
            )
            
            price = st.number_input("Price (Rs.)", min_value=0.0, step=0.01, format="%.2f")
            
            image_url = st.text_input("Image URL", placeholder="https://example.com/image.jpg", help="Enter a direct image URL (optional)")
            
            submitted = st.form_submit_button("➕ Add Product", use_container_width=True)
            
            if submitted:
                if name and price > 0:
                    new_id = st.session_state.next_product_id
                    st.session_state.products_db[new_id] = {
                        'name': name,
                        'category_id': category_id,
                        'price': price,
                        'image': image_url if image_url else 'https://via.placeholder.com/400x300?text=No+Image'
                    }
                    st.success(f"✅ Product added successfully! Product ID: {new_id}")
                    st.session_state.next_product_id += 1
                else:
                    st.error("❌ Please fill all fields with valid data!")
        
        st.info("💡 **Tip:** Use free image hosting services like Unsplash, Imgur, or upload to Google Drive and use the direct link")
    
    with tab3:
        st.subheader("✏️ Update Product")
        
        product_id = st.number_input("Enter Product ID to Update", min_value=1, step=1, key="update_pid")
        
        if product_id in st.session_state.products_db:
            current = st.session_state.products_db[product_id]
            
            col1, col2 = st.columns([1, 2])
            with col1:
                if 'image' in current and current['image']:
                    st.image(current['image'], caption="Current Image", width=200)
            with col2:
                st.info(f"**Current Product:** {current['name']} - Rs. {current['price']:.2f}")
            
            with st.form("update_product_form"):
                new_name = st.text_input("New Product Name", value=current['name'])
                
                current_cat_index = list(st.session_state.categories_db.keys()).index(current['category_id'])
                new_category = st.selectbox(
                    "New Category",
                    options=list(st.session_state.categories_db.keys()),
                    format_func=lambda x: st.session_state.categories_db[x],
                    index=current_cat_index
                )
                
                new_price = st.number_input("New Price (Rs.)", min_value=0.0, value=current['price'], step=0.01, format="%.2f")
                
                new_image = st.text_input("New Image URL", value=current.get('image', ''), placeholder="https://example.com/image.jpg")
                
                submitted = st.form_submit_button("✏️ Update Product", use_container_width=True)
                
                if submitted:
                    st.session_state.products_db[product_id] = {
                        'name': new_name,
                        'category_id': new_category,
                        'price': new_price,
                        'image': new_image if new_image else 'https://via.placeholder.com/400x300?text=No+Image'
                    }
                    st.success("✅ Product updated successfully!")
                    st.rerun()
        else:
            st.warning("⚠️ Product ID not found. Please enter a valid Product ID.")
    
    with tab4:
        st.subheader("🗑️ Delete Product")
        
        with st.form("delete_product_form"):
            product_id = st.number_input("Enter Product ID to Delete", min_value=1, step=1, key="delete_pid")
            
            submitted = st.form_submit_button("🗑️ Delete Product", use_container_width=True, type="primary")
            
            if submitted:
                if product_id in st.session_state.products_db:
                    product_name = st.session_state.products_db[product_id]['name']
                    del st.session_state.products_db[product_id]
                    st.success(f"✅ Product '{product_name}' deleted successfully!")
                    st.rerun()
                else:
                    st.error("❌ Product not found!")
    
    with tab5:
        st.subheader("📁 Add New Category")
        
        with st.form("add_category_form"):
            category_name = st.text_input("Category Name", placeholder="e.g., Shoes, Accessories")
            
            submitted = st.form_submit_button("📁 Add Category", use_container_width=True)
            
            if submitted:
                if category_name:
                    new_cat_id = st.session_state.next_category_id
                    st.session_state.categories_db[new_cat_id] = category_name
                    st.success(f"✅ Category '{category_name}' added! Category ID: {new_cat_id}")
                    st.session_state.next_category_id += 1
                else:
                    st.error("❌ Please enter a category name!")
    
    with tab6:
        st.subheader("🗑️ Delete Category")
        
        with st.form("delete_category_form"):
            category_id = st.selectbox(
                "Select Category to Delete",
                options=list(st.session_state.categories_db.keys()),
                format_func=lambda x: f"{st.session_state.categories_db[x]} (ID: {x})"
            )
            
            submitted = st.form_submit_button("🗑️ Delete Category", use_container_width=True, type="primary")
            
            if submitted:
                products_in_cat = [p for p in st.session_state.products_db.values() 
                                  if p['category_id'] == category_id]
                
                if products_in_cat:
                    st.error(f"❌ Cannot delete! {len(products_in_cat)} product(s) exist in this category. Please delete or move those products first.")
                else:
                    cat_name = st.session_state.categories_db[category_id]
                    del st.session_state.categories_db[category_id]
                    st.success(f"✅ Category '{cat_name}' deleted successfully!")
                    st.rerun()

# Main application logic
def main():
    if not st.session_state.logged_in:
        login_page()
    elif st.session_state.user_role == 'user':
        user_dashboard()
    elif st.session_state.user_role == 'admin':
        admin_dashboard()

if __name__ == "__main__":
    main()