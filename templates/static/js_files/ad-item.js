$(document).ready(function() {
    $('#add-ice-cream-btn').on('click', function() {

        var name = $('#ice_cream_name').val();
        var flavour = $('#ice_cream_flavour').val();
        var weight = $('#ice_cream_weight').val();
//        Validating Empty fields
        if (!name || !flavour || !weight){
            alert("All fields are mandatory. Please fill in all fields");
            return;
        }
//        validating ice cream name
        if (!/^[a-zA-Z\s]+$/.test(name)) {
            alert("Ice Cream Name must contain only letters and spaces.");
            return;
        }
//        validating ice cream flavour
        if (!/^[a-zA-Z\s]+$/.test(flavour)) {
            alert("Ice Cream Flavour must contain only letters and spaces.");
            return;
        }
//        validating ice cream weight
        if (isNaN(weight) || weight <= 0) {
            alert("Ice Cream Weight must be a positive number.");
            return;
        }
//        console.log(name,flavour,weight);
        var formData = {
            'ice_cream_name': name,
            'ice_cream_flavour': flavour,
            'ice_cream_weight': weight
        };
        // Get the CSRF token
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
//        console.log("CSRF Token:", csrfToken);

        // Make an AJAX POST request to add the new item
        $.ajax({
            url: '/menu-app/add-item/',
            type: 'POST',
            data: formData,
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response) {
                console.log(32,response)
                alert('Item Added Successfully');
                $('#add-item-form')[0].reset();
            },
            error: function(xhr, status, error) {
                errorCode = xhr.responseJSON['error'];
                alert('Failed To Add Item...! Enter Valid Details');

            }
        });
    });
});
