let cartCount = 0;

function addToCart(button) {
    const productCard = button.parentElement;
    const productName = productCard.getAttribute('data-name');
    const productPrice = productCard.getAttribute('data-price');

    cartCount++;
    document.getElementById('cart-count').innerText = cartCount;

    alert(`${productName} has been added to the cart for $${productPrice}!`);
}
