$(document).ready(function () {
    // shop order
    $("#add_product_cart").on("click", function () {
        let quantity = $("#product-quantity").val();
        let product_size = $("#product_size").val();
        let product_id = $("#id_product_id").val();
        let this_val = $(this);
        console.log("produc_size:", product_size);
        console.log("produc_size:", product_size);
        console.log("quantity:", quantity);
        console.log("product_id:", product_id);
        console.log("current_element:", this_val);
        // add form ajax
        $.ajax({
            type: 'POST',
            url: '/add_to_cart',
            data: {
                'id': product_id,
                'qty': quantity,
                'pr_size': product_size,
            },
            beforeSend: function(){
                console.log('adding product to cart...');
            },
            success: function(){
                this_val.html("Item added to cart.");
                console.log("Product added to cart.");
            }

        })
        
    })

    // product size
    $('.btn-size').click(function () {
        var this_val = $(this).html();
        $("#product_size").val(this_val);
        $(".btn-size").removeClass('btn-secondary');
        $(".btn-size").addClass('btn-success');
        $(this).removeClass('btn-success');
        $(this).addClass('btn-secondary');
        return false;
    });
    //btn quantity
    $('#btn-minus').click(function () {
        var val = $("#var-value").html();
        val = (val == '1') ? val : val - 1;
        $("#var-value").html(val);
        $("#product-quantity").val(val);
        return false;
    });
    $('#btn-plus').click(function () {
        var val = $("#var-value").html();
        val + 1;
        $("#var-value").html(val);
        $("#product-quantity").val(val);
        return false;
    });
})