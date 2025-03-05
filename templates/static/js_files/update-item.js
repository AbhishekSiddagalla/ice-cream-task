$(document).ready(function(){
    // get item id from the list of items
    var item_id = window.location.pathname.split('/')[3];
    // make an Ajax call to fetch item details
    $.ajax({
        url : `/menu-app/update-data/${item_id}/`,
        method : 'GET',
        success : function(response) {
            // fetch the details from response or from database
            $('#name').val(response.item_details.ice_cream_name);
            $('#flavour').val(response.item_details.ice_cream_flavour);
            $('#weight').val(response.item_details.ice_cream_weight);
        },
        error : function(xhr,status,error){
            console.error("Failed to Fetch Details" + error);
        }
    });
    //Handling save button click
    $('#save-button').click(function(){
        var name = $('#name').val();
        var flavour = $('#flavour').val();
        var weight = $('#weight').val();
        // validating fields
        if (!name || !flavour || !weight){
            alert("All Fields are mandatory. Please fill in the fields");
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
        var updatedData = {
            ice_cream_id : item_id,
            ice_cream_name : name,
            ice_cream_flavour : flavour,
            ice_cream_weight : weight
        };
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url : `/menu-app/update-data/${item_id}/`,
            method : 'POST',
            data : updatedData,
            headers: {
                'X-CSRFToken': csrfToken
            },
            success : function(response){
                alert('Item Updated Successfully')
                window.location.href = '/menu-app/menu/';
            },
            error : function(xhr,status,error){
                console.error('Failed to update item' + error);
            }
        });
    });
    $('#cancel-button').click(function(){
        window.location.href = '/menu-app/menu/'
    });
});