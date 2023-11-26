function add_product_to_order(productId) {
    const productCount = $('#product_count').val();
    $.get('/cart/add-product-to-order-me?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });
    })
}


function removeOrderDetail(detailId) {
    $.get('/cart/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

function changeOrderDetail(detailId, state) {
    $.get('/cart/change-order-detail?detail_id=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}


const faqContainers = document.querySelectorAll('.faq');

faqContainers.forEach(container => {
    const question = container.querySelector('.question');

    question.addEventListener('click', () => {
        container.classList.toggle('active');
        const answer = container.querySelector('.answer');
        answer.style.display = answer.style.display === 'none' ? 'block' : 'none';
    });
});
