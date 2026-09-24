let products = [];
let cart = [];

// Get products from Django API
fetch('/api/products/')
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to load products");
        }

        return response.json();
    })
    .then(data => {

        console.log("Products received from Django:", data);

        products = data;

        displayProducts();
    })
    .catch(error => {
        console.error("Error loading products:", error);
    });


// Display Products
function displayProducts(productList = products) {

    const container = document.getElementById("product-container");

    container.innerHTML = "";

    productList.forEach(product => {

        container.innerHTML += `
            <div class="product-card">

                <img 
                    src="${product.image}"
                    alt="${product.name}"
                >

                <div class="product-info">

                    <h3>${product.name}</h3>

                    <p class="category">
                        ${product.category}
                    </p>

                    <p>${product.description || ""}</p>

                    <p class="brand">
                        Brand: ${product.brand || ""}
                    </p>

                    <p class="price">
                        ₹${Number(product.price).toLocaleString()}
                    </p>

                    <button 
                        class="add-btn"
                        onclick="addToCart(${product.id})"
                    >
                        Add to Cart
                    </button>

                </div>

            </div>
        `;
    });
}


// Add To Cart
function addToCart(id) {

    const product = products.find(p => p.id === id);

    if (!product) {
        return;
    }

    cart.push(product);

    document.getElementById("cart-count").textContent = cart.length;

    alert(`${product.name} added to cart!`);
}


// Show Cart
function showCart() {

    const modal = document.getElementById("cart-modal");
    const items = document.getElementById("cart-items");

    items.innerHTML = "";

    let total = 0;

    cart.forEach((product, index) => {

        total += Number(product.price);

        items.innerHTML += `
            <div class="cart-item">

                <span>
                    ${product.name}
                </span>

                <span>
                    ₹${Number(product.price).toLocaleString()}

                    <button onclick="removeFromCart(${index})">
                        ❌
                    </button>
                </span>

            </div>
        `;
    });

    document.getElementById("cart-total").textContent =
        total.toLocaleString();

    modal.style.display = "block";
}


// Close Cart
function closeCart() {

    document.getElementById("cart-modal").style.display = "none";
}


// Remove Cart Item
function removeFromCart(index) {

    cart.splice(index, 1);

    document.getElementById("cart-count").textContent = cart.length;

    showCart();
}


// Search
function searchProducts() {

    const search = document
        .getElementById("search")
        .value
        .toLowerCase();

    const filtered = products.filter(product =>
        product.name.toLowerCase().includes(search)
    );

    displayProducts(filtered);
}


// Category Filter
function filterCategory(category) {

    const filtered = products.filter(product =>
        product.category === category
    );

    displayProducts(filtered);

    document.getElementById("products").scrollIntoView();
}


// Sort Products
function sortProducts() {

    const value = document.getElementById("sort").value;

    let sorted = [...products];

    if (value === "low") {

        sorted.sort((a, b) =>
            Number(a.price) - Number(b.price)
        );

    } else if (value === "high") {

        sorted.sort((a, b) =>
            Number(b.price) - Number(a.price)
        );
    }

    displayProducts(sorted);
}