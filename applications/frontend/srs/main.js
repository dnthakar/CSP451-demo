async function loadProducts() {
    const res = await fetch('/api/v1/products');
    const products = await res.json();
    const container = document.getElementById('products');
    products.forEach(p => {
        const div = document.createElement('div');
        div.textContent = `${p.name} - $${p.price}`;
        container.appendChild(div);
    });
}

loadProducts();
