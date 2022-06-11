$(document).ready(function () {
    console.log("first");


    $('.razorpay').click(function (e){
        e.preventDefault();
        var fname = $("[name='firstName']").val();
        var lname = $('[name="lastName"]').val();
        var email = $('[name="email"]').val();
        var phone = $('[name="phone"]').val();
        var address = $('[name="address"]').val();
        var country = $('[name="country"]').val(); 
        var state= $('[name="state"]').val();
        var pincode = $('[name="zip"]').val();
        var token= $('[name="csrfmiddlewaretoken"]').val();

        if (fname == '' || lname == '' || email == '' || address == '' ||country  == '' || state == '' || pincode == '' || phone=='')
        {
            swal("All Fields Are Mandatory",'error');
            return false;
        }
        else
        {
            $.ajax({ 
                method: "GET",
                url: "/proceed-to-pay",
                success:function(response){
                    // console.log(response);
                    var options = {
                        "key": "rzp_test_gHjQSl8uEHyrkC", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Ustora",
                        "description": "Thank you for buying from Us",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response2){
                            alert(response2.razorpay_payment_id);
                            data = {
                                'fname': fname,  
                                'lname': lname,  
                                'email': email,  
                                'phone': phone,  
                                'address' :ddress,  
                                'country' :ountry,  
                                'state': state,  
                                'pincode' :incode,
                                'payment_mode' :'Paid by Razorpay' ,
                                'payment_id': response2.razorpay_payment_id,
                                csrfmiddlewaretoken:token
                                
                            }
                            $.ajax({
                                method: 'POST',
                                url:'/place-order',
                                data:data,
                                success:function (response3){
                                    swal("Concragulations",response3.status,'success').then((value) => {
                                         window.location.href = '/my-orers '
                                      });
                                    return false;

                                }
                            })
                           
                        },
                        "prefill": {
                            "name": fname+' '+lname,
                            "email": email,
                            "contact": phone,
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    
                
                    rzp1.open();

                }
            });
           
        

        }

        

    });

});