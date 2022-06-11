
    $(document).ready(function () {

        $('.increment-btn').click(function (e) {
            e.preventDefault();
            var incre_value = $(this).parents('.quantity').find('.qty-input').val();
            var value = parseInt(incre_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value<10){
                value++;
                $(this).parents('.quantity').find('.qty-input').val(value);
            }

        });

        $('.decrement-btn').click(function (e) {
            e.preventDefault();
            var decre_value = $(this).parents('.quantity').find('.qty-input').val();
            var value = parseInt(decre_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value>1){
                value--;
                $(this).parents('.quantity').find('.qty-input').val(value);
            }
        });
        
        $('.AddToCartbtn').click(function (e){
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var product_qty = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();

            $.ajax ({
                method: "POST",
                url: "/add-to-cart", 
                data: {
                    'product_id':product_id,
                    'product_qty': product_qty,
                    csrfmiddlewaretoken: token
                },
                
                success: function (response) {
                    alertify.success(response.status)
                    console.log(response.status)
                }
            });

        });
        $('.addtowishlist').click(function (e){
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();

            $.ajax ({
                method: "POST",
                url: "/add-to-wishlist", 
                data: {
                    'product_id':product_id,
                    csrfmiddlewaretoken: token
                },
                
                success: function (response) {
                    alertify.success(response.status)
                    console.log(response.status)
                }
            });

        });

        $('.changequantity').click(function (e){
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var product_qty = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();

            $.ajax ({
                method: "POST",
                url: "/updatecart", 
                data: {
                    'product_id':product_id,
                    'product_qty': product_qty,
                    csrfmiddlewaretoken: token
                },
                
                success: function (response) {
                    console.log(response.status)
                }
            });

        });
        
        $(document).on('click','.delete', function (e){
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();

            $.ajax ({
                method: "POST",
                url: "delete-cart-item", 
                data: {
                    'product_id':product_id,
                    csrfmiddlewaretoken: token
                },
                
                success: function (response) {
                    console.log(response.status)
                    $('.carddata').load(location.href +' .carddata');
                }
            });

        });
        $(document).on('click','.delete-wishlist-item', function (e){
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            console.log(product_id)

            $.ajax ({
                method: "POST",
                url: "/delete-wishlist-item", 
                data: {
                    'product_id':product_id,
                    csrfmiddlewaretoken: token
                },
                
                success: function (response) {
                    console.log(response.status)
                    $('.carddata').load(location.href +' .carddata');
                }
            });

        });
        

    });